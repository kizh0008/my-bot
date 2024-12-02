import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Set up logging to get debug information
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Your bot token
TOKEN = '7029993087:AAFiIEh_4b7Re4sKkyDVS_vReDRypdV_fS8'

# Start command to reply when the bot starts
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I'm your friendly bot.")

# Function to respond when someone says "hi" or "hello"
async def greet_user(update: Update, context: CallbackContext) -> None:
    if 'hi' in update.message.text.lower() or 'hello' in update.message.text.lower():
        user_name = update.message.from_user.username
        await update.message.reply_text(f"Hello, {user_name}!")

# Function to send the link when someone says "ca" or "website"
async def send_link(update: Update, context: CallbackContext) -> None:
    if 'ca' in update.message.text.lower() or 'website' in update.message.text.lower():
        await update.message.reply_text("Here's the link: https://yourlink.com")

# Function to delete messages containing "rug" or "rug pull"
async def delete_rug_messages(update: Update, context: CallbackContext) -> None:
    if 'rug' in update.message.text.lower() or 'rug pull' in update.message.text.lower():
        await update.message.delete()

# Main function to start the bot and add handlers
async def main() -> None:
    # Create the Application and pass the bot token
    application = Application.builder().token(TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))

    # Message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, greet_user))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_link))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_rug_messages))

    # Start the bot and keep it running
    await application.run_polling()

if __name__ == '__main__':
    # Start the bot without using asyncio.run()
    import sys
    from telegram.ext import Application
    try:
        application = Application.builder().token(TOKEN).build()
        application.run_polling()
    except KeyboardInterrupt:
        sys.exit(0)

