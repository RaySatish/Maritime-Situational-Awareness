# app/services/ocr_service.py
import pytesseract
from PIL import Image

def extract_text_from_image(image_path: str) -> str:
    # OCR processing using Tesseract
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error processing OCR: {str(e)}"
