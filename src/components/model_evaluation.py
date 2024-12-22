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
    pass

class ModelEvaluation:
    def __init__(self):
        pass
    def eval_metrics(self,actual,pred):
        r2=r2_score(actual,pred)
        mae=mean_absolute_error(actual,pred)
        mse=mean_squared_error(actual,pred)
        return mae, mse,r2

    def initiate_model_eval(self,test_array,train_array):
        try:
            x_test,y_test=(test_array[:,:-1],test_array[:,-1])
            model_path= os.path.join('artifacts','model.pkl')
            model=load_object(model_path)
            
            # mlflow.set_registry_uri("")
            
            tracking_url=urlparse(mlflow.get_registry_uri()).scheme
            print(tracking_url)
            with mlflow.start_run():
                predictions=model.predict(x_test)
                mae,mse,r2=self.eval_metrics(y_test,predictions)
                mlflow.log_metric("mean squared error",mse)
                mlflow.log_metric("mean absolute error",mae)
                mlflow.log_metric("r2 score",r2)
                mlflow.sklearn.log_model(model,"model",registered_model_name="model_v1")
                
        except Exception as e:
            logging.info()
            raise custom_exception(sys,e)