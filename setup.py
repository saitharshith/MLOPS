from setuptools import find_packages,setup
from typing import List

setup(
    name='GemPricePrediction',
    version='0.0.1',
    author='Sai Tharshith',
    author_email='sai1726791@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)