import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma # Note: Using langchain_chroma for modern integration
from google import genai
from google.genai import types
import numpy as np
from backend.utils.llm_client import LLMClient

EMBEDDING_MODEL_NAME = "text-embedding-004" # Using the latest recommended embedding model

class EmbeddingClient:
    """
    A wrapper class for the Google GenAI Embedding API, made compatible with 
    the LangChain Embeddings interface by implementing embed_documents and embed_query.
    """
    def __init__(self):
        # Initialize the Google GenAI client
        self.client = LLMClient.get()

    # 1. Renamed from embed_text to embed_documents to satisfy LangChain interface
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """
        Embeds a list of texts (documents) and returns a list of embedding vectors.
        """
        if not texts:
            return []
            
        # Call the Google GenAI API for embedding content
        result = self.client.models.embed_content(
            model=EMBEDDING_MODEL_NAME,
            contents=texts,
            # Use 'RETRIEVAL_DOCUMENT' for indexing documents
            config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")
        )

        # Convert the embedding results to a list of standard Python lists (float)
        # Chroma expects the output to be list[list[float]], not numpy arrays.
        return [e.values for e in result.embeddings]
    
    # 2. Added embed_query, required for similarity search
    def embed_query(self, text: str) -> list[float]:
        """
        Embeds a single text (query) and returns the embedding vector.
        """
        # Call the Google GenAI API for embedding content
        result = self.client.models.embed_content(
            model=EMBEDDING_MODEL_NAME,
            contents=[text],
            # Use 'RETRIEVAL_QUERY' for searching/querying
            config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
        )
        
        # Return the single embedding vector as a standard Python list
        return result.embeddings[0].values


class CodeIndexer:
    def __init__(self, chroma_path="chroma_code_index"):
        self.chroma_path = chroma_path

        # Initialize the compliant embedding model
        self.embedding_model = EmbeddingClient()

        self.db = Chroma(
            persist_directory=self.chroma_path,
            # 3. FIX: Pass the ENTIRE object, not just the method.
            # Chroma will internally call .embed_documents() and .embed_query()
            embedding_function=self.embedding_model 
        )

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", ""]
        )

    def _read_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def _file_to_chunks(self, file_path):
        raw = self._read_file(file_path)
        chunks = []

        for chunk in self.splitter.split_text(raw):
            # Calculate line numbers for metadata
            start = raw.index(chunk)
            start_line = raw[:start].count("\n") + 1
            end_line = start_line + chunk.count("\n")

            

            chunks.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "file": file_path,
                        "start_line": start_line,
                        "end_line": end_line
                    }
                )
            )
        return chunks

    def index_project(self, root_dir):
        print(f"Indexing files in {root_dir}...")
        docs = []
        for subdir, _, files in os.walk(root_dir):
            for f in files:
                if f.endswith((".ts", ".html", ".css", ".scss", ".json")):
                    path = os.path.join(subdir, f)
                    normalized_path = path.replace(os.path.sep, '/')
                    file_docs = self._file_to_chunks(normalized_path)
                    docs.extend(file_docs)
                    print(f"[+] Indexed {f} — {len(file_docs)} chunks")

        if docs:
            self.db.add_documents(docs)
            
            print(f"Indexing complete. Total documents added: {len(docs)}")
        else:
            print("X No documents found to index.")


    def update_file_chunks(self, updated_files: dict):
        """
        Incrementally update the vector DB for modified files.

        Accept two formats for updated_files:
        1) { "src/app/login.ts": "<content string>" }
        2) { "src/app/login.ts": {"content": "<content string>"} }
        """
        docs_to_add = []
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=40
        )

        for file_path, value in updated_files.items():
            # get content string no matter the input shape
            if isinstance(value, dict) and "content" in value:
                content = value["content"]
            elif isinstance(value, str):
                content = value
            else:
                raise ValueError(f"update_file_chunks: unsupported value for {file_path}: {type(value)}")

            if not isinstance(content, str):
                raise ValueError(f"update_file_chunks: content for {file_path} is not string")

            print(f" Updating index for modified file: {file_path}")

            # Remove old chunks for this file (collection-level delete)
            try:
                # depending on your vectorstore API - this is the pattern used earlier
                self.db._collection.delete(where={"file": file_path})
            except Exception:
                # safe fallback if delete API differs
                print(f" Warning: unable to delete old chunks for {file_path} using low-level API")

            # Split new content into chunks
            chunks = splitter.split_text(content)

            for idx, chunk in enumerate(chunks):
                doc = Document(
                    page_content=chunk,
                    metadata={
                        "file": file_path,
                        "chunk_id": idx
                    }
                )
                docs_to_add.append(doc)

            print(f"[+] Prepared {len(chunks)} fresh chunks for {file_path}")

        if docs_to_add:
            self.db.add_documents(docs_to_add)
            print(f"[✓] Re-indexed {len(docs_to_add)} chunks from updated files.")
        else:
            print("[X] No updated documents to index.")


    def search(self, query, k=5):
        """
        Searches the vector store using LangChain's internal search mechanism.
        LangChain handles embedding the query using the configured embed_query method.
        """
        # 4. FIX: Use similarity_search, which is the standard method, 
        # instead of similarity_search_by_vector. This ensures LangChain 
        # calls self.embedding_model.embed_query() internally.
        return self.db.similarity_search(query, k=k)



