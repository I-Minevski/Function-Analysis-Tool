import numpy as np
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
from analysis_methods import *


symbol = input("Please enter your variable of choice: ")
var = sp.symbols(symbol)

function = input("Please enter the equation you want to analyse: ")
f = parse_expr(function)

lower = float(input("Please enter the lower bound of your desired interval: "))
upper = float(input("Please enter the upper bound of your desired interval: "))

x_intercepts = find_x_intercepts(f)
y_intercept = find_y_intercepts(f, var)
horizontal_asymptotes = find_horizontal_asymptotes(f, var)
vertical_asymptotes = find_vertical_asymptotes(f, var)
extrema = find_relative_extrema(f, var)
inflection_points = find_inflection_points(f, var)

x_vals = np.linspace(lower, upper, 100)

y_vals = [f.subs(var, i) for i in x_vals]

plt.plot(x_vals, y_vals)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)

if x_intercepts:
    for intercept in x_intercepts:
        plt.plot(intercept, 0, 'ro', label=f'X-intercept in ({intercept};0)')

if y_intercept:
    plt.plot(0, y_intercept, 'ro', label=f'Y-intercept in (0;{y_intercept})')

if horizontal_asymptotes:
    for asymptote in horizontal_asymptotes:
        plt.axhline(y=asymptote, color='y', linestyle='--', label=f'Horizontal Asymptote: y = {asymptote}')

if vertical_asymptotes:
    for asymptote in vertical_asymptotes:
        plt.axvline(x=asymptote, color='m', linestyle='--', label=f'Vertical Asymptote: x = {asymptote}')

if extrema:
    for ext in extrema:
        if ext[0] == 'max':
            plt.plot(ext[1], ext[2], 'go', label=f'Relative Maximum in ({ext[1]};{ext[2]})')
        elif ext[0] == 'min':
            plt.plot(ext[1], ext[2], 'bo', label=f'Relative Minimum in ({ext[1]};{ext[2]})')

if inflection_points:
    for point in inflection_points:
        plt.plot(point[0], point[1], 'mo', label=f'Inflection Point in ({sp.simplify(point[0])};{point[1]})')

plt.title(f'Graph of {f}')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()