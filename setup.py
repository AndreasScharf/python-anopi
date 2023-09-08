from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='python_anopi',
    version='0.2.1',
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    url='https://github.com/AndreasScharf/python-anopi',
    author='Andreas Scharf',
    author_email='info@frappgmbh.de',
    license='MIT',
    packages=['python_anopi'],
    install_requires=['pi-ina219'],

    classifiers=[
       
    ],
)
