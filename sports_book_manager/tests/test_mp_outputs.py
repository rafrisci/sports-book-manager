#!/usr/bin/env python3
import sports_book_manager.model_probability as mp
import unittest


class TestMP(unittest.TestCase):
    """
    Tests valid inputs for model_probability return results.
    """
    def valid_tests(self):
        """
        Tests to make sure outputs are occuring with valid inputs.
        """
        self.assertTrue(mp.model_probability(-0.5, 0.5, 0.5))
        self.assertTrue(mp.model_probability(4, 0.86, -2.6))
