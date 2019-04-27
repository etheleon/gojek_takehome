from setuptools import find_packages, setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gojek',
    version='0.0.1',
    url = 'etheleon.github.io/gojek',
    author='Wesley Goi',
    author_email='etheleon@protonmail.com',
    packages=find_packages(),
    description='For calculating API input',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True
)
