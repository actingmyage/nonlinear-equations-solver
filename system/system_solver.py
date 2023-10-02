import numpy as np
import scipy as sp

from util.functions import Function


def check_convergence_jacobian(jacobian_matrix):
    eigenvalues = np.linalg.eigvals(jacobian_matrix)
    if np.all(np.abs(eigenvalues) < 1):
        return True
    else:
        return False


def get_J(system):
    x, y = sp.symbols('x y')
    f = sp.Matrix([system[0], system[1]])
    J = f.jacobian([x, y])
    print(J)
    return J


def equation_1(x, y):
    return Function(x ** 2 + y ** 2 - 1)


def equation_2(x, y):
    return Function(x ** 2 - y - 0.5)


def equation_3(x, y):
    return Function(x - y ** 2)


system_1 = [equation_1, equation_2]
system_2 = [equation_1, equation_3]


def apply_phi(system, a, b):

    for i in range(len(system)):
        f = system[i]

        x_sym = sp.symbols('x')
        f_string = str(f)
        f_prime = sp.diff(f_string, x_sym)
        interval_values = np.linspace(a, b, 1000)
        derivative_values = [f_prime.subs(x_sym, val) for val in interval_values]
        max_derivative = max(derivative_values)
        lam = - (1 / max_derivative)

        print(f"We got a lambda equal to = {lam}")
        print(f"φ(x) = x + {lam} * ({str(f)})")

        system[i] = lambda x, y: x + lam + f(x, y)

    return system


def system_solve(system, a, b, e):
    phi_system = apply_phi(system, a, b)
    J = get_J(phi_system)

    if check_convergence_jacobian(J):
        print("The simple iteration method converges!")
    else:
        raise Exception("The simple iteration method does not converge!")

    # x0, y0
    x, y = 0, 0

