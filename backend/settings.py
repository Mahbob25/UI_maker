# to help solving the problem of paths in different file systems
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

GENERATED_DIR = BASE_DIR / "generated_output"
print(GENERATED_DIR)