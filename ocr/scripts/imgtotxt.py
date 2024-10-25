import pytesseract
from PIL import Image, ImageFilter
import os

def perform_ocr(image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    img = img.filter(ImageFilter.SHARPEN)
    img = img.resize((int(img.width * 1.5), int(img.height * 1.5)))

    custom_config = r'--oem 3 --psm 6'
    extracted_text = pytesseract.image_to_string(img, config=custom_config)
    return extracted_text

def process_image_files(folder_path, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                image_path = os.path.join(folder_path, filename)
                extracted_text = perform_ocr(image_path)
                outfile.write(f"--- Text from {filename} ---\n")
                outfile.write(extracted_text)
                outfile.write("\n\n")
                print(f"Processed image: {filename}")
