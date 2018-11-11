import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



##Contingency Table Analyses
"""
Example Contingency Table:
---------------------------------
Outcome        Treatment Groups
            Test        Control
Positive     a             c
Negative     b             d
Total       a+b           c+d
---------------------------------
Key:
a = t_pos
b = t_neg
c = c_pos
d = c_neg
"""

# Proportion of positive outcomes under test condition
def p_test_subs(t_pos, t_neg):
    total = t_pos+t_neg
    p_test = t_pos/total
    return p_test

# Proportion of positive outcomes under control condition
def p_control_subs(c_pos, c_neg):
    total = c_pos+c_neg
    p_control = c_pos/total
    return p_control

# Basic difference of proportions of positive results in test, control groups
def diff_proportions(p_test, p_control):
    dop = p_control - p_test
    return dop

# Absolute risk difference of positive results in test, control groups
def diff_proportions(p_test, p_control):
    ard = np.abs(p_control - p_test)
    return ard

# Relative Risk
def relative_risk(p_test, p_control):
    rr = p_test/p_control
    return rr
