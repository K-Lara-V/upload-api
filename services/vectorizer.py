from langchain.embeddings import OpenAIEmbeddings
import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-your-api-key")

def generate_embeddings(docs):
    texts = [doc.page_content for doc in docs]
    embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectors = embeddings_model.embed_documents(texts)
    return {"texts": texts, "embeddings": vectors}

def send_vectors_to_db(texts, embeddings):
    response = requests.post(
        "http://vector-db-api:8001/save-vectors/",
        json={"texts": texts, "embeddings": embeddings}
    )
    return response.json()