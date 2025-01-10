import argparse
import utils
import requests


def fetch_spacex_last_launch(id):
    response = requests.get('https://api.spacexdata.com/v5/launches/')
    response.raise_for_status()
    if not id:
        id = max([i['flight_number'] for i in response.json() if i['links']['flickr']['original']])
    for foto_list in response.json():
        if foto_list['flight_number'] == id:
            for index, foto in enumerate(foto_list['links']['flickr']['original']):
                extension = utils.get_extension(foto)
                utils.save_file(foto, './images/', f'spacex_{index+1}{extension}')

def main():
    parser = argparse.ArgumentParser(description='Searches for photos by flight id')
    parser.add_argument('-i', '--id', default=0, help='Print id of the launch you want to fetch')
    args = parser.parse_args()
    fetch_spacex_last_launch(int(args.id))


if __name__ == '__main__':
    main()