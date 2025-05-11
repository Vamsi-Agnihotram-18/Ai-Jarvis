from query_service import save_document
import sqlite3

def test_save_document():
    doc_id = "test123"
    content = "This is a test."
    save_document(doc_id, content)
    
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM documents WHERE id=?", (doc_id,))
    result = cursor.fetchone()
    assert result[0] == content