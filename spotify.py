import subprocess

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
