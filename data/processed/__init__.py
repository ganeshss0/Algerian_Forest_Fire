import os
import pandas as pd
import inspect
# from data.external import DATASET_FILENAME
current_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
TRAIN_DATASET_PATH = os.path.join(current_dir, 'Algerian-Forest-Fire-Train.csv')
TEST_DATASET_PATH = os.path.join(current_dir, 'Algerian-Forest-Fire-Test.csv')

def read_data(path:str, **kwargs):
    return pd.read_csv(path, **kwargs)