#!usr/bin/env python3
"""
Creates the BookScraper object. This stores and updates the website,
directories, and html properties needed to scrape the sports book website. It
can also then start a Selenium scrape and output a pandas df with the teams,
spread, and odds of the even.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

#creating baseclass scraper
class BookScraper(object):
    def __init__(self, domain, directories):
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

    #make sure CSS_SELECTOR can read the class values
    def ancestor_cont(self, container):
        if container[0] == '.':
            self.ancestor_container = container
        else:
            self.ancestor_container = '.' + container

    def row_cls(self, row_cls):
        if row_cls[0] == '.':
            self.event_row = row_cls
        else:
            self.event_row = '.' + row_cls

    def team_cls(self, team_cls):
        if team_cls[0] == '.':
            self.team_class = team_cls
        else:
            self.team_class = '.' + team_cls

    def line_cls(self, line_cls):
        if line_cls[0] == '.':
            self.line_class = line_cls
        else:
            self.line_class = '.' + line_cls

    def odds_cls(self, odds_cls):
        if odds_cls[0] == '.':
            self.odds_class = odds_cls
        else:
            self.odds_class = '.' + odds_cls

    #make function so user can update all values in one place
    def update_elements(self, container=..., row_cls=..., team_cls=...,
                        line_cls=..., odds_cls=..., team_tag=...,
                        team_attr=..., team_val=..., line_tag=...,
                        line_attr=..., line_val=..., odds_tag=...,
                        odds_attr=..., odds_val=..., drive_path=...):
        new_vals = locals()
        new_vals.pop('self')
        FCN_DICT = {'container':self.ancestor_cont, 'row_cls':self.row_cls,
                    'team_cls':self.team_cls, 'line_cls':self.line_cls,
                    'odds_cls':self.odds_cls, 'team_tag': 'team_parent_tag',
                    'team_attr':'team_parent_attr',
                    'team_val':'team_parent_val', 'line_tag':'line_parent_tag', 
                    'line_attr':'line_parent_attr',
                    'line_val':'line_parent_val', 'odds_tag':'odds_parent_tag',
                    'odds_attr':'odds_parent_attr',
                    'odds_val':'odds_parent_val', 'drive_path':'driver_path'}
        FCN_FREE = ['team_tag', 'team_attr', 'team_val', 'line_tag',
                    'line_attr', 'line_val', 'odds_tag', 'odds_attr',
                    'odds_val', 'drive_path']
        for i in new_vals:
            if new_vals[i] is ...:
                pass
            elif i in FCN_FREE:
                setattr(self, FCN_DICT[i], new_vals[i])
            else:
                FCN_DICT[i](str(new_vals[i]))

    #open up the driver and start to pull the website data
    def driver_initialize(self, domain, directory, path):
        driver = webdriver.Chrome(path)
        driver.get(domain + directory)
        time.sleep(10)
        return driver

    #get the event rows of the web page
    def find_event_rows(self, driver, ancestor_container, event_row):
        parent_container = driver.find_element(By.CSS_SELECTOR,
                                               ancestor_container)
        event_rows = parent_container.find_elements(By.CSS_SELECTOR,
                                                    event_row)
        return event_rows

    #get the teams in the event row
    def get_teams(self, event, team_class, team_parent_tag, team_parent_attr,
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

    #get the lines in the event row
    def get_lines(self, event, line_class, line_parent_tag, line_parent_attr,
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

    #get the oddss in the event row
    def get_odds(self, event, odds_class, odds_parent_tag, odds_parent_attr,
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

    #return the dataframe
    def initial_df(self, teams, lines, odds):
        return pd.DataFrame(list(zip(teams, lines, odds)),
                            columns=['Teams', 'Lines', 'Odds'])

    def retrieve_sports_book(self, league):
        driver = self.driver_initialize(self.domain, self.directories[league],
                                        self.driver_path)
        event_rows = self.find_event_rows(driver, self.ancestor_container,
                                          self.event_row)
        team_list = []
        line_list = []
        odds_list = []
        for event in event_rows:
            self.get_teams(event, self.team_class, self.team_parent_tag,
                           self.team_parent_attr, self.team_parent_val,
                           team_list)
            self.get_lines(event, self.line_class, self.line_parent_tag,
                           self.line_parent_attr, self.line_parent_val,
                           line_list)
            self.get_odds(event, self.odds_class, self.odds_parent_tag,
                          self.odds_parent_attr, self.odds_parent_val,
                          odds_list)
        driver.quit()
        return self.initial_df(team_list, line_list, odds_list)
