import sqlite3

conn = sqlite3.connect('documents.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS documents(
    id TEXT PRIMARY KEY,
    content TEXT
)
""")
conn.commit()

def save_document(doc_id: str, text: str):
    cursor.execute("INSERT OR REPLACE INTO documents (id, content) VALUES (?, ?)", (doc_id, text))
    conn.commit()

def get_document(doc_id: str) -> str:
    cursor.execute("SELECT content FROM documents WHERE id = ?", (doc_id,))
    result = cursor.fetchone()
    return result[0] if result else None