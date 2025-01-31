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

def fetch_series(url: str, auth_token: str):
    """
    Fetches series information from Crunchyroll.
    This function should interact with Crunchyroll's API to retrieve metadata about the series.
    (Simplified for example purposes.)
    """
    try:
        logger.info(f"Fetching series information for {url}")
        series_info = {"id": "xyz", "title": "Example Series", "episodes": 12}
        if not series_info:
            raise ValueError("Failed to fetch series information.")
        return series_info
    except Exception as e:
        logger.error(f"Error fetching series info for {url}: {str(e)}")
        return None

def fetch_video(series_info: dict, quality: str):
    """
    Fetches the video from Crunchyroll in the selected quality.
    """
    try:
        logger.info(f"Fetching video for {series_info['title']} in {quality} quality.")
        video_file = f"{series_info['title']}_{quality}.mp4"
        if not os.path.exists(video_file):
            raise FileNotFoundError(f"Video file not found for {series_info['title']} in {quality} quality.")
        return video_file
    except Exception as e:
        logger.error(f"Error fetching video for {series_info['title']} in {quality}: {str(e)}")
        return None

def download_series(url: str, quality: str):
    """
    Downloads a series from Crunchyroll with the given URL and quality.
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

        # Step 3: Fetch series info from Crunchyroll
        series_info = fetch_series(url, auth_token)
        if not series_info:
            raise ValueError("Failed to fetch series information.")

        # Step 4: Fetch the video in the requested quality
        video_file = fetch_video(series_info, quality)
        if not video_file:
            raise ValueError(f"Failed to fetch video in {quality} quality.")

        # Step 5: Handle DRM decryption (if required)
        decrypted_video = decrypt_drm(video_file)
        if not decrypted_video:
            raise ValueError(f"Failed to decrypt DRM video for {series_info['title']}.")

        # Step 6: Muxing the video with ffmpeg (combine video, audio, and subtitles)
        muxed_video = mux_video(decrypted_video)
        if not muxed_video:
            raise ValueError(f"Failed to mux video for {series_info['title']}.")

        logger.info(f"Download completed for {series_info['title']} in {quality} quality.")
        return muxed_video

    except Exception as e:
        logger.error(f"Error during download process for {url}: {str(e)}")
        raise
