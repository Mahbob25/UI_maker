import re

class SymbolExtractor:
    """
    Extracts exported symbol names (classes, interfaces, enums, functions)
    from raw TypeScript code strings.
    """

    # Regex patterns for different symbol types
    PATTERNS = {
        "class": r"export\s+class\s+([A-Za-z0-9_]+)",
        "interface": r"export\s+interface\s+([A-Za-z0-9_]+)",
        "enum": r"export\s+enum\s+([A-Za-z0-9_]+)",
        "function": r"export\s+function\s+([A-Za-z0-9_]+)"
    }

    @staticmethod
    def extract_symbols(ts_code: str) -> list[dict]:
        """
        Extracts symbol name and type, returns:
        [
          {"symbol": "AuthService", "type": "class"},
          {"symbol": "UserModel", "type": "interface"}
        ]
        """
        results = []

        for sym_type, pattern in SymbolExtractor.PATTERNS.items():
            matches = re.findall(pattern, ts_code)
            for name in matches:
                results.append({"symbol": name, "type": sym_type})

        return results
