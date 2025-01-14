import random
from dotenv import load_dotenv
import os
import telegram
import time
import argparse


SECONDS_PER_MINUTE = 60


def tg_bot_send(tg_token, chat_id, path):
    bot = telegram.Bot(token=tg_token)
    with open(path, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    directory = './images/'

    parser = argparse.ArgumentParser(description='Indicate how often photos will be posted in telegram channel')
    parser.add_argument('-t', '--time', default=4, type=int, help='number of hours')
    args = parser.parse_args()

    while True:
        photos = os.listdir(directory)
        random.shuffle(photos)
        for filename in photos:
            path = f'{directory}{filename}'
            try:
                tg_bot_send(tg_token, chat_id, path)
            except telegram.error.NetworkError:
                continue
            time.sleep(args.time * SECONDS_PER_MINUTE)


if __name__ == '__main__':
    main()