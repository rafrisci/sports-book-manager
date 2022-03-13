#!/usr/bin/env python3
import sports_book_manager.model_probability as mp

def smoke_test(model_mean, model_sd, line):
    """
    Test to make sure outputs are occuring with valid inputs.
    """
    try:
        mp.model_probability(model_mean, model_sd, line)
        return True
    except:
        return False

smoke_test(-0.5,0.5,0.5)
smoke_test(4,0.86,-2.6)
