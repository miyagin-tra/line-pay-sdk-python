from setuptools import setup, find_packages

def _requirements():
    with open('requirements.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]

with open('README.rst', 'r') as fd:
    long_description = fd.read()

setup(
    name='line-pay',
    version='0.0.1',
    description='LINE Pay API SDK for Python',
    long_description=long_description,
    author='Sumihiro Kagawa',
    author_email='sumihiro@gmail.com',
    url='https://github.com/sumihiro3/line-pay-sdk-python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'requests', 'examples')),
	install_requires=_requirements(),
)
