import os
import sys

from src.logger import logging
from src.exception import CustomException

from src.data import DataIngestion
from src.data import DataTransform
from src.models import ModelTrainer
from data.processed import TRAIN_DATASET_PATH, TEST_DATASET_PATH

def start_training(*args, **kwargs):
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion(*args, **kwargs)
    data_transform = DataTransform()
    train_data, test_data = data_transform.initiate_data_transform(TRAIN_DATASET_PATH, TEST_DATASET_PATH)
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_data, test_data)

if __name__ == '__main__':
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    data_transform = DataTransform()
    train_data, test_data, _= data_transform.initiate_data_transform(train_data_path, test_data_path)
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_data, test_data)