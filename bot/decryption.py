# bot/decryption.py

import subprocess
import logging
from config import MP4DECRYPT_PATH

logger = logging.getLogger(__name__)

def decrypt_drm(video_file: str):
    """
    Decrypts DRM-protected video using mp4decrypt.
    """
    try:
        decrypted_file = video_file.replace(".mp4", "_decrypted.mp4")

        # Run mp4decrypt to decrypt the video
        cmd = [MP4DECRYPT_PATH, video_file, decrypted_file]
        subprocess.run(cmd, check=True)

        logger.info(f"DRM decryption successful for {video_file}")
        return decrypted_file
    except Exception as e:
        logger.error(f"Error decrypting video {video_file}: {str(e)}")
        return None
