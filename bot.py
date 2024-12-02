from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Your bot's token (replace it with your actual token)
TOKEN = "7029993087:AAFiIEh_4b7Re4sKkyDVS_vReDRypdV_fS8"

# Define the start command handler
async def start(update: Update, context):
    """Handle the /start command."""
    await update.message.reply_text("Hello! I'm your group chatbot. Type 'hello', 'ca', 'website', or 'rug' to test me.")

# Define the message handler for 'hello' and 'hi'
async def greet(update: Update, context):
    """Handle 'hi' or 'hello' messages."""
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f"Hello, {user_name}! How can I help you today?")

# Define the message handler for 'ca'
async def provide_link(update: Update, context):
    """Provide the link when 'ca' is mentioned."""
    await update.message.reply_text("Here is the link you requested: [Insert Your Link Here]")

# Define the message handler for 'rug' or 'rug pull'
async def delete_rug_message(update: Update, context):
    """Delete messages containing 'rug' or 'rug pull'."""
    await update.message.delete()
    await update.message.reply_text("Warning: 'rug' or 'rug pull' is not allowed!")

# Define the message handler for 'website'
async def provide_website_link(update: Update, context):
    """Provide the website link when 'website' is mentioned."""
    await update.message.reply_text("Visit our website here: [Insert Your Website Link Here]")

# Main function to set up the bot
async def main():
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()

    # Add handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, greet))  # For general greetings like "hello"
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^ca$'), provide_link))  # 'ca' message
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^(rug|rug pull)$'), delete_rug_message))  # 'rug' or 'rug pull'
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex('^website$'), provide_website_link))  # 'website'

    # Run the bot with long polling
    await application.run_polling()

# Entry point
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
