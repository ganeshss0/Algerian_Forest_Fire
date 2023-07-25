import logging, os
from datetime import datetime
import pandas as pd

##########################################
###########    Logging File    ###########
##########################################



LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(), 'logs')
LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)

os.makedirs(
    name=LOGS_PATH, 
    exist_ok = True
    )




logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format='[%(asctime)s]|%(levelname)s|%(lineno)d|%(filename)s|%(funcName)s()|%(message)s',
    level=logging.INFO
)

def get_log_dataframe(file_path: str) -> pd.DataFrame:

    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("|"))

    log_df = pd.DataFrame(data)
    log_df.columns = ["Time stamp","Log Level","line number","file name","function name","message"]
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]


