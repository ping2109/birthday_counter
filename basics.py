import os
import time
import datetime
import telegram
from telegram import Sticker, PhotoSize, TelegramError, StickerSet, MaskPosition, Bot
from telegram.error import BadRequest

username = os.getenv('USERNAME')
bot_token = os.getenv('TOKEN')
channel = os.getenv('TG_ID')

def get_user_birthday():
    year = int(os.getenv('YEAR'))
    month = int(os.getenv('MONTH'))
    day = int(os.getenv('DATE'))
    birthday = datetime.datetime(year, month, day)
    return birthday

def compute_birthday_difference(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    difference = date1 - date2
    days = int(difference.total_seconds()/60/60/24)
    return days

def main():
    bday = get_user_birthday()
    now = datetime.datetime.now()
    days = compute_birthday_difference(bday, now)
    days2 = int(365)
    while days < 0:
        telegram_notify = telegram.Bot(bot_token)
        message = (f"""{username}'s birthday is in {format(-days)} days.""")

        telegram_notify.send_message(chat_id=channel, text=message, disable_web_page_preview=True,
                                parse_mode='Markdown')
        time.sleep(3600)
    if days > 0:
        telegram_notify = telegram.Bot(bot_token)
        message = (f"""{username}'s birthday is in {days2 - days} days.""")

        telegram_notify.send_message(chat_id=channel, text=message, disable_web_page_preview=True,
                                parse_mode='Markdown')
        time.sleep(3600)
    else:
        telegram_notify = telegram.Bot(bot_token)
        message = (f"""*Happy birthday to {username}!\nMake a wish 🥳\n\nHis/Her date of birth: {bday}*""")

        telegram_notify.send_message(chat_id=channel, text=message, disable_web_page_preview=True,
                                parse_mode='Markdown')
        time.sleep(3600)

        
main()
