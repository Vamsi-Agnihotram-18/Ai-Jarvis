import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")
AZURE_COG_ENDPOINT = os.getenv("AZURE_COGNITIVE_ENDPOINT")
AZURE_COG_KEY = os.getenv("AZURE_COGNITIVE_KEY")
UPLOAD_FOLDER = 'uploads'