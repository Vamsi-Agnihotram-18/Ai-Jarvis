import os
from PyPDF2 import PdfReader

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    elif ext == '.pdf':
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text

    else:
        return "Unsupported file type"