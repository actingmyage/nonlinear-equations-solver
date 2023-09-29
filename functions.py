"""
0 - text representation of the function
1 - the function itself
2 - first derivative function
3 - second derivative function
"""
from math import sin, cos

FUNCTIONS = [
    ('x^3 - x + 4', lambda x: x**3 - x + 4, lambda x: 3 * x ** 2 - 1, lambda x: 6 * x),
    ('x^2 + 3 * x - 2', lambda x: x ** 2 + 3 * x - 2, lambda x: 2*x + 3, lambda x: 2),
    ('sin(x) + 0.1 * x**2', lambda x: sin(x) + 0.1 * x**2, lambda x: cos(x) + (x / 5), lambda x: 1/5 * sin(x))
]
