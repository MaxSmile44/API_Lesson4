from pathlib import Path
import os
import urllib
import requests


def save_file(url, path, filename):
    response = requests.get(url)
    response.raise_for_status()
    Path(path).mkdir(parents=True, exist_ok=True)
    with open(f'{path}/{filename}', 'wb') as file:
        file.write(response.content)

def get_extension(url):
    path_url = urllib.parse.urlsplit(url).path
    filename = os.path.split(path_url)[1]
    clean_filename = urllib.parse.unquote(filename)
    extension = os.path.splitext(clean_filename)[1]
    return extension