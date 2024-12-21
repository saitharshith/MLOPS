import pandas as pd
import numpy as np
from src.logger.Logging import logging
from src.exceptions.exceptions import custom_exception
import os
import sys
from dataclasses import dataclass
from pathlib import path
from src.utils.utils import save_object,evaluate_model
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
@dataclass
class ModelTrainingConfig:
#configuration for data ingestion
    pass

class ModelTraining:
    def __init__(self):
        pass
    def initiate_model_training(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise custom_exception(sys,e)