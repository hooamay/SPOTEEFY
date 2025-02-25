
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

## 3. Verify Installation
```sh
spotdl --version
```

## 4. Download and Install FFmpeg using SpotDL
```sh
spotdl --download-ffmpeg
```

If it displays a version number, SpotDL is installed successfully.

## 5. Locate SpotDL Path
Open Command Prompt and run:
```sh
where spotdl
```
Copy the output and use it in your script as:
```python
SPOTDL_PATH = r"C:\\Users\\whoami\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\spotdl.exe"
```
