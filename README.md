# Spotify Downloader Script

This script allows you to download Spotify tracks or albums using **SpotDL**. Simply input the URL of the track or album, and the script will handle the rest.

## Developer

**Developer:** [whoami](https://github.com/whoami)

## Features

- Download individual tracks or entire albums from Spotify.
- Easy to use with a simple command-line interface.
- Prints download status in the terminal.

## Requirements

Before running the script, make sure you have the following installed:

1. **Python 3.x** (you can download it from [here](https://www.python.org/downloads/))
2. **SpotDL** (Spotify Downloader), which can be installed via pip:
    ```bash
    pip install spotdl
    ```

3. **FFmpeg** (required by SpotDL for media conversion)
4. **Pytube** (for YouTube video downloads)
5. **yt-dlp** (alternative download tool for videos)

## Step-by-Step Installation Guide:

### 1. Install Python
- Download Python from [Python's official website](https://www.python.org/downloads/).
- Run the installer and make sure to check the box that says **"Add Python to PATH"** during the installation process.

**Verify the installation:**
```bash
python --version
