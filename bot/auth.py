# bot/auth.py

import requests
from config import CRUNCHYROLL_USERNAME, CRUNCHYROLL_PASSWORD, CRUNCHYROLL_USER_AGENT

def authenticate_crunchyroll():
    """
    Authenticates the user with Crunchyroll and returns the auth token.
    """
    try:
        login_url = "https://sso.crunchyroll.com/login"
        headers = {"User-Agent": CRUNCHYROLL_USER_AGENT}
        data = {
            "username": CRUNCHYROLL_USERNAME,
            "password": CRUNCHYROLL_PASSWORD
        }

        response = requests.post(login_url, data=data, headers=headers)
        response.raise_for_status()

        auth_token = response.json().get("auth_token")
        if not auth_token:
            raise ValueError("Authentication failed. No auth_token received.")
        
        return auth_token
    except Exception as e:
        raise ValueError(f"Error authenticating with Crunchyroll: {str(e)}")
