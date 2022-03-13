#!/usr/bin/env python3
import sports_book_manager.implied_probability_calculator as ipc
import unittest

def smoke_test(odds):
    """
    Tests valid inputs for the implied_probability_calculator
    """
    try:
        ipc.implied_probability_calculator(odds)
        return True
    except:
        return False

smoke_test([-110, 120, -150, 100, 210])

class TestIPC(unittest.TestCase):
    """
    Tests invalid inputs for the implied_probability_calculator to see if
    the ValueError is raised.
    """
    def invalid_odds(self):
        self.assertRaises(ValueError, ipc.implied_probability_calculator,
                          ['help', 40, 15/2])
