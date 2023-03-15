import telegram
import os

BOT_API_KEY = os.getenv("TELEGRAM_BOT_API_KEY")
CHAT_ID = os.getenv("TELEGRAM_NOTIFICATION_CHAT_ID")


class TelegramBot:
    def __init__(self):
        self.bot = telegram.Bot(BOT_API_KEY)

    async def send_message(self, text):
        async with self.bot:
            await self.bot.send_message(
                chat_id=CHAT_ID,
                text=text,
                parse_mode=telegram.constants.ParseMode.MARKDOWN_V2,
            )

    def prep_code(self, code):
        CODEBLOCK_ENDS = "```"
        CODELINE_ENDS = "`"
        if code[:3] == CODEBLOCK_ENDS and code[-3:] == CODEBLOCK_ENDS:
            code = code[3:-3]
            surrounding = CODEBLOCK_ENDS
        elif code[0] == CODELINE_ENDS and code[-1] == CODELINE_ENDS:
            code = code[1:-1]
            surrounding = CODELINE_ENDS
        else:
            surrounding = ""
        escaped_text = self.prep_text(code)
        escaped_code_block = surrounding + escaped_text + surrounding
        return escaped_code_block

    def prep_text(self, text):
        return telegram.helpers.escape_markdown(text, version=2)
