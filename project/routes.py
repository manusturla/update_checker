from project.check_spanish_appointments import are_changes_in_appointments_page
from flask import Blueprint
from project.telegram_bot import TelegramBot

base_blueprint = Blueprint("base_blueprint", __name__)


@base_blueprint.route("/", methods=["GET"])
def index():
    return health()


@base_blueprint.route("/health", methods=["GET"])
def health():
    return "It's alive!"


@base_blueprint.route("/test_bot", methods=["GET"])
async def test_bot():
    bot = TelegramBot()
    await bot.send_message("Bot is working")
    return "Bot is working"


@base_blueprint.route("/verify", methods=["GET"])
async def check_spanish_appointment():
    has_changed = await are_changes_in_appointments_page()
    return "Changes detected!" if has_changed else "No changes detected"
