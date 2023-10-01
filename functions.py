import sympy as sp


class Function:
    def __init__(self, string_function):
        self.function = sp.sympify(string_function)

    def __call__(self, x_value) -> float:
        x = sp.symbols('x')
        return self.function.subs(x, x_value)


FUNCTIONS = [
    'x ** 3 - x + 4',
    'x ** 2 + 3 * x - 2',
    'sin(x) + 0.1 * x ** 2'
]


def phi_of_x_lam(f, lam, x):
    """
    Used in the simple iteration method

    :param f: f(x)
    :param lam: lambda
    :param x: x
    :return: φ(x)
    """
    return x + lam * f(x)


def phi_of_x_lam_der(f, lam, x):
    """
    Used in the simple iteration method

    :param f: f'(x)
    :param lam: lambda
    :param x: x
    :return: φ'(x)
    """
    return 1 + lam * f(x)
