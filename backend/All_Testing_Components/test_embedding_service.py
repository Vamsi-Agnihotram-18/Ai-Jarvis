from embedding_service import embed_text

def test_embed_text():
    vector = embed_text("What is AI?")
    assert isinstance(vector, list)
    assert len(vector) == 1536