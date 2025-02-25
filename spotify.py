import subprocess
import os

# Path to your SpotDL executable (replace this with your actual SpotDL path)
SPOTDL_PATH = r"C:\Users\whoami\AppData\Local\Programs\Python\Python313\Scripts\spotdl.exe"

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

# Display banner
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
