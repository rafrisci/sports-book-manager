from setuptools import setup, find_packages

setup(
    name='sports-book-manager',
    version='1.0.0',
    author='Ross Friscia',
    author_email='rafrisci@uw.edu',
    description='Get the odds in your favor',
    url='https://github.com/rafrisci/sports-book-manager',
    packages = find_packages(),
    package_data={
        'sports-book-manager': ['data/*.csv']
    },
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
