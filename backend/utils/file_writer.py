import os
from typing import Dict
import shutil
from pathlib import Path


class FileWriter:
    
    # this responsible for writing generated files to disk.
    

    def __init__(self, output_dir: str): #  the outpur dir.
        
        self.output_dir = Path(output_dir)

    def write_files(self, files_json: Dict[str, Dict[str, str]], with_template=True):
        """
        Takes a dict of file paths and content and writes them to disk.

      
        """
        if with_template:
            print("copying base Angular project.....", "="*50)
            self._copy_base_template()
        else:
            print("Skipping template copy (modify workflow only)....")

        print(f"\n==> Writing project files into: {self.output_dir}\n")

        for rel_path, file_data in files_json.items():
            try:
                
                self._write_single_file(rel_path, file_data.get("content", ""))
            except Exception as e:
                print(f"X ERROR writing {rel_path}: {e}")

        print("\n(: Done writing files.\n")

    

    def _write_single_file(self, rel_path: str, content: str):
        # normalize input
        content = (content or "").strip()
        if not content:
            print(f"!! SKIPPED (empty file): {rel_path}")
            return

        # If user passed an absolute path, convert to a path relative to output_dir if possible
        p = Path(rel_path)
        if p.is_absolute():
            try:
                rel = os.path.relpath(str(p), str(self.output_dir))
            except Exception:
                # fallback to basename
                rel = p.name
        else:
            # ensure consistent forward slashes
            rel = str(rel_path).replace(os.path.sep, '/')

        # If rel already contains output_dir prefix like "generated_output/src/app/..."
        # strip any leading output_dir segments
        if rel.startswith(str(self.output_dir.name) + "/"):
            # take part after the output_dir name
            rel = rel.split(str(self.output_dir.name) + "/", 1)[1]

        # Ensure it starts with src/app/ (your app layout)
        rel = rel.lstrip("/")

        # Remove accidental duplicated prefixes like "src/app/src/app/"
        while rel.startswith("src/app/src/app/"):
            rel = rel.replace("src/app/src/app/", "src/app/", 1)

        # If it doesn't start with src/, FORCE it to be in src/app/
        if not rel.startswith("src/"):
            rel = "src/app/" + rel

        full_path = os.path.join(str(self.output_dir), rel)
        folder = os.path.dirname(full_path)

        os.makedirs(folder, exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"(: WROTE: {rel}")



    # def _copy_base_template(self):
    #     base_template = Path("backend/workflow/angular_base_template")
    #     if not self.output_dir.exists():
    #         shutil.copytree(base_template, self.output_dir)
    #         print("(-_-) Base template copied.")
    #     else:
    #         print("[-_-] Base template already exists. Reusing it.")


    def _copy_base_template(self):
        base_template_app = Path("backend/workflow/angular_base_template/src/app")
        target_app = self.output_dir / "src" / "app"

        # ❗ Always remove the existing app folder (if any)
        if target_app.exists():
            shutil.rmtree(target_app)

        # ❗ Copy the template's app folder into the generated folder
        shutil.copytree(base_template_app, target_app)

        print("(-_-) Fresh Angular app template copied.")
