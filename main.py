from fastapi import FastAPI, UploadFile, File
from services.file_utils import save_uploaded_files
from services.doc_processing import process_documents
from services.vectorizer import generate_embeddings, send_vectors_to_db

import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

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
    docs = process_documents("data/")
    result = generate_embeddings(docs)
    logger.info("Generated Embeddings: %s", result["embeddings"])
    logger.info("Texts: %s", result["texts"])

    payload = {
        "texts": result["texts"],
        "embeddings": result["embeddings"]
    }
    logger.info("Sending payload to vector-db: %s", payload)

    response = send_vectors_to_db(result["texts"], result["embeddings"])
    return {"message": "Documents processed", "response": response}
