import random
from config import LOVE_REASONS

def handle_kochamcie(update, context):
    reason = random.choice(LOVE_REASONS)
    update.message.reply_text(f"Kocham cię, {reason}")