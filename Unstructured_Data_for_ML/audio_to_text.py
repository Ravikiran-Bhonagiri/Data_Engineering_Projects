!pip install --upgrade -q accelerate bitsandbytes
!pip install git+https://github.com/huggingface/transformers.git
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
!pip install moviepy

from transformers import pipeline
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_audio_to_text_with_huggingface(audio_file_path):
    """
    Converts an audio file to text using Hugging Face's Whisper model.

    Parameters:
        audio_file_path (str): Path to the audio file to be transcribed.

    Returns:
        str: Transcribed text from the audio file.
    """
    try:
        # Validate file path
        if not os.path.exists(audio_file_path):
            logging.error("The specified audio file does not exist.")
            return "Error: The specified audio file was not found."

        # Load the Hugging Face Whisper model pipeline
        logging.info("Loading Whisper model pipeline from Hugging Face...")
        transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base")

        # Transcribe audio
        logging.info("Transcribing audio...")
        transcription = transcriber(audio_file_path)

        logging.info("Transcription complete.")
        return transcription['text']

    except Exception as e:
        logging.error(f"An error occurred during transcription: {e}")
        return f"Error: An error occurred during transcription; {e}"

if __name__ == "__main__":
    audio_file = "path/to/your/audiofile.wav"

    # Convert audio to text
    if os.path.exists(audio_file):
        transcription = convert_audio_to_text_with_huggingface(audio_file)
        logging.info("Transcribed Text:")
        logging.info(transcription)
    else:
        logging.error("The specified audio file does not exist.")