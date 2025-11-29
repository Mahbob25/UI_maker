from backend.vectorstore.code_indexer import CodeIndexer

indexer = CodeIndexer()
indexer.index_project("generated_output/src/app")

print("\n--- Running Search Query ---")
results = indexer.search("change Password Recovery headline to forget password")

for i, r in enumerate(results):
   
    ram = f"""
\n--- Match {i+1} ---
{"FILE:", r.metadata["file"]}
{"LINES:", r.metadata["start_line"], "-", r.metadata["end_line"]}
{r.page_content}
"""

print(ram)