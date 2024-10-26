import subprocess
import os
from scripts import imgtotxt
from scripts import audiototxt

def combine_results(output_file):
    with open(output_file, 'w') as outfile:
        # Append results from non-handwritten image OCR
        if os.path.exists('flask_api/services/ocr/scripts/image_output.txt'):
            with open('flask_api/services/ocr/scripts/image_output.txt', 'r') as f:
                outfile.write(f.read())

        # Append results from audio transcription
        if os.path.exists('flask_api/services/ocr/scripts/audio_output.txt'):
            with open('flask_api/services/ocr/scripts/audio_output.txt', 'r') as f:
                outfile.write(f.read())

def main():
    folder_path_img = 'flask_api/services/rag/datasets/Input'
    output_file_img = 'flask_api/services/ocr/scripts/image_output.txt'
    output_file_audio = 'flask_api/services/ocr/scripts/audio_output.txt'

    # Execute each of the scripts in the 'scripts' folder
    imgtotxt.process_image_files(folder_path_img, output_file_img)
    audiototxt.process_audio_files(folder_path_img, output_file_audio)

    # Combine the results from both the scripts into one file
    combined_output_file = 'flask_api/services/ocr/final_combined_output.txt'
    combine_results(combined_output_file)
    print(f"All results combined and saved to {combined_output_file}")

if __name__ == "__main__":
    main()