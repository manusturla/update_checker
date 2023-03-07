import requests
from bs4 import BeautifulSoup
import logging
from project import db
from project.models import Snapshot
from project.telegram_bot import TelegramBot
from config import CHECK_URL as URL

log = logging.getLogger("gunicorn.error")


def save_snapshot(text):
    snapshot = Snapshot(text=text)
    db.session.add(snapshot)
    db.session.commit()
    log.info("Snapshot saved in database")


def get_snapshot():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    log.info("Snapshot obtained from appointment page")
    return text


async def are_changes_in_appointments_page():
    bot = TelegramBot()
    log.info("Checking for changes in appointments page")
    current_snapshot = get_snapshot()
    last = Snapshot.query.order_by(Snapshot.id.desc()).first()
    log.info("Last snapshot of time %s", last.created_at if last else None)
    if not last or last.text != current_snapshot:
        log.info("Changes detected. Sending telegram message")
        await bot.send_message(f"HAY CAMBIOS. Ver: {URL}")
        save_snapshot(current_snapshot)
        return True
    else:
        log.info("No changes detected")
        return False
