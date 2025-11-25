import os
from typing import Dict
import shutil
from pathlib import Path


class FileWriter:
    
    # this responsible for writing generated files to disk.
    

    def __init__(self, output_dir: str): #  the outpur dir.
        
        self.output_dir = Path(output_dir)

    def write_files(self, files_json: Dict[str, Dict[str, str]]):
        """
        Takes a dict of file paths and content and writes them to disk.

      
        """
        print("copying base Angular project.....", "="*50)
        self._copy_base_template()

        print(f"\n==> Writing project files into: {self.output_dir}\n")

        for path, file_data in files_json.items():
            try:
                rel_path = "src/app/" + path
                self._write_single_file(rel_path, file_data.get("content", ""))
            except Exception as e:
                print(f"X ERROR writing {rel_path}: {e}")

        print("\n(: Done writing files.\n")

    

    def _write_single_file(self, rel_path: str, content: str):
        
        # Writes a single file to disk, skipping empty ones.
        
        content = (content or "").strip() # clean  file

        if not content:
            print(f"!! SKIPPED (empty file): {rel_path}")
            return

        full_path = os.path.join(self.output_dir, rel_path)
        folder = os.path.dirname(full_path)

        # Create directories if not exist
        os.makedirs(folder, exist_ok=True)

        # Overwrite file
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"(: WROTE: {rel_path}")


    def _copy_base_template(self):
        base_template = Path("backend/workflow/angular_base_template")
        if not self.output_dir.exists():
            shutil.copytree(base_template, self.output_dir)
            print("(-_-) Base template copied.")
        else:
            print("[-_-] Base template already exists. Reusing it.")