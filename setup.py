from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e.'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # .strip() to remove newlines and extra spaces

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='FLIGHT-FARE-PREDICTION-ML-PROJECT',
    version='3.11.5',
    author='Sudhanshu Upadhyay',
    author_email='bhanuupadhyay302448@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
