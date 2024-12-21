import pandas as pd
import numpy as np
from src.logger.Logging import logging
from src.exceptions.exceptions import custom_exception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
#configuration for data ingestion
    raw_data_path:str=os.path.join("artifacts","raw_data.csv")
    train_data_path:str=os.path.join("artifacts","train_data.csv")
    test_data_path:str=os.path.join("artifacts","test_data.csv")
    

class DataIngestion:
#data ingestion
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion")
        try:
            data=pd.read_csv("https://raw.githubusercontent.com/saitharshith/gemstone-dataset/refs/heads/main/train_data.csv")
            logging.info('reading a dataframe')
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(" i have saved the raw dataset in artifact folder")
            
            logging.info("here i have performed train test split")
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train test split completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("data ingestion part completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


            
            
        except Exception as e:
            logging.info()
            raise custom_exception(sys,e)
        
if __name__=='__main__':
    data_ingestion=DataIngestion()
    data_ingestion.initiate_data_ingestion()
    