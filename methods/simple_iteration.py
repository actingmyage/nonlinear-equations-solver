from tabulate import tabulate
from functions import *

from scipy.optimize import minimize_scalar


TABLE_DATA = [["x_(i)", "x_(i+1)", "φ(x_(i+1))", "f(x_(i+1))", "|x_(i+1) - x_(i)|"]]


def simple_iteration_method(f, a, b, epsilon, max_iterations=50):
    """
    Implementation of the simple iteration method for finding
    the root of the equation y(x) = 0.

    :param f: function
    :param a: left border of interval
    :param b: right border of interval
    :param epsilon: accuracy
    :param max_iterations:  if we can't find the root after n iterations, we'll say
    that the equation has no solution
    :return: root :3
    """

    """
    in the simple iteration method, you need to express x from the equation.
    If this cannot be done explicitly, you can do the following:

    let's transform the equation: f(x) = 0 => λf(x) = 0 (λ != 0); | + x
    x = x + λf(x) =>

    φ(x) = x + λf(x), φ'(x) = 1 + λf'(x); λ = - (1 / max(f'(x) on [a, b]))
    """

    # variable and function definition
    x_sym = sp.symbols('x')
    # string representation of function, e.g. x ** 2 + 3 + 4
    f_string = str(f)
    # first derivative of the function
    f_prime = sp.diff(f_string, x_sym)
    # finding the maximum value of the derivative on an interval
    interval_values = np.linspace(a, b, 1000)
    derivative_values = [f_prime.subs(x_sym, val) for val in interval_values]
    max_derivative = max(derivative_values)
    # lambda
    lam = - (1 / max_derivative)

    print(f"We got a lambda equal to = {lam}")
    print(f"φ(x) = x + {lam} * ({str(f)})")

    """
      necessary condition for the convergence of the method:
      |φ'(x)| < q, 0 <= q < 1
      """

    print("Let's check necessary condition for the convergence of the method")

    necessity_1 = phi_of_x_lam_der(f_prime, lam, a)
    necessity_2 = phi_of_x_lam_der(f_prime, lam, b)

    if necessity_1 < 1 and necessity_2 < 1:
        print("The convergence condition is satisfied!")
    else:
        raise Exception("The convergence condition is not satisfied!")

    iterations = 1

    x0 = a
    while iterations < max_iterations:
        x_next = phi_of_x_lam(f, lam, x0)

        TABLE_DATA.append([x0, x_next, phi_of_x_lam(f, lam, x_next), f(x_next), abs(x_next - x0)])

        if abs(x_next - x0) <= epsilon:
            print(f"Root was not found in {iterations} iterations!")

            table = tabulate(TABLE_DATA, headers="firstrow", tablefmt="fancy_grid")
            print(table)
            return x_next

        x0 = x_next

        iterations += 1

    table = tabulate(TABLE_DATA, headers="firstrow", tablefmt="fancy_grid")
    print(table)

    raise Exception(f"Could not find the root after {max_iterations} iterations!")
