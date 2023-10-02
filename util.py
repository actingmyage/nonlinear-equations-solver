from functions import FUNCTIONS


def choose_function():
    print("<Choose equation!>")

    for i in range(len(FUNCTIONS)):
        number_of_function = str(i + 1)
        print('[' + number_of_function + '] ' + FUNCTIONS[i] + "\n")

    choice = int(input("choice: ")) - 1
    function = FUNCTIONS[choice]

    return function


def choose_method(methods: list):
    print("<Choose method!>")

    for i in range(len(methods)):
        number_of_method = str(i + 1)
        print(f"[{number_of_method}] {methods[i].__name__}")

    choice = int(input("choice: ")) - 1
    method = methods[choice]

    return method


def choose_interval_borders():  # TODO if the root does not exist on this interval, change the interval
    print("<Choose interval borders!>")

    borders = input("a b: ").split()
    a = float(borders[0])
    b = float(borders[1])

    return a, b


def choose_epsilon():
    print("<Choose epsilon!>")

    epsilon = float(input("ε: "))
    return epsilon
