from transformers import pipeline
import pytesseract

class MaritimeTextProcessor:
    def __init__(self):
        self.ocr = pytesseract
        self.rag_model = pipeline('text2text-generation', model='maritime-rag')
    
    def process_report(self, image_path):
        text = self.ocr.image_to_string(image_path)
        structured_data = self.rag_model(text)
        return self.extract_vessel_data(structured_data)
