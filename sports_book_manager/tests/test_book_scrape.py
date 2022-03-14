#!/usr/bin/env python3
import sports_book_manager.book_scrape_class as bs
import unittest
import pandas as pd


TS = bs.BookScraper(r'https://nj.pointsbet.com/sports',
                    {'NBA': r'/basketball/NBA'})
TS_2 = bs.BookScraper(r'https://nj.pointsbet.com/sports',
                      {'NBA': r'/basketball/NBA'})
TS_2.update_html_elements(ancestor_container='.facf5sk', event_row=".f1oyvxkl",
                          team_class='.fji5frh.fr8jv7a.f1wtz5iq',
                          line_class='.fsu5r7i', line_parent_tag='button',
                          line_parent_attr='data-test',
                          line_parent_val='Market0OddsButton',
                          odds_class='.fheif50', odds_parent_tag='button',
                          odds_parent_attr='data-test',
                          odds_parent_val='Market0OddsButton',
                          drive_path=r'/usr/local/bin/chromedriver')


class TestBookScraper(unittest.TestCase):
    """
    Tests involving the BookScraper class
    """
    def test_nondict_directories(self):
        """
        Test non-dictionary directories return an error
        """
        self.assertRaises(TypeError,
                          bs.BookScraper, r'https://nj.pointsbet.com/sports',
                          r'/basketball/NBA')

    def test_update_directories_error(self):
        """
        Test directory updates are provided as dictionaries as well
        """
        self.assertRaises(TypeError, TS.update_directories, 'test')

    def test_update_elements(self):
        """
        Tests ensuring every attribute in update_html_elements can be set
        without issue. Also confirming that private methods work for both
        conditions
        """
        self.assertIsNone(TS.update_html_elements('faf5he', '3irhs', 'qod93',
                                                'dsfae31', 'f93jejw', 'button',
                                                'name', 'w4rds', 'button',
                                                'name', 'w4rds', 'button',
                                                'name', 'w4rds',
                                                r'www.google.com',
                                                r'C:\chromedrive'))
        self.assertIsNone(TS.update_html_elements('.f4fshe', '.hales', '.32hdn',
                                                '.q3hkd', '.bioewon'))

    def test_retrieve_sports_book(self):
        """
        Tests ensuring the scraper works as intended
        """
        self.assertIsInstance(TS_2.retrieve_sports_book('NBA'), pd.DataFrame)
