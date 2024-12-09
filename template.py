import os
from pathlib import Path #create a system compatable path
import logging

list_of_files =[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",
    "src/pipline/__init__.py",
    "src/pipline/training_pipeline.py",
    "src/pipline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exceptions/exceptions.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/eperiments.ipynb",
]

#creating file directory
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory:{filedir} for file: {filename}")

    if(not os.path.exists(filepath)or os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            logging.info(f"Created file: {filepath}")
            pass