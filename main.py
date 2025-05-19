from fastapi import FastAPI, UploadFile, File
from services.file_utils import save_uploaded_files
from services.doc_processing import process_documents
from services.vectorizer import generate_embeddings, send_vectors_to_db

app = FastAPI()

@app.get("/health/")
async def health():
    return {"status": "ok"}

@app.post("/upload-docs/")
async def upload_docs(files: list[UploadFile] = File(...)):
    file_paths = await save_uploaded_files(files)
    return {"saved_files": file_paths}

@app.post("/process-docs/")
async def process_docs():
    texts = process_documents("data/")
    vectors = generate_embeddings(texts)
    response = send_vectors_to_db(texts, vectors)
    return {"message": "Documents processed", "response": response}