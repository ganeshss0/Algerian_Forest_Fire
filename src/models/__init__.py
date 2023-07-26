import os, sys
from src.logger import logging
from src.exception import CustomException
from src.features import saveObject, evalute_model

import numpy as np
from src.constant import MODEL_PATH
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from dataclasses import dataclass



@dataclass
class ModelTrainer:

    def initiate_model_training(self, train_data: np.array, test_data: np.array) -> str:
        try:
            
            logging.info('Splitting Dependent and Independent Variable Train-Test Data')

            X_train, X_test, y_train, y_test = (
                train_data[:, :-1],
                test_data[:, :-1],
                train_data[:, -1],
                test_data[:, -1]
            )
            
            models = {
                'Random Forest Classifier': RandomForestClassifier(
                    criterion='gini',
                    max_depth=8,
                    min_samples_split=3,
                    n_estimators=200
                ),
                'Suport Vector Classifier': SVC(
                    C=2,
                    degree=2,
                    gamma='scale',
                    kernel='linear'
                ),
                'Decision Tree Classifier': DecisionTreeClassifier(
                    criterion='gini',
                    max_depth=15,
                    min_samples_split=3
                ),
                'ExtraTree Classifier' : ExtraTreesClassifier(
                    criterion='gini',
                    max_depth=8,
                    min_samples_split=2,
                    n_estimators=100

                )
            }
        
            
            model_report = {}
                
            model_report = evalute_model(
                                    X_train,
                                    X_test,
                                    y_train,
                                    y_test,
                                    models
                                        )

            logging.info(f'Model Report: \n{model_report}')
            print('Model Reports:\n', model_report, '\n\n')


            best_model_name = model_report.sort_values(by = 'Recall', ascending = False).iloc[0,0]
            print('Best Model:\n', model_report[model_report.ModelName == best_model_name], '\n\n')
            best_model = models[best_model_name]

            saveObject(
                file_path = MODEL_PATH,
                obj = best_model
            )

        except Exception as e:
            logging.error('FAILED Model Training')
            logging.error(e)
            raise CustomException(e, sys)
