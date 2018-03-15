from codecs import open
from setuptools import setup
import shutil


# requirements
reqs = list()
with open('requirements.txt', encoding='utf-8') as file:
    for line in file:
        reqs.append(line.strip())

# readme
README = open('README.rst').read()
HISTORY = open('HISTORY.rst').read()

setup(
    name='coindata',
    version='1.0',
    description='Parse and cache historical data from coinmarketcap.',
    long_description=README + '\n\n' + HISTORY,
    packages=['coindata'],
    url='https://github.com/anaxilaus/coindata',
    author='Anaxilaus',
    install_requires=reqs
)

# remove unnecessary files
for directory in ('dist', 'build', 'coindata.egg-info'):
    shutil.rmtree(directory)
