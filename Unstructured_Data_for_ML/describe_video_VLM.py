# Describe the video using VLM

from transformers import BitsAndBytesConfig, LlavaNextVideoForConditionalGeneration, LlavaNextVideoProcessor
import torch
from moviepy.editor import VideoFileClip
import os
import av
import numpy as np
import subprocess
import pandas as pd

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

processor = LlavaNextVideoProcessor.from_pretrained("llava-hf/LLaVA-NeXT-Video-7B-hf")
model = LlavaNextVideoForConditionalGeneration.from_pretrained(
    "llava-hf/LLaVA-NeXT-Video-7B-hf",
    quantization_config=quantization_config,
    device_map='auto'
)

# Each "content" is a list of dicts and you can add image/video/text modalities
conversation = [
      {
          "role": "user",
          "content": [
              {"type": "text", "text": "Analyze the video to provide a detailed description. describe that?"},
              {"type": "video"},
              ],
      },
]

prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)


# Function to re-encode the video to fix potential encoding issues
def reencode_video(input_path, output_path):
    try:
        # Re-encode the video using FFmpeg to a standard format (H.264 codec)
        command = [
            'ffmpeg', '-y', '-i', input_path, '-c:v', 'libx264', '-preset', 'fast',
            '-c:a', 'aac', '-b:a', '192k', '-strict', 'experimental', output_path
        ]
        subprocess.run(command, check=True)
        print(f"Video re-encoded successfully to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during video re-encoding: {e}")


def read_video_pyav(container, indices):
    '''
    Decode the video with PyAV decoder.

    Args:
        container (av.container.input.InputContainer): PyAV container.
        indices (List[int]): List of frame indices to decode.

    Returns:
        np.ndarray: np array of decoded frames of shape (num_frames, height, width, 3).
    '''
    frames = []
    container.seek(0)
    start_index = indices[0]
    end_index = indices[-1]
    for i, frame in enumerate(container.decode(video=0)):
        if i > end_index:
            break
        if i >= start_index and i in indices:
            frames.append(frame)
    return np.stack([x.to_ndarray(format="rgb24") for x in frames])



# Initialize an empty dictionary to store the results
results = {}

path_list = ["/content/video.mp4"]
for path in path_list:

    data = {}
    data['video_path'] = path

    new_path = "/content/new_video.avi"
    reencode_video(path, new_path)

    # Download video from the hub
    container = av.open(new_path)

    # Sample uniformly 8 frames from the video
    total_frames = container.streams.video[0].frames
    indices = np.arange(0, total_frames, total_frames / 8).astype(int)
    video = read_video_pyav(container, indices)

    # Call the processor to tokenize the prompt and get pixel_values for videos
    inputs = processor([prompt], videos=[video], padding=True, return_tensors="pt").to(model.device)
    generate_kwargs = {"max_new_tokens": 256, "do_sample": True, "top_p": 0.9}

    # Generate output
    output = model.generate(**inputs, **generate_kwargs)
    generated_text = processor.batch_decode(output, skip_special_tokens=True)[0]

    # Add the generated text to the results dictionary
    results[path] = generated_text

# Dump results to a JSON file
output_json_path = "/content/generated_texts.json"
with open(output_json_path, "w") as json_file:
    json.dump(results, json_file, indent=4)

print(f"Generated texts saved to {output_json_path}")