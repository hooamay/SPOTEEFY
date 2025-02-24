import subprocess

# Replace this with the actual path of spotdl.exe
SPOTDL_PATH = r"PASTE YOUR SPOTDL FILE PATH HERE"

def download_spotify_track(url):
    print(f"Link Detected: {url}")
    print("Downloading...")

    command = [SPOTDL_PATH, "download", url]

    try:
        subprocess.run(command, check=True)
        print("Download Complete!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

print(r"""
███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗    ██████╗ ██╗     
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝    ██╔══██╗██║     
███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝     ██║  ██║██║     
╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝      ██║  ██║██║     
███████║██║     ╚██████╔╝   ██║   ██║██║        ██║       ██████╔╝███████╗
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝       ╚═════╝ ╚══════╝
CREATED BY: whoami
""")

if __name__ == "__main__":
    spotify_url = input("Paste Spotify Track/Album URL: ").strip()
    download_spotify_track(spotify_url)

"""
# Installation Instructions

## 1. Install Python
Download Python from https://www.python.org/downloads/
Run the installer and check the box "Add Python to PATH" during installation.

Verify installation:
```sh
python --version
```
If it shows a version number, Python is installed correctly.

## 2. Install SpotDL
```sh
pip install spotdl
```

## 3. Download and Install FFmpeg using SpotDL
```sh
spotdl --download-ffmpeg
```

## 4. Install Additional Dependencies
```sh
pip install pytube yt-dlp
```

## 5. Verify Installation
```sh
spotdl --version
```
If it displays a version number, SpotDL is installed successfully.

## 6. Locate SpotDL Path
Open Command Prompt and run:
```sh
where spotdl
```
Copy the output and use it in your script as:
```python
SPOTDL_PATH = r"C:\\Users\\whoami\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\spotdl.exe"
```
"""
