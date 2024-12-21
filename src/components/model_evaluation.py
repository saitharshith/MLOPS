import os
import sys
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.utils.utils import load_object
from dataclasses import dataclass
import logging
from src.exceptions.exceptions import custom_exception
@dataclass
class ModelEvaluationConfig:
#configuration for data ingestion
    pass

class ModelEvaluation:
#data ingestion
    def __init__(self):
        pass
    def initiate_model_eval(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise custom_exception(sys,e)