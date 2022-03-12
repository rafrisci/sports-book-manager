#!/usr/bin/env python3
from setuptools import setup, find_packages

def _find_packages():
    packages = find_packages()
    packages.append('sports-book-manager.data')
    return packages


setup(
    name='sports_book_manager',
    version='1.0.0',
    author='Ross Friscia',
    author_email='rafrisci@uw.edu',
    description='Get the odds in your favor',
    url='https://github.com/rafrisci/sports-book-manager',
    packages = _find_packages(),
    package_dir={
        'sports-book-manager.data': 'data',
        'sports_book_manager': 'sports_book_manager'
    },
    include_package_data=True,
    install_requires=[
        'selenium',
        'scipy',
        'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
