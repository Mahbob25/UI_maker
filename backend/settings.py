# to help solving the problem of paths in different file systems
import os
from pathlib import Path

# Detect if running in Cloud Functions/Run
IS_CLOUD = os.environ.get("K_SERVICE") or os.environ.get("FUNCTION_TARGET")

BASE_DIR = Path(__file__).resolve().parent.parent

if IS_CLOUD:
    # In Cloud Functions, only /tmp is writable
    GENERATED_DIR = Path("/tmp") / "generated_output"
else:
    GENERATED_DIR = BASE_DIR / "generated_output"

print(f"Environment: {'CLOUD' if IS_CLOUD else 'LOCAL'}")
print(f"BASE_DIR: {BASE_DIR}")
print(f"GENERATED_DIR: {GENERATED_DIR}")