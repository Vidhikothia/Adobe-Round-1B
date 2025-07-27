# src/extract_text.py
import fitz
import os

def extract_text_from_pdfs(input_folder):
    extracted = []

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            path = os.path.join(input_folder, filename)
            doc = fitz.open(path)
            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()
                extracted.append({
                    "document": filename,
                    "page": page_num + 1,
                    "text": text
                })

    return extracted
