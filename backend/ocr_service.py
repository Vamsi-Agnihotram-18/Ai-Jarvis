import os
import easyocr
import pytesseract
from pdf2image import convert_from_path
from config import UPLOAD_FOLDER

def extract_text(file_path):
    text = ''
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        images = convert_from_path(file_path)
        for img in images:
            text += pytesseract.image_to_string(img)
    else:
        reader = easyocr.Reader(['en'], gpu=False)
        text = ' '.join([res[1] for res in reader.readtext(file_path)])
    return text