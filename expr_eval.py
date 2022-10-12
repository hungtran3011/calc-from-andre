"""
A new, reimplemented evaluation algorithm / expression parser instead of Python's built-in eval() function.
This works with the symbols that we are used to when learning math, e.g. obelus (÷) sign for division or radical sign for root, etc,
which are converted Python's operations and functions for evaluation.
"""

from math import pow, log, factorial, lcm, gcd, sin, cos, tan, sinh, cosh, tanh, asin, acos, atan, asinh, acosh, atanh
from structures import Stack
