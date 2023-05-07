# Function-Analysis-Tool
Python tool for analysis of mathematical functions.

This is a Python app that allows you to analyze mathematical functions by plotting the graph and identifying various characteristics such as intercepts, asymptotes, extrema, and inflection points.

## Requirements

* Python 3.x
* NumPy
* Matplotlib
* SymPy

## How to Use

1. Clone the repository or download the files.
2. Install the required libraries using `pip`.
3. Run the `function_analysis.py` file.
4. Enter your desired function and the variable you want to analyze.
5. Enter the lower and upper bounds of your desired interval.
6. The app will plot the graph of the function and label any intercepts, asymptotes, extrema, and inflection points it finds within the specified interval.

## Functions

The app uses the following methods to analyze the function:

* `find_x_intercepts(f)`: Uses the solve method from sympy to find the roots of the function `f` and returns only the real solutions.
* `find_y_intercepts(f, var)`: Evaluates the function `f` at x = 0 to find the y-intercept of the function. It returns None if the y-intercept is not real.
* `find_horizontal_asymptotes(f, var)`: Uses the `limit` method from sympy to find the horizontal asymptotes of the function `f`. It returns a set of horizontal asymptotes.
* `find_vertical_asymptotes(f, var)`: Uses the `solve` method from sympy to find the vertical asymptotes of the function `f`. It then uses the `limit` method to check if the function approaches infinity or negative infinity at those points. It returns a set of vertical asymptotes.
* `find_relative_extrema(f, var)`:  Finds the critical points of the function `f` by setting its derivative equal to zero. It then evaluates the sign of the first derivative of `f` at points around each critical point to determine whether the point is a maximum or minimum. It returns a list of tuples that contain the type of extrema, the x-coordinate of the extremum, and the y-coordinate of the extremum.
* `find_inflection_points(f, var)`: Finds the critical points of the second derivative of `f`. It then evaluates the sign of the second derivative of `f` at points around each critical point to determine whether the point is an inflection point. It returns a list of tuples that contain the x-coordinate and y-coordinate of each inflection point.


## Example

Here is an example of how to use the app:
```
Please enter your variable of choice: x
Please enter the equation you want to analyse: x**3 - 3*x
Please enter the lower bound of your desired interval: -5
Please enter the upper bound of your desired interval: 5
```
The app will plot the graph of f(x) = x^3 - 3x and label the x-intercepts, y-intercept, asymptotes, and inflection points within the interval (-5, 5).
![Figure_1](https://user-images.githubusercontent.com/114011447/236684561-5cd61c96-2241-47e0-922b-f2849c10a8df.png)

