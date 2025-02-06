import requests
from config import CRUNCHYROLL_PASSWORD, CRUNCHYROLL_USERNAME, CRUNCHYROLL_USER_AGENT

# Constants
PUBLIC_TOKEN = "d2piMV90YThta3Y3X2t4aHF6djc6MnlSWlg0Y0psX28yMzRqa2FNaXRTbXNLUVlGaUpQXzU="
APP_VERSION = "3.59.0"
DEVICE_NAME = "RMX2170"
DEVICE_TYPE = "realme RMX2170"
DEVICE_ID = str(uuid4())

def get_api_headers(headers: Optional[Dict] = None) -> Dict:
    """Generates and returns the API headers for Crunchyroll requests."""
    return {
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"Crunchyroll/{APP_VERSION} Android/13 okhttp/4.12.0"
    } | (headers or {})

def authenticate_crunchyroll():
    """
    Authenticates the user with Crunchyroll using the email or phone number 
    (passed as `CRUNCHYROLL_USERNAME`) and returns the auth token.
    """
    try:
        login_url = "https://sso.crunchyroll.com/login"
        
        # Custom headers for authentication
        headers = get_api_headers({
            "User-Agent": CRUNCHYROLL_USER_AGENT,
        })
        
        # Authentication data: The username can be email or phone number.
        data = {
            "login": CRUNCHYROLL_USERNAME,  # Email or phone number here
            "password": CRUNCHYROLL_PASSWORD
        }

        # Sending the login request
        response = requests.post(login_url, data=data, headers=headers)
        
        # Check for successful response
        response.raise_for_status()

        # Log the raw response content for debugging
        print("Response Text:", response.text)  # For debugging purposes
        
        # Extract auth_token from the response JSON (if it exists)
        try:
            auth_token = response.json().get("auth_token")
            if not auth_token:
                raise ValueError("Authentication failed. No auth_token received.")
        except ValueError:
            raise ValueError("Error: Response is not JSON or does not contain the expected data.")
        
        return auth_token
    except Exception as e:
        raise ValueError(f"Error authenticating with Crunchyroll: {str(e)}")