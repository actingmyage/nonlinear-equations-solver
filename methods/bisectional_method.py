from tabulate import tabulate

TABLE_DATA = [["a", "b", "x", "f(a)", "f(b)", "f(x)", "|a-b|"]]


def bisection_method(f, a, b, epsilon) -> float:
    """
    The bisection method for finding the root of an equation.

    :param f: function = f(x)
    :param a: left border of the interval
    :param b: right border of the interval
    :param epsilon: accuracy
    :return: root of equation
    """

    """
    pros: simple and reliable, has absolute convergence
    cons: too slow, if the interval contains several roots, it is unknown which root it will find :>
    convergence: linear convergence
    """

    iterations = 1
    while abs(b - a) > epsilon:
        x0 = (a + b) / 2

        solution = f(x0)
        iterations += 1

        TABLE_DATA.append([a, b, x0, f(a), f(b), f(x0), abs(a - b)])

        if abs(solution) <= epsilon:
            print("Root was found in " + str(iterations) + " iterations!")
            print(f"Root ≈ {x0}")

            table = tabulate(TABLE_DATA, headers="firstrow", tablefmt="fancy_grid")
            print(table)

            return solution

        if f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0

    table = tabulate(TABLE_DATA, headers="firstrow", tablefmt="fancy_grid")
    print(table)

    print(f"Since |b - a| < epsilon => cycle ended. It took {iterations} iterations!")

    solution = (a + b) / 2
    print(f"Returning (a_last + b_last) / 2. It's equals {solution}")

    return (a + b) / 2
