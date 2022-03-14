#!/usr/bin/env python3
import sports_book_manager.implied_probability_calculator as ipc
import unittest


class TestIPC(unittest.TestCase):
    """
    Unittests for the implied_probability_calculator.
    """
    def test_invalid_odds(self):
        """
        Tests invalid inputs for the implied_probability calculator to see if
        the ValueError is raised.
        """
        self.assertRaises(ValueError, ipc.implied_probability_calculator,
                          'help')
        self.assertRaises(ValueError, ipc.implied_probability_calculator,
                          15/2)
        self.assertRaises(ValueError, ipc.implied_probability_calculator,
                          40)

    def test_valid_tests(self):
        """
        Tests valid inputs for the implied_probability_calculator.
        """
        self.assertTrue(ipc.implied_probability_calculator(-150))
        self.assertTrue(ipc.implied_probability_calculator(-110))
        self.assertTrue(ipc.implied_probability_calculator(120))
        self.assertTrue(ipc.implied_probability_calculator(100))
        self.assertTrue(ipc.implied_probability_calculator(210))
