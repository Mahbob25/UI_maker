import os
import base64

def load_response_folder(folder_path: str):
    files_json = []

    for root, _, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(root, filename)

            with open(full_path, "rb") as f:
                raw = f.read()

            # detect encoding
            try:
                # try to decode as utf-8 (works for text)
                content = raw.decode("utf-8")
                encoding = "utf-8"
            except:
                # if binary → Base64
                content = base64.b64encode(raw).decode("utf-8")
                encoding = "base64"

            relative_path = os.path.relpath(full_path, folder_path)

            files_json.append({
                "path": relative_path.replace("\\", "/"),
                "content": content,
                "encoding": encoding
            })

    return files_json
