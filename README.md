### Step-by-Step Installation Guide:

```bash
# 1. Install Python
# Download Python from https://www.python.org/downloads/
# Run the installer and make sure to check the box that says "Add Python to PATH" during the installation process.

# Verify the installation:
python --version

# If it shows a version number, Python is installed correctly.

# 2. Install SpotDL
# Open Command Prompt (Win + R, type `cmd`, and hit Enter).
pip install spotdl

# 3. Download and Install FFmpeg using SpotDL
spotdl --download-ffmpeg

# 4. Install Pytube
pip install pytube

# 5. Install yt-dlp
pip install yt-dlp

# 6. Verify the Installation
spotdl --version

# If it displays a version number, SpotDL is installed successfully.

# 7. Locate the SpotDL Path using Command Prompt
where spotdl

# Copy the output from the command and use it in your script.

# Example Output from Command Prompt:
# C:\Users\whoami\AppData\Local\Programs\Python\Python313\Scripts\spotdl.exe

# In your script, define the SPOTDL_PATH like this:
SPOTDL_PATH = r"C:\Users\whoami\AppData\Local\Programs\Python\Python313\Scripts\spotdl.exe"
