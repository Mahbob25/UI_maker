# import shutil
# from pathlib import Path
# import os

# def zip_folder(src, dest):
#     # src: folder you want to zip
#     # dest: where you want the zip file stored
    
#     src_path = Path(src)
#     dest_path = Path(dest)

#     zip_name = dest_path / src_path.name  # e.g. D:\...\agent_coder\generated_output.zip
    
#     shutil.make_archive(str(zip_name), 'zip', root_dir=str(src_path))

#     try:
#         shutil.rmtree(src_path)
#         print(f"Folder '{src_path}' deleted successfully.")
#     except OSError as e:
#         print(f"Error deleting folder: {e}")


import zipfile
from pathlib import Path
import os

def zip_folder(src: str | Path, dest: str | Path):
    src_path = Path(src).resolve()
    dest_path = Path(dest).resolve()
    dest_path.mkdir(parents=True, exist_ok=True)
    
    zip_path = dest_path / f"{src_path.name}.zip"
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(src_path):
            for file in files:
                full_path = Path(root) / file

                # FIX: remove the root folder from inside the ZIP
                arcname = full_path.relative_to(src_path)

                zipf.write(full_path, arcname)
    
    print(f"Zip created: {zip_path}")
    return zip_path  # <- helpful for API