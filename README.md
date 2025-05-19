# upload-api

# Upload API - Document Processor

API FastAPI para subir documentos, procesarlos y generar vectores con embeddings.

## Requisitos

- Python 3.9+
- Dependencias en `requirements.txt`
- Docker (opcional)

## Instalación local

```bash
git clone <repo-upload-api>
cd upload-api
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
