import matplotlib.pyplot as plt

from methods.simple_iteration import simple_iteration_method
from util.functions import *
from methods.secant_method import *
from methods.bisectional_method import *


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

METHODS = [bisection_method, secant_method, simple_iteration_method]

print("<input>")

f = Function(choose_function())
m = choose_method(METHODS)
a, b     = choose_interval_borders()
e        = choose_epsilon()
print("<input> [end]")

x = np.linspace(a, b, 100)
y = eval(str(f))

a, b = check_interval(f, a, b)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x)')
plt.grid(True)
plt.show()

m(f, a, b, e)
