#!/usr/bin/env python3
"""
The model mean is added to the line because the model being positive means the
model expects the team to be better. However, the line being positive means the
market expects the team to be worse. Since they are calculated differently,
the line needs to change signs to match the model output.
"""
from scipy.stats import norm

def model_probability(model_mean, model_sd, line):
    """
    Get the probability an event occurs at the margin set with the market line.

    Parameters
    ----------
        model_mean: float
            the expected margin of victory from the model
        model_sd: float
            the standard deviation of the model's margin of victory
        line: float
            the margin of victory the market is setting the wager at

    Returns
    -------
    int
        The model's expected probability of the team winning accounting for the
        line.
    """
    z_score = (model_mean + line)/abs(model_sd)
    return norm.cdf(z_score)
