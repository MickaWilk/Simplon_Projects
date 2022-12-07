from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    content = f.readlines()
    requirements = [x.strip() for x in content if 'git+' not in x]

setup(
    name='popo',
    version='0.0.0.1',
    packages=find_packages(),
    description="Creation automatisé d'une architecture ML",
    author=...,
    author_email='...',
    scripts=['scripts/run_popo'],
    # package_data={
    #     "": ["*.joblib"],
    # },
    # include_package_data=True,
    install_requires=requirements
)