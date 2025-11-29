from backend.vectorstore.code_indexer import CodeIndexer
from backend.agent.registry import current_state

class CodeSearch:
    @staticmethod
    def run(modify_prompt: str):
        indexer = CodeIndexer()
        results = indexer.search(modify_prompt)
        current_state.search_results = results
        return results