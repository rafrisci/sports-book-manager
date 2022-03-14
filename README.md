![logo file](./logo.PNG)

[![Build Status](https://app.travis-ci.com/rafrisci/sports-book-manager.svg?branch=master)]((https://app.travis-ci.com/rafrisci/sports-book-manager) [![Coverage Status](https://coveralls.io/repos/github/rafrisci/sports-book-manager/badge.svg?branch=master)](https://coveralls.io/github/rafrisci/sports-book-manager?branch=master) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/rafrisci/sports-book-manager/blob/master/LICENSE) 


# sports-book-manager
Sports-book-manager helps programmers connect their model predictions to the sports book of their choice. By inputting the necessary html information into an instance of the BookScraper class, users can get back all wagers of the sports book of their choice. This, along with a couple of python modules to convert and compare market odds to model outputs, does the tedious work for the user and saves them time.

## Project Organization
```
AWS-foryou/
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
  |- setup.py
  |- requirements.txt
  |- README.md
  |- LICENSE
```
