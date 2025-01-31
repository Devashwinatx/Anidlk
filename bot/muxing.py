# bot/muxing.py

import subprocess

def mux_video(decrypted_video: str) -> None:
    """Mux the decrypted video file (e.g., combine video, audio, and subtitles)."""
    try:
        output_file = f"{decrypted_video}_muxed.mkv"
        subprocess.run(["mkvmerge", "-o", output_file, decrypted_video], check=True)
        print(f"Video muxing completed: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during muxing: {str(e)}")
        raise
