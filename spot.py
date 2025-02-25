import subprocess
import os
import time
import re

#Developed by: whoami

# Path to your SpotDL executable (replace this with your actual SpotDL path)
SPOTDL_PATH = r"C:\Users\sawnd\AppData\Local\Programs\Python\Python313\Scripts\spotdl.exe"

def download_spotify_track(url):
    print(f"Link Detected: {url}")
    print("Downloading...")

    # Ensure the SpotDL path is correct
    if not os.path.exists(SPOTDL_PATH):
        print("Error: SpotDL not found at the specified path.")
        return

    # Prepare the command to run SpotDL
    command = [SPOTDL_PATH, "download", url]

    try:
        # Run the command and check for errors
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
    """Clear the screen and reprint the banner."""
    os.system('cls' if os.name == 'nt' else 'clear')  # This works for Windows (nt) and UNIX-like systems
    print(r"""
███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗    ██████╗ ██╗     
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝    ██╔══██╗██║     
███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝     ██║  ██║██║     
╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝      ██║  ██║██║     
███████║██║     ╚██████╔╝   ██║   ██║██║        ██║       ██████╔╝███████╗
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝       ╚═════╝ ╚══════╝
CREATED BY: whoami
""")

def validate_url(url):
    """Check if the provided URL is a valid Spotify or YouTube Music URL."""
    spotify_pattern = r"^(https:\/\/(www\.)?spotify\.com\/)(track|album|playlist)\/[a-zA-Z0-9]+$"
    youtube_pattern = r"^(https:\/\/music\.youtube\.com\/)(watch\?v=[a-zA-Z0-9_-]+)$"
    
    if re.match(spotify_pattern, url) or re.match(youtube_pattern, url):
        return True
    else:
        return False

# Display banner and ask for URL in a loop
if __name__ == "__main__":
    while True:
        clear_screen()  # Clear the screen and display the banner
        spotify_url = input("Paste Spotify Track/Album URL (or type 'exit' to quit): ").strip()

        if spotify_url.lower() == 'exit':
            print("Exiting program.")
            break  # Exit the loop if user types 'exit'

        if not validate_url(spotify_url):
            print("Invalid URL entered. Please provide a valid Spotify or YouTube Music URL.")
            time.sleep(1)  # Wait a little before asking for input again
            continue  # Skip the download attempt if the URL is invalid

        download_spotify_track(spotify_url)  # Download the track
        time.sleep(2)  # Add a slight delay before clearing the screen again
