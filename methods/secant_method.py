import sympy as sp

from tabulate import tabulate
from functions import check_derivative_sign


TABLE_DATA = [["x_(i-1)", "x_(i)", "x_(i+1)", "f(x_(i+1))", "|x_(i+1) - x_(i)|"]]


def secant_method(f, a, b, epsilon, max_iterations=50):  # TODO estimate the number of iterations
    """
    secant method for finding the approximate value of the root of the equation
    :param f: function
    :param a: left border of interval
    :param b: right border of interval
    :param epsilon: accuracy
    :param max_iterations: if we can't find the root after n iterations, we'll say
    that the equation has no solution
    :return: root :>
    """

    """
    firstly, let's define initial approximation

    x_0 = a_0 => if f(a_0) * f''(a_0) > 0
        = b_0 => if f(b_0) * f''(b_0) > 0
    """

    x = sp.symbols('x')
    f_string = str(f)
    f_prime = sp.diff(f_string, x)
    f_double_prime = sp.diff(f_prime, x)

    print("Let's choose x_0:")

    if f(a) * f_double_prime.subs(x, a) > 0:
        print(f"Equation: f(a) * f''(a) = {f(a)} * {f_double_prime.subs(x, a)} => x_0 = a")
        x0 = a
    elif f(b) * f_double_prime.subs(x, b) > 0:
        print(f"Equation: f(b) * f''(b) = {f(b)} * {f_double_prime.subs(x, b)} => x_0 = b")
        x0 = b
    else:
        raise Exception("Unable to determine initial approximation!")

    """
    secondly, let's check convergence conditions

    1) The sign of the derivative f'(x) must not change in [a, b]
    2) The sign of the derivative f''(x) must not change in [a, b]
    3) f'(x) != 0
    """

    necessity_1 = check_derivative_sign(f, a, b)
    # necessity_2 = derivative_not_zero_on_interval(f, a, b)

    if necessity_1:
        print("The convergence conditions = TRUE!")

        default_h = 0.005
        h = input("Enter the value for h: ") or default_h

        """
        criterion for ending the iteration process:
        |x_n - x_n-1| <= ε OR |f(x_n)| <= ε
        """

        if x0 == a:
            x1 = x0 + float(h)
        else:
            x1 = x0 - float(h)

        iteration = 1
        while iteration < max_iterations:

            if abs(x1 - x0) <= epsilon or abs(f(x1)) <= epsilon:
                print(f"abs(x1 - x0) = {abs(x1 - x0)}")
                print(f"f(x1) = {abs(f(x1))}")
                print(f"The root was found in {iteration} iterations")
                print(f"Root ≈ {x1}")
                print(tabulate(TABLE_DATA, headers="firstrow", tablefmt="fancy_grid"))
                return x1

            x_next = x1 - ((x1 - x0) / (f(x1) - f(x0))) * f(x1)  # TODO check for non zero division

            TABLE_DATA.append([x0, x1, x_next, f(x_next), abs(x_next - x1)])

            x0 = x1
            x1 = x_next

            iteration += 1

        table = tabulate(TABLE_DATA, headers="firstrow", tablefmt="fancy_grid")
        print(table)

        raise Exception(f"Could not find the root after {max_iterations} iterations!")
    else:
        raise Exception("The convergence conditions = FALSE!")
