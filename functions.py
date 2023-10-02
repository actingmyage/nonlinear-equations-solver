import sympy as sp
import numpy as np
import warnings
import scipy.optimize as opt

warnings.filterwarnings("ignore", category=DeprecationWarning)
# TODO check that a function is continuous on an interval

class Function:
    def __init__(self, string_function):
        self.function = sp.sympify(string_function)
        self.string_function = string_function

    def __call__(self, x_value) -> float:
        x = sp.symbols('x')
        return self.function.subs(x, x_value)

    def scalar_function(self):
        return lambda x: self.__call__(x)

    def __str__(self):
        return self.string_function


FUNCTIONS = [
    'x ** 3 - x + 4',
    'x ** 2 + 3 * x - 2',
    'sin(x) + 0.1 * x ** 2'
]


def check_interval(f, a, b) -> tuple[float, float]:
    """
    :param f: function
    :param a: left border of interval
    :param b: right border of interval
    :return: interval containing roots or error message
    """

    if a >= b:
        raise Exception("Error: The left border of the interval must be less than the right border!")

    print("Checking the interval for the presence of roots...")
    fa = f(a)
    fb = f(b)
    print(f"{fa} * {fb} = {fa * fb}")

    if f(a) * f(b) > 0:

        delta = 0.01
        warning = f"We reduce the interval until find the roots or until the difference between a and b becomes less than Δ = {delta}"

        print(warning)

        decreases = 0
        while abs(b - a) > delta:
            a += delta
            b -= delta
            fa = f(a)
            fb = f(b)
            decreases += 1
            print(f"{fa} * {fb} = {fa * fb}")

            if f(a) * f(b) <= 0:
                if f(a) * f(b) < 0:
                    message = f"We have decreased the interval {decreases} times and found roots"
                    print(message)
                else:
                    print(f"We have decreased the interval {decreases} times and found one root")

                print(f"New borders: a = {a}, b = {b}")
                return a, b

        raise Exception("Error: There are no roots on this interval!")

    elif f(a) * f(b) == 0:
        print("There is one root on a given interval!")
    else:
        print("There are roots on a given interval!")

    return a, b


def check_derivative_sign(f, a, b) -> bool:
    x = sp.symbols('x')

    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)

    x_values = np.linspace(a, b, 10)

    sign_f_prime = sp.sign(f_prime.subs(x, x_values[0]))
    sign_f_double_prime = sp.sign(f_double_prime.subs(x, x_values[0]))

    sign_changed = False

    for x_val in x_values:
        curr_sign_f_prime = sp.sign(f_prime.subs(x, x_val))
        curr_sign_f_double_prime = sp.sign(f_double_prime.subs(x, x_val))
        print(f"At x = {x_val}: f' = {curr_sign_f_prime}, f'' = {curr_sign_f_double_prime}")

        if curr_sign_f_prime != sign_f_prime or curr_sign_f_double_prime != sign_f_double_prime:
            sign_changed = True
            break

    if sign_changed:
        print("The sign of the first or second derivative changes on the interval.")
        return False
    else:
        print("The sign of the first and second derivatives remains the same on the interval.")
        return True


# FIXME
# def derivative_not_zero_on_interval(f: Function, a: float, b: float) -> bool:
#     result = opt.minimize_scalar(f.scalar_function(), bounds=(a, b))
#     if result.success and result.fun != 0:
#         print("The derivative is not equal to zero on the interval!")
#         return True
#     else:
#         print("The derivative is zero on the interval!")
#         return False


def phi_of_x_lam(f, lam, x):
    """
    Used in the simple iteration method

    :param f: f(x)
    :param lam: lambda
    :param x: x
    :return: φ(x)
    """

    print(f"{x} + {lam} * {f(x)} = {x + lam * f(x)}")
    return x + lam * f(x)


def phi_of_x_lam_der(f, lam, x):
    """
    Used in the simple iteration method

    :param f: f'(x)
    :param lam: lambda
    :param x: x
    :return: φ'(x)
    """

    x_sym = sp.symbols('x')
    print(f"1 + {lam} * {f.subs(x_sym, x)} = {1 + lam * f.subs(x_sym, x)}")

    return 1 + lam * f.subs(x_sym, x)
