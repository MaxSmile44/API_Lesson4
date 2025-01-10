import argparse
import utils
import requests
from dotenv import load_dotenv
import os


def fetch_apod_images(api_key, count):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'count': count, 'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, foto_list in enumerate(response.json()):
        extension = utils.get_extension(foto_list['url'])
        save_filename = f'apod_{index+1}{extension}'
        utils.save_file(foto_list['url'], './images/', save_filename)

def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    parser = argparse.ArgumentParser(description='Determines how many photos fetch')
    parser.add_argument('-c', '--count', help='Print number of photos to fetch')
    args = parser.parse_args()
    fetch_apod_images(api_key, int(args.count))


if __name__ == '__main__':
    main()