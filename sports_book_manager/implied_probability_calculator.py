#!/usr/bin/env python3
"""
This function assumes that the odds are presented in American odds. This means
that 'favorites' are given line -100 or lower while 'underdogs' are given odds
100 or greater.
"""

def implied_probability_calculator(odds):
    """
    Converts odds in the data into probability the outcome occurs.

    Parameters
    ----------
        odds: the weighted return on the wager made if correct

    Returns
    -------
    int
        The market's expected probability of the team winning accounting for
        the line.
    """

    if abs(int(odds)) < 100:
        raise ValueError('American lines must be three digits or longer.')
    if odds < 0:
        return round((abs(odds)/(abs(odds) + 100)), 4)
    else:
        return round((100/(odds + 100)), 4)
