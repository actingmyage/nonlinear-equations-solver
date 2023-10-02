import numpy as np
from scipy.optimize import minimize_scalar


def equation_1(x1, x2):
    return 0.1 * x1 ** 2 + x1 + 0.2 * x2 ** 2 - 0.3


def equation_2(x1, x2):
    return 0.2 * x1 ** 2 + x2 + 0.1 * x1 * x2 - 0.7


def phi_1(x1, x2):
    return 0.3 - 0.1 * x1 ** 2 - 0.2 * x2 ** 2


def phi_2(x1, x2):
    return 0.7 - 0.2 * x1 ** 2 - 0.1 * x1 * x2


def d_phi_11(x1):
    return -0.2 * x1


def d_phi_12(x2):
    return -0.4 * x2


def d_phi_21(x1, x2):
    return -0.4 * x1 - 0.1 * x2


def d_phi_22(x1):
    return -0.1 * x1


SYSTEMS = [
    [[equation_1, equation_2], [phi_1, phi_2], []]
]


def system_simple_iteration_method(sys, epsilon):
    print("determine the square in which the equation will be located")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))



