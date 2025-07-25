from setuptools import setup,find_packages

with open("requirements.txt") as f:
   requirements = f.read().splitlines()

setup (
    name="MLOPS-Project-6",
    version = 1,
    author= "Sai Sandy",
    packages=find_packages(),
    install_requires = requirements,
)