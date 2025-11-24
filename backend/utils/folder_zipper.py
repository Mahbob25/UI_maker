import shutil
from pathlib import Path
import os

def zip_folder(src, dest):
    # src: folder you want to zip
    # dest: where you want the zip file stored
    
    src_path = Path(src)
    dest_path = Path(dest)

    zip_name = dest_path / src_path.name  # e.g. D:\...\agent_coder\generated_output.zip

    shutil.make_archive(str(zip_name), 'zip', root_dir=str(src_path))

    try:
        shutil.rmtree(src_path)
        print(f"Folder '{src_path}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting folder: {e}")





