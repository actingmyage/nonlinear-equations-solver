import time

from functions import FUNCTIONS


def print_load_stub():
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")


def choose_function():
    print("<Choose equation!>")

    for i in range(len(FUNCTIONS)):
        number_of_function = str(i + 1)
        print('[' + number_of_function + '] ' + FUNCTIONS[i][0] + "\n")

    choice = int(input("choice: ")) - 1
    function = FUNCTIONS[choice]

    return function


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
