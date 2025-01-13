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
    for index, photos in enumerate(response.json(), start=1):
        extension = utils.get_extension(photos['url'])
        save_filename = f'apod_{index}{extension}'
        utils.save_file(photos['url'], './images/', save_filename)

def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    parser = argparse.ArgumentParser(description='Find out number of photos to fetch from NASA')
    parser.add_argument('-c', '--count', default=1, type=int, help='number of photos to fetch')
    args = parser.parse_args()
    fetch_apod_images(api_key, args.count)


if __name__ == '__main__':
    main()