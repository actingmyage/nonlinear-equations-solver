from tabulate import tabulate


def verify_interval(f, a, b):
    """
    Checks for the presence of a root at a given interval

    :param f: function
    :param a: left border of interval
    :param b: right border of interval
    :return:  interval containing roots or error message
    """

    if a >= b:
        raise Exception("Error: The left border of the interval must be less than the right border!")

    print("Checking the interval for the presence of roots...")

    if f(a) * f(b) > 0:
        fa = f(a)
        fb = f(b)

        print(str(fa) + " * " + str(f(b)) + " = " + str(fa * fb))
        print("=> f(a) * f(b) > 0!")

        delta = 0.0001

        warning = """
            We reduce the interval until we find the roots or until the difference between a and b becomes less than 
            Δ =    
        """ + str(delta)

        print(warning)

        number_of_decreases = 0
        while abs(b - a) > delta:
            a += delta
            b -= delta

            number_of_decreases += 1

            fa = f(a)
            fb = f(b)

            print(str(fa) + " * " + str(f(b)) + " = " + str(fa * fb))

            if f(a) * f(b) < 0:
                print("We have decreased the interval " + str(number_of_decreases) +
                      " times and found several roots [maybe several]")

                print("New borders: a = " + str(a) + ", b = " + str(b))
                return a, b

            elif f(a) * f(b) == 0:
                print("We have decreased the interval " + str(number_of_decreases) +
                      " times and found one root")

                print("New borders: a = " + str(a) + ", b = " + str(b))
                return a, b

        raise Exception("Error: There are no roots on this interval!")

    elif f(a) * f(b) == 0:
        fa = f(a)
        fb = f(b)

        print(str(fa) + " * " + str(f(b)) + " = " + str(fa * fb))
        print("There is one root on a given interval!")

        return a, b

    else:
        fa = f(a)
        fb = f(b)

        print(str(fa) + " * " + str(f(b)) + " = " + str(fa * fb))
        print("There are several roots on a given interval!")

        return a, b


def bisection_method(f, a, b, epsilon):
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

    # TODO move the check outside the function
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the ends of the interval!")

    table_data = [["a", "b", "x", "f(a)", "f(b)", "f(x)", "|a-b|"]]

    iterations = 1
    while abs(b - a) > epsilon:
        x0 = (a + b) / 2

        solution = f(x0)
        iterations += 1

        table_data.append([a, b, x0, f(a), f(b), f(x0), abs(a-b)])

        if abs(solution) <= epsilon:

            print("Root was found in " + str(iterations) + " iterations!")
            print("Root = " + str(solution))

            table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
            print(table)

            return solution

        if f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0

    table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
    print(table)

    print("Root was not found in " + str(iterations) + " iterations!")
    print("Returning (a_last + b_last) / 2. It's equals " + str((a + b) / 2))

    return (a + b) / 2
