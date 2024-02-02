
# YouTube Channel Analysis Project
## Project Overview
This project automates the process of analyzing content from YouTube channels. It involves fetching video URLs from a YouTube channel, downloading them as MP3 files, transcribing the audio using OpenAI's Whisper, cleaning the data through several mini-programs, and finally analyzing the content with the Assistant API.

## Getting Started
### Prerequisites
- Python 3.x
- OpenAI API key
- Google API client
- Internet connection

### Clone the repository to your local machine.

### Install the required Python packages listed in requirements.txt.
pip install -r requirements.txt


### Components
- video_URL_fetcher.py: Fetches video URLs from a specified YouTube channel.
- video_as_mp3_downloader.py: Downloads videos as MP3 files.
- video_transcriber.ipynb: Transcribes the audio from the MP3 files using OpenAI's Whisper.
- util_data_cleaner.py: Cleans the transcribed data.
- util_mergetxt.py: Merges text files.
- util_tokencounter.py: Counts tokens in the text.
- util_charcounter.py: Counts characters in the text.
- assistant_podcast_intel.ipynb and assistant_demo1.ipynb: Analyze the content using the Assistant API.

### Usage
- Set up your API keys and environment variables.
- Run video_URL_fetcher.py to fetch video URLs.
- Use video_as_mp3_downloader.py to download videos as MP3.
- Transcribe the audio files with video_transcriber.ipynb.
- Clean the data using util_data_cleaner.py.
- Merge, count tokens, and characters using the respective utility scripts.
- Analyze the content using the Jupyter notebooks.


### Dependencies
- OpenAI for Whisper and Assistant APIs
- YouTube API




