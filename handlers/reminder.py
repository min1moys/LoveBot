import random
from config import REMINDER_MESSAGES
from telegram.ext import CallbackContext
from telegram import Update

def send_reminder(context: CallbackContext):
    chat_id = context.job.context
    message = random.choice(REMINDER_MESSAGES)
    context.bot.send_message(chat_id=chat_id, text=message)

def set_reminder(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(send_reminder, interval=3600*6, first=10, context=chat_id)
    update.message.reply_text("Przypominacz nastrojowy został włączony 🌸")