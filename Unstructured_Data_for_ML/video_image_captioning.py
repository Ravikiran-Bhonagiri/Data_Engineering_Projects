# caption each key frame of video and generate json file

!pip install --upgrade -q accelerate bitsandbytes
!pip install git+https://github.com/huggingface/transformers.git
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
!pip install moviepy


import cv2
import os
import logging
import json
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to("cuda")

def extract_and_caption_key_frames(video_file_path, output_dir, frame_interval=30):
    """
    Extracts key frames from a video file, generates captions, and saves them as a JSON file.
    """
    try:
        # Validate video file existence
        if not os.path.exists(video_file_path):
            logging.error("The specified video file does not exist.")
            return "Error: The specified video file was not found."

        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Open the video file
        logging.info("Opening video file...")
        video_capture = cv2.VideoCapture(video_file_path)
        if not video_capture.isOpened():
            logging.error("Failed to open video file.")
            return "Error: Failed to open video file."

        frame_count = 0
        saved_frames = 0
        captions = {}

        while True:
            success, frame = video_capture.read()
            if not success:
                break

            # Save every nth frame based on frame_interval
            if frame_count % frame_interval == 0 and frame is not None:
                frame_file_path = os.path.abspath(os.path.join(output_dir, f"frame_{frame_count}.jpg"))
                cv2.imwrite(frame_file_path, frame)
                
                # Ensure frame is saved correctly
                if not os.path.exists(frame_file_path):
                    logging.error(f"Failed to save frame: {frame_file_path}")
                    continue
                
                # Generate caption for the saved frame
                raw_image = Image.open(frame_file_path).convert('RGB')
                inputs = processor(raw_image, return_tensors="pt").to("cuda")
                out = model.generate(**inputs)
                caption = processor.decode(out[0], skip_special_tokens=True)

                # Add to captions dictionary
                captions[frame_file_path] = caption

                saved_frames += 1

            frame_count += 1

        video_capture.release()

        # Save captions as JSON
        captions_json_path = os.path.join(output_dir, "captions.json")
        with open(captions_json_path, 'w') as json_file:
            json.dump(captions, json_file, indent=4)

        logging.info(f"Extracted {saved_frames} frames and generated captions, saved to {output_dir}.")
        return f"Extracted {saved_frames} frames and generated captions successfully."

    except Exception as e:
        logging.error(f"An error occurred during frame extraction and captioning: {e}")
        return f"Error: An error occurred during frame extraction and captioning; {e}"


if __name__ == "__main__":
    video_file = "/content/video.mp4"
    output_directory = "/content/images"
    frame_interval = 30
    
    # Extract and caption key frames
    result = extract_and_caption_key_frames(video_file, output_directory, frame_interval)
    logging.info(result)
