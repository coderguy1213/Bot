from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Replace 'YOUR_TOKEN_HERE' with your actual token
TOKEN = '7391872222:AAHnIBqRin21dvPB7PRxaU7qhVkjtObBMpo'

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Your custom auto-reply message
    reply_message = "Hello, I’m currently offline. Please let me know the purpose of your message, and I’ll get back to you as soon as possible."
    await update.message.reply_text(reply_message)

def main():
    application = Application.builder().token(TOKEN).build()

    # Add a message handler for text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    # Start the bot
    application.run_polling()
    print("Bot is running. Press Ctrl+C to stop.")

if __name__ == '__main__':
    main()
