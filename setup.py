import os
import sys
import warnings
from setuptools import setup

version = "1.1.0"

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = []

if sys.version_info < (2, 7):
    warnings.warn(
        'Python 2.6 is not officially supported by Bayonet. '
        'If you have any questions, please file an issue on Github or '
        'contact us at support@bayonet.io.',
        DeprecationWarning)

setup(
    name='bayonet',
    version=version,
    description='Bayonet python client library',
    long_description=open('README.md').read(),
    license='MIT',
    author='Bayonet',
    author_email='support@bayonet.io',
    url='https://github.com/Bayonet-Client/bayonet-python',
    packages=['bayonet', 'test'],
    install_requires=['requests'],
    test_suite='test.test_bayonet',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
