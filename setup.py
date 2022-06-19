from gettext import install
from multiprocessing import AuthenticationError
from setuptools import setup
from typing import List



PROJECT_NAME = 'housing-predictor'
VERSION = '0.0.1'
AUTHOR = 'Ashok Kumar'
DISCRIPTION = 'Housing price prediction'
PACKEGE=['housing']
REQUIRMENT_FILE_NAME = 'requirements.txt'


def get_requirements(REQUIRMENT_FILE_NAME: str) -> List[str]:
    with open(REQUIRMENT_FILE_NAME) as f:
        return f.read().splitlines()

setup(
    name='PROJECT_NAME',
    version='VERSION',
    author=AUTHOR,
    packages=PACKEGE,
    description=DISCRIPTION,
    
    install_requires=get_requirements(REQUIRMENT_FILE_NAME),
)