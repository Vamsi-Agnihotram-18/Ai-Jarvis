import os
import openai
from pinecone import Pinecone
from config import OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_ENV, PINECONE_INDEX

openai.api_key = OPENAI_API_KEY
pc = Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pc.Index(PINECONE_INDEX)

def embed_text(text: str):
    resp = openai.Embedding.create(
        model='text-embedding-ada-002',
        input=text
    )
    return resp['data'][0]['embedding']

def upsert_vector(id: str, vector: list, metadata: dict):
    index.upsert(vectors=[{"id": id, "values": vector, "metadata": metadata}])

def query_similar(vector: list, top_k=3):
    return index.query(vector=vector, top_k=top_k, include_metadata=True)['matches']