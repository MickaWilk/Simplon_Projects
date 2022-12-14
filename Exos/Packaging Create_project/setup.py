# https://pypi.org/project/setuptools/

from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
    requirements = [x.strip() for x in content if "git+" not in x]


setup(name="mon_packet",
      version="2.0",
      # packages=find_packages(),
      packages=find_packages(),
      install_requires=requirements,
      scripts=["scripts/hello", "scripts/start_project", "scripts/fichier_append"])
