from joblib import load, dump
import os
import sys
from src.logger import logging
from src.exception import CustomException
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score

def saveObject(file_path: str, obj: object) -> None:
    '''Save python object to disk.'''
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok = True)

        dump(obj, file_path)
        logging.info(f'Successful Save Object at {file_path}')

    except Exception as e:
        logging.error(f'FAIL Save Object at {file_path}')
        logging.error(e)
        raise CustomException(e, sys)
    
def loadObject(file_path: str) -> None:
    '''Load python object from disk.'''
    try:
        obj = load(file_path)
        logging.info(f'Successful Read Object at {file_path}')
        return obj
    
    except Exception as e:
        logging.error(f'FAIL Read Object at {file_path}')
        logging.error(e)
        raise CustomException(e, sys)
    

def evalute_model(X_train: np.array, X_test: np.array, y_train: np.array, y_test: np.array, models: dict) -> pd.DataFrame:
    
    '''Return a data from of Accuracy and Recall score of different algorithms.'''
    
    try:
        report = []

        for model in models:
            MODEL = models[model]

            # Model Training
            MODEL.fit(X_train, y_train)

            # Predict Test Data
            y_pred = MODEL.predict(X_test)

            # Evaluation

            report.append([
                model,
                accuracy_score(y_test, y_pred),
                recall_score(y_test, y_pred)
            ])

        return pd.DataFrame(report, columns = ['ModelName', 'Accuracy', 'Recall'])

    except Exception as e:
        logging.error('FAILED to Train Model')
        logging.error(e)
        raise CustomException(e, sys)
