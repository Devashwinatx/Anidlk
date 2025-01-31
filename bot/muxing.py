# bot/muxing.py

import subprocess
import logging
from config import FFMPEG_PATH, MKVMERGE_PATH

logger = logging.getLogger(__name__)

def mux_video(decrypted_video: str):
    """
    Muxes the decrypted video using ffmpeg and mkvmerge (you may need to implement more muxing logic).
    """
    try:
        output_file = decrypted_video.replace(".mp4", "_muxed.mkv")

        # Example ffmpeg muxing (you can modify this depending on your needs)
        logger.info(f"Starting muxing process for {decrypted_video}...")

        cmd = [
            FFMPEG_PATH, '-i', decrypted_video, '-c:v', 'copy', '-c:a', 'copy', '-c:s', 'mov_text', output_file
        ]
        subprocess.run(cmd, check=True)

        # Optionally, you can run mkvmerge for additional muxing
        cmd_mkvmerge = [MKVMERGE_PATH, '-o', output_file, decrypted_video]
        subprocess.run(cmd_mkvmerge, check=True)

        logger.info(f"Video muxed successfully: {output_file}")
        return output_file
    except Exception as e:
        logger.error(f"Error muxing video {decrypted_video}: {str(e)}")
        return None
