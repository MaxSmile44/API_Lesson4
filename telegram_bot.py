from dotenv import load_dotenv
import os
import telegram


def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token=tg_token)
    bot.send_message(text='Hello World!', chat_id=-1002498810711)


if __name__ == '__main__':
    main()