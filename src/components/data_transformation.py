import pandas as pd
import numpy as np
from src.logger.Logging import logging
from src.exceptions.exceptions import custom_exception
import os
import sys
from dataclasses import dataclass
from pathlib import path
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.utils.utils import save_object
@dataclass
class DataTransformationConfig:
#configuration for data transformation
    pass

class DataTransformation:
#data ingestion
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise custom_exception(sys,e)