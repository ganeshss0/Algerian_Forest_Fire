import os
import pandas as pd
import inspect
from data.external import DATASET_FILENAME
current_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
filepath = os.path.join(current_dir, DATASET_FILENAME)

def read_data(path=filepath):
    return pd.read_csv(path)