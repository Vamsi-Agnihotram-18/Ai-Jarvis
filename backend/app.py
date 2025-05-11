import os, uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
from config import UPLOAD_FOLDER
from embedding_service import embed_text, upsert_vector, query_similar
from query_service import save_document
from transcribe_service import transcribe
from extract_text import extract_text
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    doc_id = str(uuid.uuid4())
    path = os.path.join(UPLOAD_FOLDER, f"{doc_id}_{file.filename}")
    file.save(path)
    text = extract_text(path)
    save_document(doc_id, text)
    vector = embed_text(text)
    upsert_vector(doc_id, vector, {"filename": file.filename, "text": text})
    return jsonify({"status": "success", "id": doc_id})

@app.route('/query', methods=['POST'])
def query():
    q = request.json.get('query')
    file_id = request.json.get('file_id')
    q_vec = embed_text(q)
    matches = query_similar(q_vec)

    print(f"User query: {q}")
    print(f"File ID: {file_id}")
    print("Matching results:")
    for m in matches:
        print(f" - ID: {m['id']} | Filename: {m['metadata'].get('filename')}")

    # Only use context from the currently uploaded file
    filtered = [m for m in matches if m['id'] == file_id]

    if not filtered:
        return jsonify({"answer": "Sorry, I couldn't match the query to the uploaded document."})

    contexts = [m['metadata'].get('text', '') for m in filtered]
    prompt = f"Answer based only on this document:\n{chr(10).join(contexts)}\n\nQuestion: {q}"

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify({"answer": response.choices[0].message.content})


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    file = request.files['file']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    text = transcribe(path)
    return jsonify({"transcription": text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)