import os
from fastapi import UploadFile
import shutil

UPLOAD_DIR = "data/"

async def save_uploaded_files(files: list[UploadFile]):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_paths = []
    for file in files:
        path = os.path.join(UPLOAD_DIR, file.filename)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_paths.append(path)
    return file_paths