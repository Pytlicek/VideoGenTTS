from moviepy.editor import concatenate_videoclips, ColorClip, CompositeVideoClip, AudioFileClip, TextClip
from moviepy.config import change_settings
from helpers import preprocess_text
from gtts import gTTS
import os

change_settings({"IMAGEMAGICK_BINARY": "/usr/local/bin/magick"})

# Parameters
tts_lang = "sk"  # "en" / "sk"
text_file_path = 'prefixes_' + tts_lang + ".txt"
video_output_path = 'output_video.mp4'
background_color = (0, 0, 0)  # Black
text_color = 'white'
font_size = 30
audio_dir = "temp_audio"
os.makedirs(audio_dir, exist_ok=True)

# Read lines from the text file
with open(text_file_path, 'r') as file:
    lines = file.readlines()



# Create a list to hold all clips
clips = []

# Generate a video clip for each line of text
for i, line in enumerate(lines):
    text = line.strip()
    print(f"{i}/{len(lines)} | {text}")

    preprocessed_text = preprocess_text(text)

    # Generate TTS audio for the line of text
    tts = gTTS(text=preprocessed_text, lang=tts_lang)
    audio_file_path = os.path.join(audio_dir, f"audio_{i}.mp3")
    tts.save(audio_file_path)

    # Load the audio file to determine its duration
    audio_clip = AudioFileClip(audio_file_path)
    audio_duration = audio_clip.duration

    # Create a text clip without specifying duration in the constructor
    txt_clip = TextClip(text, fontsize=font_size, color=text_color, size=(640, 480))
    
    # Then, set the duration of the text clip to match the audio duration
    txt_clip = txt_clip.set_duration(audio_duration)
    
    # Create a background clip with the same adjusted duration
    bg_clip = ColorClip(size=(640, 480), color=background_color, duration=audio_duration)
    
    # Overlay the text on the background
    video_clip = CompositeVideoClip([bg_clip, txt_clip.set_pos('center')])
    
    # Set the video clip duration to match the audio clip
    video_clip = video_clip.set_duration(audio_duration)
    
    # Set the audio of the video clip to be the TTS audio
    video_clip = video_clip.set_audio(audio_clip)
    
    # Add the completed video clip to the list
    clips.append(video_clip)


# Concatenate all clips into one video
final_clip = concatenate_videoclips(clips)

# Write the result to a file
final_clip.write_videofile(video_output_path, fps=24, audio_codec='aac')

# Clean up the temporary audio files
for filename in os.listdir(audio_dir):
    os.remove(os.path.join(audio_dir, filename))
os.rmdir(audio_dir)
