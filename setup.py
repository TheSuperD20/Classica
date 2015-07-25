from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='classica',
    version='1.0',
    description='Template',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    author='Alexander Shendrik',
    url='https://plus.google.com/u/0/+AlexandrShendrik/posts',
    author_email='thesuperd20@icloud.com',
)