![logo file](./logo.png)

[![Build Status](https://app.travis-ci.com/rafrisci/sports-book-manager.svg?branch=master)](https://app.travis-ci.com/rafrisci/sports-book-manager) [![Coverage Status](https://coveralls.io/repos/github/rafrisci/sports-book-manager/badge.svg?branch=master&service=github)](https://coveralls.io/github/rafrisci/sports-book-manager?branch=master) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/rafrisci/sports-book-manager/blob/master/LICENSE) 


# sports-book-manager
Sports-book-manager helps programmers connect their model predictions to the sports book of their choice. By inputting the necessary html information into an instance of the BookScraper class, users can get back all wagers of the sports book of their choice. This, along with a couple of python modules to convert and compare market odds to model outputs, does the tedious work for the user and saves them time.

---
## Project Organization
```
sports-book-manager/
  |- sports_book_manager/
    |- __init__.py
    |- book_scrape_class.py
    |- implied_probability_calculator.py
    |- model_probability.py
    |- tests/
      |- __init__.py
      |- test_book_scrape.py
      |- test_ipc_outputs.py
      |- test_mp_outputs.py
  |- data/
    |- hockey_odds.csv
    |- model_output_example.csv
  |-examples/
    |-example.ipynb
  |-docs/
    |-written_report.pdf
    |-presentation.pdf
  |- setup.py
  |- requirements.txt
  |- README.md
  |- LICENSE
```
---
## Installation
### On Windows Anaconda
Enter the following into your command prompt
```bash
pip3 install git+https://github.com/rafrisci/sports-book-manager
```
### On Linux
First create a clone of the repository
```bash
git clone https://github.com/rafrisci/sports-book-manager
```
Then go into the project directory and install the requirements
```bash
cd sports-book-manager
python -m pip install -r requirements.txt
```
Finally run the setup.py to download the package
```bash
sudo python setup.py install
```
---
## Usage
See the [example notebook](examples/example.ipynb) to see how the package works, using PointsBet and the [data files](data/).
