from data.external import download_data, unzip_data, DATASET_PATH, DATASET_LINK
from data.processed import read_data, TRAIN_DATASET_PATH, TEST_DATASET_PATH
from src.constant import PREPROCESSOR_PATH, TARGET_COLUMN, DROP_COLUMNS
import pandas as pd
import os, sys
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from src.features import saveObject


class DataIngestion:

    def initiate_data_ingestion(self, url=DATASET_LINK):
        zip_file = download_data(url)
        file_path = unzip_data(zip_file, DATASET_PATH)
        self.data = read_data(file_path, skiprows=1, skip_blank_lines=True)
        self.clean_data()
        self.missing_value()
        self.save_data()

    def clean_data(self):
        '''Remove and clean columns in data.'''
        
        self.data = self.data[self.data.day.str.isnumeric()]
        self.data.columns = self.data.columns.str.strip()
        self.data.drop(columns=DROP_COLUMNS, inplace=True)
        self.data.Classes = self.data.Classes.str.strip()
        self.data.reset_index(inplace=True, drop=True)

    def missing_value(self):
        
        '''Handle missing values in the Classes column'''

        values = []
        for value in self.data[self.data.Classes.isna()].values[0]:
            if type(value) == str:
                values.extend(value.split())
        idx = self.data[self.data.Classes.isna()].index
        self.data.loc[idx[0]] = values
        self.data.Classes = self.data.Classes.map({'fire':1, 'not fire':0})

    def save_data(self):
        # Splitting Data in training and testing
        train_data, test_data = train_test_split(self.data, test_size = 0.3, random_state = 7)
        logging.info('Train Test Splitting')

        # Saving Train Test Data
        train_data.to_csv(TRAIN_DATASET_PATH, index = False, header = True)
        logging.info(f'Train Split Saved at {TRAIN_DATASET_PATH}')

        test_data.to_csv(TEST_DATASET_PATH, index = False, header = True)
        logging.info(f'Test Split Saved at {TEST_DATASET_PATH}')

        logging.info('PASS Data Ingestion')
    



@dataclass
class DataTransform:

    def build_pipeline(self):
        try:
            logging.info('Build Pipeline Initiated')

            
            # Pipeline

            Preprocessor = Pipeline(
                steps = (
                ('imputer', SimpleImputer(strategy = 'median')),
                ('scaling', StandardScaler())
                )
            )

            logging.info('Build Pipeline Successful')

            return Preprocessor

        except Exception as e:
            logging.error('Build Pipeline Failed')
            logging.error(e)
            raise CustomException(e, sys)
    

    def initiate_data_transform(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)


            

            logging.info('Train Test Data Loaded Succesful')
            logging.info(f'Train DataFrame: \n{train_df.head(3).to_string()}')
            logging.info(f'Test DataFrame: \n{test_df.head(3).to_string()}')
            
            

            features_train_data = train_df.drop(columns=TARGET_COLUMN)
            target_train_data = train_df[TARGET_COLUMN]

            features_test_data = test_df.drop(columns=TARGET_COLUMN)
            target_test_data = test_df[TARGET_COLUMN]


            preprocessor = self.build_pipeline()
            logging.info('Pipeline Loaded Successful')


            preprocessor.fit(features_train_data)

            transform_feature_train_data = preprocessor.transform(features_train_data)
            transform_feature_test_data = preprocessor.transform(features_test_data)

            logging.info('Data Transformation Successful')

            train_data = np.c_[transform_feature_train_data, np.array(target_train_data)]
            test_data = np.c_[transform_feature_test_data, np.array(target_test_data)]

            saveObject(
                file_path = PREPROCESSOR_PATH,
                obj = preprocessor
            )

            return (
                train_data,
                test_data,
            )

        except Exception as e:
            logging.error('Data Transform Failed')
            logging.error(e)
            raise CustomException(e, sys)
