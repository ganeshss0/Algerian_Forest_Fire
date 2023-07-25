from data.external import download_data, unzip_data, DATASET_PATH, DATASET_LINK
from data.interim import read_data
import pandas as pd

class DataIngestion:
    def initiate_data_ingestion():
        zip_file = download_data(DATASET_LINK)
        file_path = unzip_data(zip_file, DATASET_PATH)
        df = pd.read_csv(file_path)
        df.drop(columns=['year'], inplace=True)
        df = df[df.day.str.isnumeric()]
        # df =