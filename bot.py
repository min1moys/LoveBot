from telegram.ext import Updater, CommandHandler
from config import TOKEN

from handlers.ilerazem import handle_ilerazem
from handlers.kochamcie import handle_kochamcie
from handlers.reminder import set_reminder

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("ilerazem", handle_ilerazem))
    dp.add_handler(CommandHandler("kochamcie", handle_kochamcie))
    dp.add_handler(CommandHandler("reminder", set_reminder))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()