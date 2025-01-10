from dotenv import load_dotenv
import os
import telegram


def tg_bot_send(tg_token, chat_id, path):
    bot = telegram.Bot(token=tg_token)
    bot.send_photo(chat_id=chat_id, photo=open(path, 'rb'))

def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    chat_id = -1002498810711
    path = './images/spacex_7.jpg'
    tg_bot_send(tg_token, chat_id, path)


if __name__ == '__main__':
    main()