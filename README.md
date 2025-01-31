# Billa Crunchyroll Bot

A Telegram bot to download Crunchyroll series and episodes.

Co-powered By - BILLA SPACE & FN NETWORK 

SUPPORT CHANNEL - @BillaSpace & @Heavenwaala
SUPPORT GROUP CHAT - @BillaCore & @fn_network_back

## Features:
- Download videos from Crunchyroll in various qualities (240p, 360p, 720p, 1080p, HDRip)
- Decrypt DRM protected content
- Mux video, audio, and subtitles

## Setup:
1. Clone the repo Locally To VPS: `git clone https://github.com/billaCrunchyrollBot.git`
2. Install required dependencies: `pip install -r requirements.txt`
3. Configure the `config.py` or  `.env` file with your credentials.

(a) For Config.py Vars -:

# Telegram bot token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_BOT_TOKEN")

# Crunchyroll login credentials
CRUNCHYROLL_USERNAME = os.getenv("CRUNCHYROLL_USERNAME", "your_crunchyroll_username")
CRUNCHYROLL_PASSWORD = os.getenv("CRUNCHYROLL_PASSWORD", "your_crunchyroll_password")

# User-Agent for Crunchyroll API (optional)
CRUNCHYROLL_USER_AGENT = os.getenv("CRUNCHYROLL_USER_AGENT", "CrunchyrollBot/1.0")

# Path to DRM decryption tools
MP4DECRYPT_PATH = os.getenv("MP4DECRYPT_PATH", "/path/to/mp4decrypt")
FFMPEG_PATH = os.getenv("FFMPEG_PATH", "/usr/bin/ffmpeg")
MKVMERGE_PATH = os.getenv("MKVMERGE_PATH", "/usr/bin/mkvmerge")

(b) If .env is USED its Vars SHOULD be like that :-

TELEGRAM_TOKEN=your_bot_token
CRUNCHYROLL_USERNAME=your_crunchyroll_username
CRUNCHYROLL_PASSWORD=your_crunchyroll_password
CRUNCHYROLL_USER_AGENT=CrunchyrollBot/1.0
MP4DECRYPT_PATH=/path/to/mp4decrypt
FFMPEG_PATH=/usr/bin/ffmpeg
MKVMERGE_PATH=/usr/bin/mkvmerge


4. Run the bot: `python3 main.py`



#Here’s the list of commands available for the Advanced Billa Crunchyroll Bot :-

List of Commands:
`/start`

Description: Starts the bot and provides a welcome message with a brief description of how the bot works.
Usage: `/start`
Response:
Radhe Radhe, This Is Billa Space & you're plugged into Billa Crunchyroll Bot.
Paste a streaming link & quality (e.g., 720p).
`/download` <url> <quality>

Description: Downloads a series or episode from Crunchyroll based on the provided URL and quality. Quality can be specified as 240p, 360p, 720p, 1080p, HDRip, etc.
Usage: `/download` <url> <quality>
Example:
`/download` https://www.crunchyroll.com/example_series 720p
Response:
Download started for https://www.crunchyroll.com/example_series in 720p quality!
`/help` (optional)

Description: Provides instructions and usage information about the bot.
Usage: `/help`
Response:
Welcome to Billa Crunchyroll Bot!

Commands:
- `/start`: Welcome message and bot info
- /download <url> <quality>: Download series or episode from Crunchyroll
How to Use:
Start the Bot:
Type `/start` in your Telegram chat with the bot to receive a welcome message.
Download Content:
To download a series or episode, simply paste the Crunchyroll streaming URL along with the desired quality. For example:
bash
Copy
`/download` https://www.crunchyroll.com/example_series 720p
The bot will start fetching and processing the content for download.
Additional Notes:
Quality Options: The bot supports different video quality options, including:

`240p`

`360p`

`720p`

`1080p`

`HDRip`
Error Handling: If an invalid URL or quality option is provided, the bot will respond with an error message and guide the user accordingly.


Feel Free To Contact If have issues over it & if you are happy with my work consider to Donate Me :- {TELEGRAM}
@ifeelraam `THE DEVLOPER OF THIS BOT AND SOURCE CODE`

# I WOULD like to give special thanks to the cruncpyroll devs and its repected team and owners for their Api
(Already open source In Github)

if issues persists related to this create issues in branch Or Wannaa To Contribute in this Repo ?
pull issues or pull requests to merge.

`Good to Go See You Ahead !!`



