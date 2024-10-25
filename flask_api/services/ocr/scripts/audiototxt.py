import speech_recognition as sr
from pydub import AudioSegment
import os

def transcribe_audio(audio_path):
    if audio_path.lower().endswith('.mp3'):
        sound = AudioSegment.from_mp3(audio_path)
        wav_path = audio_path.replace('.mp3', '.wav')
        sound.export(wav_path, format="wav")
        audio_path = wav_path
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Audio could not be transcribed."
        except sr.RequestError as e:
            return f"Error with the speech recognition service: {e}"

def process_audio_files(folder_path, output_file):
    processed_files = set()
    
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if filename.lower().endswith(('.wav', '.flac', '.mp3')):
                if file_path in processed_files:
                    continue
                
                transcribed_text = transcribe_audio(file_path)
                
                if filename.lower().endswith('.mp3'):
                    processed_files.add(file_path.replace('.mp3', '.wav'))

                outfile.write(f"--- Transcription from {filename} ---\n")
                outfile.write(transcribed_text)
                outfile.write("\n\n")
                print(f"Processed audio: {filename}")

if __name__ == "__main__":
    folder_path = 'datasets/testing'
    output_file = 'ocr/scripts/audio_output.txt' 
    process_audio_files(folder_path, output_file)