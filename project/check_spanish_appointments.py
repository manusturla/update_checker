import requests
from bs4 import BeautifulSoup
import logging
from project import db
from project.models import Snapshot
from project.telegram_bot import TelegramBot
from config import CHECK_URL as URL
import difflib

log = logging.getLogger("gunicorn.error")


def save_snapshot(text):
    snapshot = Snapshot(text=text)
    db.session.add(snapshot)
    db.session.commit()
    log.info("Snapshot saved in database")


def get_snapshot():
    try:
        response = requests.get("https://www.gooe.com.ar")
        if response.status_code != 200:
            log.warning(
                f"Error obtaining snapshot from appointment page. Request not OK. Status: {response.status_code}"
            )
            return ""
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        log.info("Snapshot obtained from appointment page")
        return text
    except requests.exceptions.RequestException as e:
        log.warning(f"Error obtaining snapshot from appointment page on GET request. \nError: {e}")
        return ""
    except Exception as e:
        log.warning(f"Unkoen error when obtaining snapshot from appointment page. \nError: {e}")
        return ""


def get_difference(last_snapshot, current_snapshot):
    diff = difflib.unified_diff(
        last_snapshot.splitlines(),
        current_snapshot.splitlines(),
        fromfile="last_snapshot",
        tofile="current_snapshot",
    )
    return "\n".join(diff)


def get_message(bot, difference):
    header = bot.prep_text("HAY CAMBIOS:\n------------------------------\n")
    difference_section = bot.prep_code(f"```{difference}```")
    footer = bot.prep_text(f"-------------------------------\nVer: {URL}")

    return header + difference_section + footer


async def are_changes_in_appointments_page():
    bot = TelegramBot()
    log.info("Checking for changes in appointments page")
    current_snapshot = get_snapshot()
    last = Snapshot.query.order_by(Snapshot.id.desc()).first()
    log.info("Last snapshot of time %s", last.created_at if last else None)
    if current_snapshot and ((not last) or last.text != current_snapshot):
        log.info("Changes detected. Sending telegram message")
        difference = get_difference(last.text, current_snapshot)
        log.info(f"Difference detected: {difference}")
        await bot.send_message(get_message(bot, difference))
        save_snapshot(current_snapshot)
        return True
    else:
        log.info("No changes detected")
        return False
