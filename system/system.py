from sympy import symbols, diff

x, y = symbols('x y')

equation_1 = x ** 2 + y ** 2 - 1

equation_2 = x ** 2 - y - 0.5

equation_3 = x - y ** 2

SYSTEM_1 = [equation_1, equation_2]
SYSTEM_2 = [equation_1, equation_3]