# Video Generation Script with Text-to-Speech

This script generates a video from a list of text phrases, each accompanied by synthesized speech using Google's Text-to-Speech (gTTS) API. Each line of text from an input file is displayed as a separate video clip with a corresponding audio track that reads the text aloud.

## Features

- Converts a list of text phrases into spoken audio using gTTS.
- Generates a video clip for each phrase with custom background and text color.
- Combines all video clips into a single output video file.
- Adjusts the duration of each video clip to match the length of the audio.
- Preprocesses text to adjust the pronunciation for TTS.

## Prerequisites

Before running the script, you need to have Python installed on your system. The script has been tested with Python 3.10. Additionally, you will need the following packages:

- moviepy
- gTTS

You also need to have ImageMagick installed, which is used by MoviePy for text rendering.

## Installation

### System Requirements

Install ImageMagick using Homebrew:

```sh
brew install imagemagick
```

### Python Dependencies

Install the required Python packages using `pip`. It's recommended to use a virtual environment.

Create a virtual environment (optional):

```sh
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```sh
pip install moviepy gTTS
```

## Usage

To run the script, use the following command:

```sh
python movie_gen.py
```

The script will process each line in the input text file and generate a video clip for it. After processing all lines, it will concatenate them into a single video file.

## Configuration

You can configure the script parameters at the beginning of the script:

- `tts_lang`: Set the language code for gTTS (e.g., "en" for English, "sk" for Slovak).
- `text_file_path`: Path to the input text file containing the phrases to convert.
- `video_output_path`: Path where the output video file will be saved.
- `background_color`: RGB color tuple for the video background (default is black).
- `text_color`: Color name or RGB tuple for the text color (default is white).
- `font_size`: Size of the text font.
- `audio_dir`: Temporary directory to store the generated audio files.

## Text Preprocessing

The `preprocess_text` function can be modified to change the pronunciation of certain phrases or abbreviations for the TTS.

## Cleanup

After the video is generated, the script will automatically remove the temporary audio files created during the process.

## Disclaimer

The performance and accuracy of the TTS conversion may vary based on the input text and the selected language. The script may need to be adjusted for complex pronunciation cases.
