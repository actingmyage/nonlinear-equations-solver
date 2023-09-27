import matplotlib.pyplot as plt
import numpy as np


def plot_graph(f, f_title, a, b):
    x = np.linspace(a - 3, b + 3, 30)  # graph covers more than the interval
    y = f(x)

    print("let's build function graph!")

    print("<SET OF POINTS FOR A FUNCTION>")
    for i in range(len(x)):
        print(f"x: {x[i]}, y: {y[i]}")

    print("<SET OF POINTS FOR A FUNCTION> [END]")

    plt.plot(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # TODO how it works?
    major_ticks = np.arange(a-100, b+100, 20)
    minor_ticks = np.arange(a-100, b+100, 5)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title("Graph of function f(x) = " + str(f_title))

    plt.grid(True, 'both', 'both', color='r', linestyle=':', )
    plt.show()
