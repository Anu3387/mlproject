from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT ='-e .'

def get_requirment(file_path:str)->List[str]:
        
     requirments=[]
     with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace('\n',"")for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
            
     return requirments


setup(

    name= 'mlproject',
    version='0.01',
    author='anu',
    author_email='anubhosale3387@gmail.com',
    packages=find_packages(),
    install_requries = get_requirment('requirments.txt')
)