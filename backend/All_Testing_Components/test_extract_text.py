from extract_text import extract_text
import tempfile

def test_txt_extraction():
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as f:
        f.write("This is a sample.")
        f.seek(0)
        path = f.name

    content = extract_text(path)
    assert "sample" in content