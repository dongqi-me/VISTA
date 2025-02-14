import os
import sys
import moviepy.editor as mp
import openai
import argparse
import logging
from pathlib import Path
import cv2
import easyocr

def setup_logging():
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler("transcription.log"), logging.StreamHandler(sys.stdout)])

def extract_audio(video_path: str, audio_output: str) -> str:
    """Extracts audio from a video file and saves it as a WAV file."""
    try:
        logging.info(f"Processing video: {video_path}")
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(audio_output, codec='pcm_s16le')
        logging.info(f"Audio saved to: {audio_output}")
        return audio_output
    except Exception as e:
        logging.error(f"Error extracting audio: {e}")
        return None

def transcribe_audio(audio_path: str, openai_api_key: str) -> str:
    """Transcribes an audio file using OpenAI's Whisper model."""
    try:
        openai.api_key = openai_api_key
        with open(audio_path, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
            transcript = response["text"]
            logging.info("Transcription complete.")
            return transcript
    except Exception as e:
        logging.error(f"Error in transcription: {e}")
        return ""

def save_transcription(transcript: str, output_path: str):
    """Saves the transcript to a text file."""
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(transcript)
        logging.info(f"Transcription saved to {output_path}")
    except Exception as e:
        logging.error(f"Error saving transcription: {e}")

def extract_ocr_text(video_path: str, output_dir: str) -> str:
    """Extracts on-screen text from video frames using EasyOCR."""
    try:
        reader = easyocr.Reader(["en"])  # Initialize OCR model for English
        video = cv2.VideoCapture(video_path)
        frame_count = 0
        ocr_text = ""
        
        while True:
            ret, frame = video.read()
            if not ret:
                break
            if frame_count % 30 == 0:  # Process every 30th frame
                result = reader.readtext(frame, detail=0)
                ocr_text += " ".join(result) + "\n"
            frame_count += 1
        
        video.release()
        
        ocr_output_path = os.path.join(output_dir, "ocr_text.txt")
        with open(ocr_output_path, "w", encoding="utf-8") as f:
            f.write(ocr_text)
        logging.info(f"OCR text saved to {ocr_output_path}")
        
        return ocr_text
    except Exception as e:
        logging.error(f"Error extracting OCR text: {e}")
        return ""

def process_video(video_path: str, output_dir: str, openai_api_key: str):
    """Extracts audio, transcribes it, extracts OCR text, and saves the results."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    video_filename = Path(video_path).stem
    audio_output = os.path.join(output_dir, f"{video_filename}.wav")
    transcript_output = os.path.join(output_dir, f"{video_filename}.txt")
    
    extracted_audio = extract_audio(video_path, audio_output)
    if extracted_audio:
        transcript = transcribe_audio(extracted_audio, openai_api_key)
        save_transcription(transcript, transcript_output)
    
    extract_ocr_text(video_path, output_dir)
    
    # Cleanup audio file after transcription to save space
    if os.path.exists(audio_output):
        os.remove(audio_output)
        logging.info(f"Deleted temporary audio file: {audio_output}")

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Transcribe video audio and extract on-screen text using OCR")
    parser.add_argument("video", type=str, help="Path to the video file")
    parser.add_argument("--output", type=str, default="transcriptions", help="Output directory")
    parser.add_argument("--api_key", type=str, required=True, help="OpenAI API Key")
    args = parser.parse_args()
    
    process_video(args.video, args.output, args.api_key)

if __name__ == "__main__":
    main()