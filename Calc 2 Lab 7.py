from sympy import *
from sympy.plotting import (plot, plot_parametric)
import matplotlib.pyplot as plt
import numpy as np


# 1.
print('1.')
#
#   a.
print('a.')
series = 0
for n in range(1, 11):
    series += 1/(n**4)
print(f'The partial sum s_10 of the series is {series}')
p_series = ((pi**4)/90).evalf()
print(f'The percent error of 10th partial sum is {100*(p_series-series)/p_series}%')
#   b.
print('b.')

