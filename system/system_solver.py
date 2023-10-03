import inspect
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

from sympy import symbols, diff, sympify
from scipy.optimize import minimize


def transform_system(system, gx1, gy1, gx2, gy2):
    x, y = symbols('x y')
    
    func_1 = system[0]
    func_2 = system[1]
    
    derivative1_x = diff(func_1, x)
    derivative1_y = diff(func_2, y)

    derivative2_x = diff(func_1, x)
    derivative2_y = diff(func_2, y)

    import scipy.optimize as optimize

    # Define the objective functions for each derivative
    def objective_f1_x(point):
        x_value, y_value = point
        return -derivative1_x.subs([(x, x_value), (y, y_value)])

    def objective_f1_y(point):
        x_value, y_value = point
        return -derivative1_y.subs([(x, x_value), (y, y_value)])

    def objective_f2_x(point):
        x_value, y_value = point
        return -derivative2_x.subs([(x, x_value), (y, y_value)])

    def objective_f2_y(point):
        x_value, y_value = point
        return -derivative2_y.subs([(x, x_value), (y, y_value)])

    # Define the interval for optimization
    interval = [(gx1, gy1), (gx2, gy2)]

    # Find the maximum value for each derivative
    max_f1_x = optimize.minimize_scalar(objective_f1_x, bounds=interval)
    max_f1_y = optimize.minimize_scalar(objective_f1_y, bounds=interval)
    max_f2_x = optimize.minimize_scalar(objective_f2_x, bounds=interval)
    max_f2_y = optimize.minimize_scalar(objective_f2_y, bounds=interval)

    # Print the maximum values
    print("Maximum value for f1_x:", -max_f1_x.fun)
    print("Maximum value for f1_y:", -max_f1_y.fun)
    print("Maximum value for f2_x:", -max_f2_x.fun)
    print("Maximum value for f2_y:", -max_f2_y.fun)
    
    # lambda1 = - 1 / (max(max_derivative1_x, max_derivative1_y))
    # lambda2 = - 1 / (max(max_derivative2_x, max_derivative2_y))
    #
    # print(f"[1] We got a lambda equal to = {lambda1}")
    # print(f"[1] φ(x, y) = x + {lambda1} * ({inspect.getsource(func_1)})")
    #
    # print(f"[2] We got a lambda equal to = {lambda2}")
    # print(f"[2] φ(x, y) = y + {lambda2} * ({inspect.getsource(func_2)})")
    #
    # phi_func_1 = f"x + {lambda1} * ({inspect.getsource(func_1)})"
    # phi_func_2 = f"y + {lambda2} * ({inspect.getsource(func_2)})"
    #
    # return phi_func_1, phi_func_2


def convergence_condition(phi_func_1, phi_func_2, gx1, gy1, gx2, gy2) -> bool:
    x, y = symbols('x y')
    
    expr1 = sympify(phi_func_1)    
    expr2 = sympify(phi_func_2)    
    
    derivative_x1 = diff(expr1, x)
    derivative_y1 = diff(expr1, y)
    
    derivative_x2 = diff(expr2, x)
    derivative_y2 = diff(expr2, y)
    
    right_der_x1 = derivative_x1.subs([(x, gx2), (y, gy2)])
    right_der_x2 = derivative_x2.subs([(x, gx2), (y, gy2)])
    
    right_der_y1 = derivative_y1.subs([(x, gx2), (y, gy2)])
    right_der_y2 = derivative_y2.subs([(x, gx2), (y, gy2)])
    
    cond_1 = abs(right_der_x1) + abs(right_der_y1) < 1
    cond_2 = abs(right_der_x2) + abs(right_der_y2) < 1
    
    if cond_1 and cond_2:
        print("The convergence condition is OK!")
        return True
    elif cond_1:
        print(f"{abs(right_der_x2)} + {abs(right_der_y2)} < 1!")
        return False
    elif cond_2:
        print(f"{abs(right_der_x1)} + {abs(right_der_y1)} < 1!")
        return False
    else:
        print("The convergence condition is NOT OK!")
        return False
            
           
def choose_G_area(system):
    
    """
    :param system: list of string equations [2 equations]
    :return: x, y, which form a square area G
    """
    
    # a = float(input("Left side of graph interval [a]: "))
    # b = float(input("Right side of graph interval [b]: "))
    #
    # x = np.linspace(a, b, 100)
    #
    # func_1 = sp.lambdify((x, y), system[0])
    # func_2 = system[1]
    #
    # plt.plot(x, func_1(x))
    # plt.plot(x, func_2(x))
    #
    # plt.grid(True)
    # plt.show()
    
    gx1 = float(input("Choose g_x1: "))
    gx2 = float(input("Choose g_x2: "))
    gy1 = float(input("Choose g_y1: "))
    gy2 = float(input("Choose g_y2: "))
    
    print(f"{gx1} < x < {gx2}")
    print(f"{gy1} < y < {gy2}")

    return gx1, gy1, gx2, gy2 
    
    
def solve(phi_system, gx1, gy1, gx2, gy2):
    x0 = float(input("Initial approximation x0: "))
    y0 = float(input("Initial approximation y0: "))
    
    e = float(input("ε: "))
    
    max_iteration = 1080
    
    x, y = symbols('x y')
    
    expr1 = sympify(phi_system[0])
    expr2 = sympify(phi_system[1])
    
    x0_next = expr1.subs({x: x0, y: y0})
    y0_next = expr1.subs({x: x0, y: y0})
    
    iteration = 1
    while iteration < max_iteration:
        x0 = x0_next
        y0 = y0_next
        
        x0_next = expr1.subs({x: x0, y: y0})
        y0_next = expr1.subs({x: x0, y: y0})
        
        temp = max(abs(x0_next - x0), abs(y0_next - y0))
        
        if temp <= e:
            print(f"The iteration process is complete in {iteration}!")
            print(f"Roots = {x0_next} and {y0_next}")
        else:
            iteration += 1

