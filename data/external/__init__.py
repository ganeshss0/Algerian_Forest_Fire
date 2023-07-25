import requests as R
import os
from zipfile import ZipFile
import sys
import inspect

DATASET_LINK = 'https://archive.ics.uci.edu/static/public/547/algerian+forest+fires+dataset.zip'
DATASET_ZIP_FILENAME = 'Algerian-Forest-Fires-dataset.zip'
DATASET_ZIP_PATH = os.path.dirname(inspect.getfile(inspect.currentframe()))
DATASET_PATH = os.path.join(os.path.dirname(DATASET_ZIP_PATH), 'raw')
DATASET_FILENAME = 'Algerian_Forest_Fires_dataset.csv'

def download_data(URL: str, ) -> R.Response:
    '''Downloads data from given url.'''
    response = R.get(URL)
    if response.status_code == 200:
        path = os.path.join(DATASET_ZIP_PATH, DATASET_ZIP_FILENAME)
        with open(path, 'wb') as file:
            file.write(response.content)
        return path
    else:
        return

def unzip_data(path_zip: str, path_extract: str):
    '''Unzip archived files.'''
    with ZipFile(path_zip) as zip:
        zip.extractall(path_extract)
    return os.path.join(path_extract, os.listdir(path_extract)[0])
