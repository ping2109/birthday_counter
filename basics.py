import os
import datetime
import telegram
from telegram import Sticker, PhotoSize, TelegramError, StickerSet, MaskPosition, Bot
from telegram.error import BadRequest

bot_token = os.getenv('TOKEN')
channel = os.getenv('TG_ID')

def get_user_birthday():
    year = os.getenv('YEAR')
    month = os.getenv('MONTH')
    day = os.getenv('DATE')
    birthday = datetime.datetime(year, month, day)
    return birthday

def compute_birthday_difference(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    difference = date1 - date2
    days = int(difference.total_seconds()/60/60/24)
    return days

def print_bday_info(days):
    if days < 0:
        print('Your birthday is in {} days.'.format(-days))
    elif days > 0:
        print('Your birthday was {} days ago. Hope it was great!'.format(days))
    else:
        print('Happy Birthday!')

def main():
    bday = get_user_birthday()
    now = datetime.datetime.now()
    days = compute_birthday_difference(bday, now)
    print_bday_info(days)
    
def send_tg_message():
    try:
        telegram_notify = telegram.Bot(bot_token)
        message = print_bday_info(days)

        telegram_notify.send_message(chat_id=channel, text=message, disable_web_page_preview=True,
                                parse_mode='Markdown')
    except Exception as ex:
        print(ex)

main()
send_tg_message()
