import argparse
import utils
import requests


def fetch_spacex_last_launch(id):
    response = requests.get('https://api.spacexdata.com/v5/launches/')
    response.raise_for_status()
    if not id:
        id = max([i['flight_number'] for i in response.json() if i['links']['flickr']['original']])
    for photos in response.json():
        if photos['flight_number'] == id:
            for index, photo in enumerate(photos['links']['flickr']['original'], start=1):
                extension = utils.get_extension(photo)
                utils.save_file(photo, './images/', f'spacex_{index}{extension}')

def main():
    parser = argparse.ArgumentParser(description='Searches for photos by flight id from NASA')
    parser.add_argument('-i', '--id', default=0, type=int, help='id of the launch you want to fetch')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)


if __name__ == '__main__':
    main()