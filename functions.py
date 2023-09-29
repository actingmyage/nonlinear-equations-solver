"""
0 - text representation of the function
1 - the function itself
2 - first derivative function
3 - second derivative of the function
"""
FUNCTIONS = [
    ('x^3 - x + 4', lambda x: x**3 - x + 4, lambda x: 3 * x ** 2 - 1, lambda x: 6 * x),
    ('x^2 + 3 * x - 2', lambda x: x ** 2 + 3 * x - 2, lambda x: 2*x + 3, lambda x: 2 * x + 3)
]
