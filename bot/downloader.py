# bot/downloader.py
import os
import subprocess
import logging
from bot.auth import authenticate_crunchyroll
from bot.decryption import decrypt_drm
from bot.muxing import mux_video
from bot.utils import validate_crunchyroll_url
from config import FFMPEG_PATH, MP4DECRYPT_PATH, MKVMERGE_PATH

logger = logging.getLogger(__name__)

def fetch_series_info(url: str, auth_token: str):
    """
    Fetches information for a specific episode from Crunchyroll using the URL.
    """
    try:
        logger.info(f"Fetching series information for {url}")
        # Example: We would need to extract episode ID and title from the URL here
        # Assuming we have an API or a method to extract the necessary metadata from Crunchyroll.
        episode_id = url.split('/')[4]  # Assuming 'https://www.crunchyroll.com/watch/EPISODE_ID/series_name'
        series_name = url.split('/')[-1]  # Extracting series name from URL
        series_info = {"id": episode_id, "title": series_name}
        
        if not series_info:
            raise ValueError("Failed to fetch series information.")
        
        return series_info
    except Exception as e:
        logger.error(f"Error fetching series info for {url}: {str(e)}")
        return None

def fetch_video(episode_id: str, quality: str):
    """
    Fetches the video for the episode using the episode ID and requested quality.
    """
    try:
        logger.info(f"Fetching video for episode {episode_id} in {quality} quality.")
        video_file = f"episode_{episode_id}_{quality}.mp4"
        if not os.path.exists(video_file):
            raise FileNotFoundError(f"Video file not found for episode {episode_id} in {quality} quality.")
        return video_file
    except Exception as e:
        logger.error(f"Error fetching video for episode {episode_id} in {quality}: {str(e)}")
        return None

def download_series(url: str, quality: str):
    """
    Downloads a specific episode from Crunchyroll with the given URL and quality.
    Handles authentication, fetching video, decryption, and muxing.
    """
    try:
        # Step 1: Validate URL format
        if not validate_crunchyroll_url(url):
            raise ValueError("Invalid Crunchyroll URL format.")
        
        # Step 2: Authenticate and get auth token
        auth_token = authenticate_crunchyroll()
        if not auth_token:
            raise ValueError("Authentication failed.")

        # Step 3: Fetch episode info from Crunchyroll (URL now represents an episode)
        series_info = fetch_series_info(url, auth_token)
        if not series_info:
            raise ValueError("Failed to fetch episode information.")

        episode_id = series_info["id"]
        series_name = series_info["title"]

        # Step 4: Fetch the video in the requested quality
        video_file = fetch_video(episode_id, quality)
        if not video_file:
            raise ValueError(f"Failed to fetch video in {quality} quality.")

        # Step 5: Handle DRM decryption (if required)
        decrypted_video = decrypt_drm(video_file)
        if not decrypted_video:
            raise ValueError(f"Failed to decrypt DRM video for episode {series_name}.")

        # Step 6: Muxing the video with ffmpeg (combine video, audio, and subtitles)
        muxed_video = mux_video(decrypted_video)
        if not muxed_video:
            raise ValueError(f"Failed to mux video for episode {series_name}.")

        logger.info(f"Download completed for {series_name} episode {episode_id} in {quality} quality.")
        return muxed_video

    except Exception as e:
        logger.error(f"Error during download process for {url}: {str(e)}")
        raise