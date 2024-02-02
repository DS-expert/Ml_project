from setuptools import find_packages,setup
from typing import List

hypen_e_dot = "-e ."

def get_requirments(file_path:str) -> List[str]:
    """
        this function will return the list of requirment 
    """
    requirment = []
    with open(file=file_path) as file_obj:
        requirment  = file_obj.readlines()
        requirment = [req.replace("\n"," ")for req in requirment]

        if hypen_e_dot in requirment:
            requirment.remove(hypen_e_dot)

    return requirment


setup(
    name='mlproject',
    version='0.0.1',
    author='Ahmad Ali',
    author_email='workmy.chd@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('Requirments.txt')

)
