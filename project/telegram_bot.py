import telegram
import os

BOT_API_KEY = os.getenv("TELEGRAM_BOT_API_KEY")
CHAT_ID = os.getenv("TELEGRAM_NOTIFICATION_CHAT_ID")


class TelegramBot:
    def __init__(self):
        self.bot = telegram.Bot(BOT_API_KEY)

    async def send_message(self, text):
        async with self.bot:
            await self.bot.send_message(chat_id=CHAT_ID, text=text)
