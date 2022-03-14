#!/usr/bin/env python3
"""
Creates the BookScraper class. It then uses the instances of the class to start
a Selenium scrape and output a pandas df with the teams, spread, and odds of
the league of choice.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


#  creating baseclass scraper
class BookScraper(object):
    """
    A class to store and update domain, directories, and html properties of a
    sports book website.
    Attributes
    ----------
        domain: str
            base website path
        directories: dict
            league names as keys and directory paths as values
        ancestor_container: str
            class value which contains event rows
        event_row: str
            class value which contains event teams, lines, and odds
        team_class: str
            class value which has individual teams
        line_class: str
            class value which has individual lines
        odds_class: str
            class value which has individual odds
        team_parent_tag: str, optional
            html tag that contains team information for the event
        team_parent_attr: str, optional
            html attribute that contains team information for the event
        team_parent_val: str, optional
            part or all of the html atrribute value unique to the tag for teams
        line_parent_tag: str, optional
            html tag that contains line information for the event
        line_parent_attr: str, optional
            html attribute that contains line information for the event
        line_parent_val: str, optional
            part or all of the html atrribute value unique to the tag for lines
        odds_parent_tag: str, optional
            html tag that contains odds information for the event
        odds_parent_attr: str, optional
            html attribute that contains odds information for the event
        odds_parent_val: str, optional
            part or all of the html atrribute value unique to the tag for odds
        driver_path: str, optional
            the path to your chromedriver. Only needed if webdriver.Chrome()
            returns an error
    Methods
    -------
    update_directories:
        appends or sets a new dict for an instance's directory.
    update_html_elements:
        changes all called parameters to their new value.
    retrieve_sports_book:
        runs the scraper to get all events of a league.
    """
    def __init__(self, domain, directories):
        """
        Constructs all necessary attributes for the scraper.
        Parameters
        ----------
        domain: str
            base website path
        directories: dict
            league names as keys and directory paths as values
        Attributes
        ----------
        ancestor_container: str
            class value which contains event rows
        event_row: str
            class value which contains event teams, lines, and odds
        team_class: str
            class value which has individual teams
        line_class: str
            class value which has individual lines
        odds_class: str
            class value which has individual odds
        team_parent_tag: str, optional
            html tag that contains team information for the event
        team_parent_attr: str, optional
            html attribute that contains team information for the event
        team_parent_val: str, optional
            part or all of the html atrribute value unique to the tag for teams
        line_parent_tag: str, optional
            html tag that contains line information for the event
        line_parent_attr: str, optional
            html attribute that contains line information for the event
        line_parent_val: str, optional
            part or all of the html atrribute value unique to the tag for lines
        odds_parent_tag: str, optional
            html tag that contains odds information for the event
        odds_parent_attr: str, optional
            html attribute that contains odds information for the event
        odds_parent_val: str, optional
            part or all of the html atrribute value unique to the tag for odds
        driver_path: str, optional
            the path to your chromedriver. Only needed if webdriver.Chrome()
            returns an error
        Returns
        -------
        None.
        """
        #  makes sure the user inputs directories in dictionary
        if not isinstance(directories, dict):
            raise TypeError('directories must be stored as dicts')
        self.domain = domain
        self.directories = directories
        self.ancestor_container = None
        self.event_row = None
        self.team_parent_tag = None
        self.team_parent_attr = 'class'
        self.team_parent_val = None
        self.line_parent_tag = None
        self.line_parent_attr = 'class'
        self.line_parent_val = None
        self.odds_parent_tag = None
        self.odds_parent_attr = 'class'
        self.odds_parent_val = None
        self.team_class = None
        self.line_class = None
        self.odds_class = None
        self.driver_path = None

    #  update directory dicts of website
    def update_directories(self, new_directories):
        """
        Appends or sets a new dict for an instance's directory.
        Parameters
        ----------
        new_directories: dict
            updates the directories value if the key exists
        Returns
        -------
        None.
        """
        if not isinstance(new_directories, dict):
            raise TypeError('directories must be stored and updated as dicts')
        for key in new_directories.key():
            self.directories[key] = new_directories[key]

    #  make function so user can update all values in one place
    def update_html_elements(self, ancestor_container=..., event_row=...,
                             team_class=..., line_class=..., odds_class=...,
                             team_parent_tag=..., team_parent_attr=...,
                             team_parent_val=..., line_parent_tag=...,
                             line_parent_attr=..., line_parent_val=...,
                             odds_parent_tag=..., odds_parent_attr=...,
                             odds_parent_val=..., new_domain=...,
                             drive_path=...):
        """
        Changes all called parameters to their new value.
        Parameters
        ----------
        ancestor_container : str, optional
            class value which contains event rows
        event_row : str, optional
            class value which contains event teams, lines, and odds
        team_class : str, optional
            class value which has individual teams
        line_class : str, optional
            class value which has individual lines
        odds_class : str, optional
            class value which has individual odds
        team_parent_tag : str, optional
            html tag that contains team information for the event
        team_parent_attr : str, optional
            html attribute that contains team information for the event
        team_parent_val : str, optional
            part or all of the html atrribute value unique to the tag for teams
        line_parent_tag : str, optional
            html tag that contains line information for the event
        line_parent_attr : str, optional
            html attribute that contains line information for the event
        line_parent_val : str, optional
            part or all of the html atrribute value unique to the tag for lines
        odds_parent_tag : str, optional
            html tag that contains odds information for the event
        odds_parent_attr : str, optional
            html attribute that contains odds information for the event
        odds_parent_val : str, optional
            part or all of the html atrribute value unique to the tag for odds
        new_domain : str, optional
            base website path
        drive_path : str, optional
            the path to your chromedriver. Only needed if webdriver.Chrome()
            returns an error
        Returns
        -------
        None.
        """
        new_vals = locals()
        new_vals.pop('self')
        FCN_DICT = {'ancestor_container': self.__ancestor_cont,
                    'event_row': self.__row_cls, 'team_class': self.__team_cls,
                    'line_class': self.__line_cls,
                    'odds_class': self.__odds_cls,
                    'team_parent_tag': 'team_parent_tag',
                    'team_parent_attr': 'team_parent_attr',
                    'team_parent_val': 'team_parent_val',
                    'line_parent_tag': 'line_parent_tag',
                    'line_parent_attr': 'line_parent_attr',
                    'line_parent_val': 'line_parent_val',
                    'odds_parent_tag': 'odds_parent_tag',
                    'odds_parent_attr': 'odds_parent_attr',
                    'odds_parent_val': 'odds_parent_val',
                    'new_domain': 'domain', 'drive_path': 'driver_path'}
        FCN_FREE = ['team_parent_tag', 'team_parent_attr', 'team_parent_val',
                    'line_parent_tag', 'line_parent_attr', 'line_parent_val',
                    'odds_parent_tag', 'odds_parent_attr', 'odds_parent_val',
                    'new_domain', 'drive_path']
        for updated_val in new_vals:
            if new_vals[updated_val] is ...:
                pass
            elif updated_val in FCN_FREE:
                setattr(self, FCN_DICT[updated_val], new_vals[updated_val])
            else:
                FCN_DICT[updated_val](str(new_vals[updated_val]))

    def retrieve_sports_book(self, league):
        """
        Runs the Selenium scraper to get all events of a league.
        Parameters
        ----------
        league: str
            directories key of sports league you want events for.
        Returns
        -------
        pandas df
            A dataframe containing the teams, lines, and odds of all events.
        """
        if league not in self.directories.keys():
            raise ValueError('league value must be a key within the class'
                             'directory')
        driver = self.__driver_initialize(self.domain,
                                          self.directories[league],
                                          self.driver_path)
        event_rows = self.__find_event_rows(driver, self.ancestor_container,
                                            self.event_row)
        team_list = []
        line_list = []
        odds_list = []
        for event in event_rows:
            self.__get_teams(event, self.team_class, self.team_parent_tag,
                             self.team_parent_attr, self.team_parent_val,
                             team_list)
            self.__get_lines(event, self.line_class, self.line_parent_tag,
                             self.line_parent_attr, self.line_parent_val,
                             line_list)
            self.__get_odds(event, self.odds_class, self.odds_parent_tag,
                            self.odds_parent_attr, self.odds_parent_val,
                            odds_list)
        driver.quit()
        return self.__initial_df(team_list, line_list, odds_list)

    #  private methods for update_elements
    #  make sure CSS_SELECTOR can read the class values
    def __ancestor_cont(self, container):
        if container[0] == '.':
            self.ancestor_container = container
        else:
            self.ancestor_container = '.' + container

    def __row_cls(self, row_cls):
        if row_cls[0] == '.':
            self.event_row = row_cls
        else:
            self.event_row = '.' + row_cls

    def __team_cls(self, team_cls):
        if team_cls[0] == '.':
            self.team_class = team_cls
        else:
            self.team_class = '.' + team_cls

    def __line_cls(self, line_cls):
        if line_cls[0] == '.':
            self.line_class = line_cls
        else:
            self.line_class = '.' + line_cls

    def __odds_cls(self, odds_cls):
        if odds_cls[0] == '.':
            self.odds_class = odds_cls
        else:
            self.odds_class = '.' + odds_cls

    #  private methods for retrieve_sports_book
    #  open up the driver and start to pull the website data
    def __driver_initialize(self, domain, directory, path):
        driver = webdriver.Chrome(path)
        driver.get(domain + directory)
        time.sleep(10)
        return driver

    #  get the event rows of the web page
    def __find_event_rows(self, driver, ancestor_container, event_row):
        parent_container = driver.find_element(By.CSS_SELECTOR,
                                               ancestor_container)
        event_rows = parent_container.find_elements(By.CSS_SELECTOR,
                                                    event_row)
        return event_rows

    #  get the teams in the event row
    def __get_teams(self, event, team_class, team_parent_tag, team_parent_attr,
                    team_parent_val, team_list):
        if team_parent_tag and team_parent_attr:
            team_paths = (f".//{team_parent_tag}[contains(@{team_parent_attr}"
                          f", '{team_parent_val}')]")
            team_parent = event.find_elements(By.XPATH, team_paths)
            for team_entry in team_parent:
                team = team_entry.find_element(By.CSS_SELECTOR, team_class)
                team_list.append(team.text)
        else:
            teams = event.find_elements(By.CSS_SELECTOR, team_class)
            for team in teams:
                team_list.append(team.text)

    #  get the lines in the event row
    def __get_lines(self, event, line_class, line_parent_tag, line_parent_attr,
                    line_parent_val, line_list):
        if line_parent_tag and line_parent_attr:
            line_paths = (f".//{line_parent_tag}[contains(@{line_parent_attr}"
                          f", '{line_parent_val}')]")
            line_parent = event.find_elements(By.XPATH, line_paths)
            for line_entry in line_parent:
                line = line_entry.find_element(By.CSS_SELECTOR, line_class)
                line_list.append(line.text)
        else:
            lines = event.find_elements(By.CSS_SELECTOR, line_class)
            for line in lines:
                line_list.append(line.text)

    #  get the odds in the event row
    def __get_odds(self, event, odds_class, odds_parent_tag, odds_parent_attr,
                   odds_parent_val, odds_list):
        if odds_parent_tag and odds_parent_attr:
            odds_paths = (f".//{odds_parent_tag}[contains(@{odds_parent_attr}"
                          f", '{odds_parent_val}')]")
            odds_parent = event.find_elements(By.XPATH, odds_paths)
            for odds_entry in odds_parent:
                odds = odds_entry.find_element(By.CSS_SELECTOR, odds_class)
                odds_list.append(odds.text)
        else:
            spreads = event.find_elements(By.CSS_SELECTOR, odds_class)
            for odds in spreads:
                odds_list.append(odds.text)

    #  return the dataframe
    def __initial_df(self, teams, lines, odds):
        return pd.DataFrame(list(zip(teams, lines, odds)),
                            columns=['Teams', 'Lines', 'Odds'])
