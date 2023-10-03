from sympy import symbols, diff

x, y = symbols('x y')

equation_1 = "0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3"

equation_2 = "0.2 * x ** 2 + y + 0.1 * x * y - 0.7"

equation_3 = "x - y ** 2"

SYSTEM_1 = [equation_1, equation_2]
SYSTEM_2 = [equation_1, equation_3]
