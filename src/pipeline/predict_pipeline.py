import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.features import loadObject
from src.constant import PREPROCESSOR_PATH, MODEL_PATH, COLUMN_NAME
import pandas as pd
import numpy as np
 

@dataclass
class PredictPipeline:

    def predict(self, features, map=False):
        try:

            preprocessor = loadObject(PREPROCESSOR_PATH)
            model = loadObject(MODEL_PATH)

            scaled_data = preprocessor.transform(features)

            prediction = model.predict(scaled_data)
            logging.info('Successful Predition')
            if map:
                return pd.Series(prediction[0]).map({1:'Fire', 0:'Not Fire'}).values
            return prediction
        
        except Exception as e:
            logging.error('FAILED Prediction')
            raise CustomException(e, sys)
        
# @dataclass
# class CustomData:
#     data:list

#     def get_data_as_dataframe(self):
#         try:
        
#             col_names = COLUMN_NAME[:-1]
            
#             data = pd.DataFrame(self.data, columns = col_names)

            

        #     logging.info('DataFrame Gathered')
        #     return data
        # except Exception as e:
        #     logging.error('FAILED DataFrame Gathered')
        #     logging.error(e)
        #     raise CustomException(e, sys)
    
# if __name__ == '__main__':
#     data = CustomData(1, 6, 2012, 29, 57, 18, 0, 65.7, 3.4, 7.6, 1.3, 3.4, 0.5, 'not fire')
#     df = data.get_data_as_dataframe()
#     predict_pipeline = PredictPipeline()
#     res = predict_pipeline.predict(df)
#     print(res)
