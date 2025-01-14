import utils
import requests
from dotenv import load_dotenv
import os


def fetch_epic_images(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, photos in enumerate(response.json(), start=1):
        url = f"https://api.nasa.gov/EPIC/archive/natural/{photos['date'][:10].replace('-', '/')}/png/{photos['image']}.png"
        utils.save_file(url, './images/', f'epic_{index}.png', payload)

def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    fetch_epic_images(api_key)


if __name__ == '__main__':
    main()