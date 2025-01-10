import random
from dotenv import load_dotenv
import os
import telegram
import time
import argparse


SECONDS_PER_MINUTE = 60

def get_all_files(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        return filenames

def tg_bot_send(tg_token, path):
    bot = telegram.Bot(token=tg_token)
    updates = bot.get_updates()
    chat_id = updates[0]['my_chat_member']['chat']['id']
    bot.send_photo(chat_id=chat_id, photo=open(path, 'rb'))

def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    directory = './images/'

    parser = argparse.ArgumentParser(description='Determines how many hours a photo will be posted')
    parser.add_argument('-t', '--time', default=4, help='Print number of hours')
    args = parser.parse_args()

    while True:
        photo_list = get_all_files(directory)
        random.shuffle(photo_list)
        for filename in photo_list:
            path = f'{directory}{filename}'
            print(path)
            try:
                tg_bot_send(tg_token, path)
            except Exception:
                continue
            time.sleep(int(args.time) * SECONDS_PER_MINUTE)


if __name__ == '__main__':
    main()