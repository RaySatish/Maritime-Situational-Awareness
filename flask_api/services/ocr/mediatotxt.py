import subprocess
import os

def combine_results(output_file):
    with open(output_file, 'w') as outfile:
        # Append results from non-handwritten image OCR
        if os.path.exists('ocr/scripts/non_handwritten_output.txt'):
            with open('ocr/scripts/non_handwritten_output.txt', 'r') as f:
                outfile.write(f.read())

        # Append results from audio transcription
        if os.path.exists('ocr/scripts/audio_output.txt'):
            with open('ocr/scripts/audio_output.txt', 'r') as f:
                outfile.write(f.read())

def main():
    # Execute each of the scripts in the 'scripts' folder
    subprocess.run(["python3", "ocr/scripts/imgtotxt.py"])
    subprocess.run(["python3", "ocr/scripts/audiototxt.py"])

    # Combine the results from all three scripts into one file
    combined_output_file = 'ocr/final_combined_output.txt'
    combine_results(combined_output_file)
    print(f"All results combined and saved to {combined_output_file}")

if __name__ == "__main__":
    main()