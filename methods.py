from util import *
from tabulate import tabulate

def bisection_method(f, a, b, epsilon):
    """
    The bisection method for finding the root of an equation.

    :param f: function = f(x)
    :param a: left border of the interval
    :param b: right border of the interval
    :param epsilon: accuracy
    :return: single solution, otherwise, if no such solution was found, a list consisting of a and b
    """

    """
    pros: simple and reliable, has absolute convergence
    cons: too slow, if the interval contains several roots, it is unknown which root it will find :>
    convergence: linear convergence
    """

    #TODO move the check outside the function
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the ends of the interval!")

    iterations = 1
    while abs(b - a) > epsilon:
        x0 = (a + b) / 2

        solution = f(x0)
        iterations += 1
        if abs(solution) <= epsilon:
            print("Root was found in " + str(iterations) + " iterations!")
            print("Root = " + str(solution))
            return solution

        if f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0

    print("Root was not found in " + str(iterations) + " iterations!")
    print("Returning (a_last + b_last) / 2. It's equals " + (a + b / 2))

    return (a + b) / 2
