from datetime import date
from config import START_DATE

def handle_ilerazem(update, context):
    today = date.today()
    start = date(*START_DATE)
    days = (today - start).days
    update.message.reply_text(f"Jesteśmy razem już {days} dni ❤️")