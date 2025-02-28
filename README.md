
# Installation Instructions

## 1. Install Python
Download Python from https://www.python.org/downloads/
Run the installer and check the box "Add Python to PATH" during installation.

Verify installation:
```sh
python --version
```
If it shows a version number, Python is installed correctly.

## 2. Install the requirements.txt
```sh
pip install -r requirements.txt
```

## 3. Download and Install FFmpeg using SpotDL
```sh
spotdl --download-ffmpeg
```

## 4. Verify Installation
```sh
spotdl --version
```

If it displays a version number, SpotDL is installed successfully.

## 5. Locate SpotDL Path
Open Command Prompt and run:
```sh
where spotdl
```

Copy the output and use it in your script as:
```python
SPOTDL_PATH = r"C:\Users\whoami\AppData\Local\Programs\Python\Python313\Scripts\spotdl.exe"
```

## Full Script Code

```python
import subprocess
import os
import time
import re

# DEVELOPED BY: whoami

SPOTDL_PATH = r"C:\Users\whoami\AppData\Local\Programs\Python\Python313\Scripts\spotdl.exe"

def download_spotify_track(url):
    print(f"Link Detected: {url}")
    print("Downloading...")

    if not os.path.exists(SPOTDL_PATH):
        print("Error: SpotDL not found at the specified path.")
        return

    # Add --bitrate 320k flag to the command
    command = [SPOTDL_PATH, "--bitrate", "320k", "download", url]

    try:
        subprocess.run(command, check=True)
        print("Download Complete!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Possible cause: This track might not be available.")
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        print("Make sure SpotDL is properly installed and the path is correct.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
███████╗██████╗  ██████╗ ████████╗███████╗███████╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝██╔════╝╚██╗ ██╔╝
███████╗██████╔╝██║   ██║   ██║   █████╗  █████╗  █████╗   ╚████╔╝ 
╚════██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══╝  ██╔══╝    ╚██╔╝  
███████║██║     ╚██████╔╝   ██║   ███████╗███████╗██║        ██║   
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚═╝        ╚═╝
DEVELOPED BY: whoami
""")

def validate_url(url):
    spotify_pattern = r"^https:\/\/open\.spotify\.com\/(track|album|playlist)\/[a-zA-Z0-9]+(\?[\w&=]*)?$"
    
    if re.match(spotify_pattern, url):
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        clear_screen()
        spotify_url = input("Paste Spotify Track/Album URL: ").strip()

        if spotify_url.lower() == 'exit':
            print("Exiting program.")
            break

        if not validate_url(spotify_url):
            print("Invalid URL entered. Please provide a valid Spotify URL.")
            time.sleep(1)
            continue

        download_spotify_track(spotify_url)
        time.sleep(2)
