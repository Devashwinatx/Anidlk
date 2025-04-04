import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot.downloader import download_series
from bot.utils import to_small_caps, validate_crunchyroll_url
from config import TELEGRAM_TOKEN  # Import the bot token from config.py

# Setup logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    welcome_message = (
        "Radhe Radhe, this is billa space @Billaspace & you are plugged into Billa crunchyroll bot, "
        "an advanced bot that downloads series and episodes from crunchyroll URL with >quality "
        "e.g., 240p, 360p, 720p, 1080p, hdrip> . Just paste a streaming link of content and desired quality. "
        "Billa will download it for you."
    )
    update.message.reply_text(to_small_caps(welcome_message))

def download(update: Update, context: CallbackContext):
    try:
        # Get URL and quality from the user's message
        message = update.message.text.strip()
        parts = message.split(' ')
        
        if len(parts) < 2:
            update.message.reply_text(to_small_caps("Please provide both the URL and desired quality "
                                                    "(e.g., 'https://crunchyroll.com/series/xyz 720p')."))
            return
        
        url = parts[0]
        selected_quality = parts[1]

        # Validate the URL
        if not validate_crunchyroll_url(url):
            update.message.reply_text(to_small_caps("Invalid URL! Please provide a valid Crunchyroll series link."))
            return

        # Validate the quality
        valid_qualities = ["240p", "360p", "480p", "720p", "1080p", "hdrip"]
        if selected_quality not in valid_qualities:
            update.message.reply_text(to_small_caps("Invalid quality! Please provide a valid quality (e.g., 240p, 720p, 1080p, hdrip)."))
            return

        # Start the download process with the selected quality
        download_series(url, selected_quality)
        update.message.reply_text(to_small_caps(f"Download started for: {url} in {selected_quality} quality."))
    except Exception as e:
        logger.error(f"Error downloading: {e}")
        update.message.reply_text(to_small_caps(f"An error occurred while processing your request: {str(e)}"))

def main():
    # Importing the TELEGRAM_TOKEN from config.py
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("download", download))
    dp.add_handler(CommandHandler("download_series", download))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
