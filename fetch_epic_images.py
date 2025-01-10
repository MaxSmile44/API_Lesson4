import utils
import requests
from dotenv import load_dotenv
import os


def fetch_epic_foto(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, foto_list in enumerate(response.json()):
        url = f"https://api.nasa.gov/EPIC/archive/natural/{foto_list['date'][:10].replace('-', '/')}/png/{foto_list['image']}.png"
        foto = requests.get(url, params=payload)
        utils.save_file(foto.url, './images/', f'epic_{index+1}.png')

def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    fetch_epic_foto(api_key)


if __name__ == '__main__':
    main()