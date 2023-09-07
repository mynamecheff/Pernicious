from telegram import InputFile, ParseMode, Bot

async def send_telegram_data(token, chat_id, text, file_path, caption):
    try:
        # Create a Telegram bot instance
        bot = Bot(token=token)

        # Send the text message
        await bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)

        # Send the file if specified
        if file_path:
            with open(file_path, 'rb') as file_stream:
                input_file = InputFile(file_stream)
                # Send the file with optional caption
                await bot.send_document(chat_id=chat_id, document=input_file, caption=caption)

        print("Message sent successfully")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    telegram_token = "YOUR_TELEGRAM_BOT_TOKEN"
    chat_id = 123456789  # Replace with the chat ID you want to send the message to
    message_text = "XIT here!"
    file_path = "C:\\path\\to\\file.zip"  # Replace with the path to your file
    caption_text = "Check out this new user data!"

    send_telegram_data(telegram_token, chat_id, message_text, file_path, caption_text)
