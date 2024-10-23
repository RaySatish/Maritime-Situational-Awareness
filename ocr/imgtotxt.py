import pytesseract
from PIL import Image
import re

# Perform OCR function
def perform_ocr(image_path):
    img = Image.open(image_path)
    img = img.convert('L')  # Convert image to grayscale

    # Perform OCR and return the result
    custom_config = r'--oem 3 --psm 6'  # Optional Tesseract settings
    return pytesseract.image_to_string(img, config=custom_config)

# Parse the maritime message
def parse_maritime_message(message):
    parsed_data = {}

    # Extract time
    time_match = re.search(r'\b(\d{1,2}[:.]\d{2})\s?(UTC|Z)\b', message)
    if time_match:
        parsed_data['time'] = time_match.group(0)
    print(f"Time match: {time_match.group(0) if time_match else 'No match'}")

    # Extract coordinates
    coord_match = re.search(r'(\d{1,2}°\d{1,2}\'[NS]),\s*(\d{1,3}°\d{1,2}\'[EW])', message)
    if coord_match:
        parsed_data['latitude'] = coord_match.group(1)
        parsed_data['longitude'] = coord_match.group(2)
    print(f"Coordinates match: {coord_match.groups() if coord_match else 'No match'}")

    # Extract speed
    speed_match = re.search(r'\b(\d+)\s?knots\b', message)
    if speed_match:
        parsed_data['speed'] = speed_match.group(1)
    print(f"Speed match: {speed_match.group(0) if speed_match else 'No match'}")

    # Extract direction
    direction_match = re.search(r'towards the (\w+)', message)
    if direction_match:
        parsed_data['direction'] = direction_match.group(1)
    print(f"Direction match: {direction_match.group(1) if direction_match else 'No match'}")

    return parsed_data

# Save data to a text file
def save_to_txt(data, file_name='parsed_message.txt'):
    with open(file_name, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

# Main function
def main():
    # Image path
    image_path = '/Users/satishpremanand/Documents/GitHub/Maritime-Situational-Awareness/Screenshot 2024-10-23 at 1.18.57 PM.png'
    
    # Perform OCR on the image
    ocr_text = perform_ocr(image_path)

    # Save raw OCR output to file for debugging
    with open('ocr_output.txt', 'w') as file:
        file.write(ocr_text)
    print("OCR output saved to ocr_output.txt")

    # Parse the OCR text
    parsed_message = parse_maritime_message(ocr_text)
    
    # Save the parsed data to a text file
    if parsed_message:
        save_to_txt(parsed_message)
        print("Parsed message saved to parsed_message.txt")
    else:
        print("No data was parsed from the OCR output.")

if __name__ == "__main__":
    main()