!pip install --upgrade -q accelerate bitsandbytes
!pip install git+https://github.com/huggingface/transformers.git
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
!pip install moviepy

import os
import moviepy.editor as mp
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_audio_from_video(video_file_path, output_audio_path):
    """
    Extracts the audio from a video file and saves it as a separate audio file.

    Parameters:
        video_file_path (str): Path to the video file.
        output_audio_path (str): Path to save the extracted audio file.

    Returns:
        str: Path to the extracted audio file if successful, otherwise an error message.
    """
    try:
        # Validate video file existence
        if not os.path.exists(video_file_path):
            logging.error("The specified video file does not exist.")
            return "Error: The specified video file was not found."

        # Extract audio from video
        logging.info("Extracting audio from video...")
        video = mp.VideoFileClip(video_file_path)
        video.audio.write_audiofile(output_audio_path)

        logging.info(f"Audio successfully extracted to {output_audio_path}.")
        return output_audio_path

    except Exception as e:
        logging.error(f"An error occurred during audio extraction: {e}")
        return f"Error: An error occurred while extracting audio; {e}"
