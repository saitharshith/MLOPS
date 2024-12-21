import pandas as pd
import numpy as np
from src.logger.Logging import logging
from src.exceptions.exceptions import custom_exception

import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import path

@dataclass
class DataIngestionConfig:
#configuration for data ingestion
    pass

class DataIngestion:
#data ingestion
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise custom_exception(sys,e)