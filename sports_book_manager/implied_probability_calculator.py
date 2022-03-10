#!/usr/bin/env python3
"""
Converts the line in the data into probability the outcome occurs.

This function assumes that the line are presented in American line. This means
that 'favorites' are given line -100 or lower while 'underdogs' are given line
100 or greater.
"""

def implied_probability_calculator(line):
    if abs(int(line)) < 100:
        raise ValueError('American lines must be three digits or longer.')
    if line < 0:
        return round((abs(line)/(abs(line) + 100)), 4)
    else:
        return round((100/(line + 100)), 4)
