from setuptools import setup


# requirements
reqs = list()
with open('requirements.txt') as file:
    for line in file:
        reqs.append(line.strip())

# readme
README = open('README.rst').read()
HISTORY = open('HISTORY.rst').read()

setup(
    name='coindata',
    version='1.3',
    description='Historical data manager for cryptos.',
    long_description=README + '\n\n' + HISTORY,
    packages=['coindata'],
    url='https://github.com/anaxilaus/coindata',
    author='Anaxilaus',
    install_requires=reqs
)
