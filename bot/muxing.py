import subprocess
import logging
from config import FFMPEG_PATH, MKVMERGE_PATH  # Assuming MKVMERGE_PATH is still in use, if needed
import pymkv  # Import pymkv2

logger = logging.getLogger(__name__)

def mux_video(decrypted_video: str):
    """
    Muxes the decrypted video using ffmpeg and pymkv (instead of mkvmerge).
    """
    try:
        # Define the output file name and MKV output path
        output_file = decrypted_video.replace(".mp4", "_muxed.mkv")

        # Check if FFMPEG_PATH exists (and if not, raise an error)
        if not FFMPEG_PATH:
            logger.error("FFMPEG_PATH is not defined in the config.")
            return None

        # Run ffmpeg to copy the video and audio streams (without re-encoding)
        logger.info(f"Starting ffmpeg muxing process for {decrypted_video}...")

        # FFmpeg command to mux video and audio streams without re-encoding
        cmd = [
            FFMPEG_PATH, '-i', decrypted_video, '-c:v', 'copy', '-c:a', 'copy', '-c:s', 'mov_text', output_file
        ]
        subprocess.run(cmd, check=True)

        # Now, use pymkv2 to mux the video into an MKV file (optional, if you need additional logic here)
        logger.info("Starting Anime mixing process...")

        # Use pymkv2 to add tracks and mux the final file
        mkv = pymkv.MKVFile()  # Create a new MKVFile object
        mkv.add_track(decrypted_video)  # Add the decrypted video track
        mkv.mux(output_file)  # Mux the tracks into the output MKV file

        # Logging success
        logger.info(f"Video muxed successfully: {output_file}")
        return output_file

    except Exception as e:
        # In case of any error, log the error message
        logger.error(f"Error muxing video {decrypted_video}: {str(e)}")
        return None
