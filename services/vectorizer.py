from sentence_transformers import SentenceTransformer
import requests

def generate_embeddings(docs):
    texts = [doc.page_content for doc in docs]
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Puedes usar otros como paraphrase-MiniLM
    vectors = model.encode(texts).tolist()
    return {"texts": texts, "embeddings": vectors}

def send_vectors_to_db(texts, embeddings):
    ids = [f"vec_{i}" for i in range(len(texts))]  # IDs únicos
    metadatas = [{"text": text} for text in texts]  # O cualquier metadato que desees

    payload = {
        "ids": ids,
        "embeddings": embeddings,
        "metadatas": metadatas
    }

    response = requests.post(
        "http://vector-db-api:8001/save-vectors/",
        json=payload
    )
    return response.json()

