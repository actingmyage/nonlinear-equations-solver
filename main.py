from functions import *
from util import *
from methods import *


def lab_info():
    lab_name = "Laboratory work №2"
    author = "Chesnokov Arkady"
    description = """
    study numerical methods for solving nonlinear equations and their systems,
    find the roots of a given nonlinear equation/system of nonlinear equations,
    complete the software implementation of the methods.
    """

    print("=" * 50)
    print(f"{'Lab Info':^50}")
    print("=" * 50)
    print(f"Title: {lab_name}")
    print(f"Author: {author}")
    print("-" * 50)
    print(f"Description: {description}")
    print("=" * 50)


lab_info()

print("<input>")

f = Function(choose_function())
a, b     = choose_interval_borders()
e        = choose_epsilon()

print("<input> [end]")

a, b = check_interval(f, a, b)

check_derivative_sign(f, a, b)
