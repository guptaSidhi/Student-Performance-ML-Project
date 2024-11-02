# This is basically used to make our application as a package itself.
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''This Function is returning the list of all libraries used in Project'''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='StudentPerformaceMLProject',
    version='0.0.1',
    author='SidhiGupta',
    author_email='guptasidhi159@gmail.com',
    packages=find_packages(),  # This is used and we made a src folder with __init__.py file so that all the project is used as a package itself.
    intstall_requires=get_requirements('requirements.txt')
)