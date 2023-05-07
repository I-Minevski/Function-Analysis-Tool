import sympy as sp


def find_x_intercepts(f):
    """
        Finds the x-intercepts of a function f.

        Args:
            f: sympy expression, the function whose x-intercepts to find.

        Returns:
            A list of real numbers representing the x-intercepts of the function.
    """

    # Solve for all the real roots of f(x).
    x_intercepts = [num for num in sp.solve(f) if num.is_real]
    return x_intercepts


def find_y_intercepts(f, x):
    """
        Finds the y-intercept of a function f.

        Args:
            f: sympy expression, the function whose y-intercept to find.
            x: sympy symbol, the variable in f.

        Returns:
            A real number representing the y-intercept of the function, if it exists.
    """

    # Evaluate the function at x=0 to find the y-intercept.
    if f.subs(x, 0).is_real:
        y_intercept = f.subs(x, 0)
        return y_intercept


def find_horizontal_asymptotes(f, x):
    """
        Finds the horizontal asymptotes of a function f.

        Args:
            f: sympy expression, the function whose horizontal asymptotes to find.
            x: sympy symbol, the variable in f.

        Returns:
            A set of real numbers representing the horizontal asymptotes of the function.
    """

    # Find the limits of the function as x approaches positive and negative infinity.
    horizontal_asymptotes = [sp.limit(f, x, sp.oo), sp.limit(f, x, -sp.oo)]

    # Filter out any infinities.
    return {a for a in horizontal_asymptotes if a.is_number and a.is_real}


def find_vertical_asymptotes(f, x):
    """
        Finds the vertical asymptotes of a function f.

        Args:
            f: sympy expression, the function whose vertical asymptotes to find.
            x: sympy symbol, the variable in f.

        Returns:
            A set of real numbers representing the vertical asymptotes of the function.
    """

    # Find the points where the denominator of f(x) is zero.
    va_points = [a for a in sp.solve(sp.denom(f))]
    vertical_asymptotes = []

    # Check if the limit of the function as x approaches each vertical asymptote is infinite.
    for point in va_points:
        if sp.limit(f, x, point) == sp.oo or sp.limit(f, x, point) == -sp.oo:
            vertical_asymptotes.append(point)

    # Filter out any infinities.
    return {a for a in vertical_asymptotes if a != sp.oo and a != -sp.oo}


def find_relative_extrema(f, x, eps=1e-6, max_iter=100):
    """
    Finds the relative extrema of a function.

    Args:
        f: sympy expression
            The function to find extrema of.
        x: sympy symbol
                The independent variable of the function.
        eps: float, optional
            The distance from a critical point to evaluate the function at. Defaults to 1e-6.
        max_iter: int, optional
            The maximum number of iterations to use when searching for extrema. Defaults to 100.

    Returns:
        A list of tuples representing the relative extrema of the function. Each tuple contains three elements:
            - The type of extremum ('max' or 'min')
            - The x-coordinate of the extremum
            - The y-coordinate of the extremum
    """

    # Calculate the first derivative of the function.
    f_prime = sp.diff(f, x)

    # Find critical points by setting f'(x) = 0
    critical_points = sp.solve(f_prime, x)

    # Evaluate the first derivative at points around critical points
    extrema = []
    for point in critical_points:
        if not point.is_real:
            continue

        i = 0
        while i < max_iter:
            f_left = f_prime.subs(x, point - eps * (i + 1))
            f_right = f_prime.subs(x, point + eps * (i + 1))

            # If the sign of first derivative changes from positive to negative,
            # there is a relative maximum at this point
            if f_left > 0 and f_right < 0:
                extrema.append(('max', point, f.subs(x, point)))
                break

            # If the sign of first derivative changes from negative to positive,
            # there is a relative minimum at this point
            elif f_left < 0 and f_right > 0:
                extrema.append(('min', point, f.subs(x, point)))
                break
            i += 1

    return extrema


def find_inflection_points(f, x, eps=1e-6, max_iter=100):
    """
        Find the inflection points of a function.

        Args:
            f: sympy expression
                The function to find the inflection points of.
            x: sympy symbol
                The independent variable of the function.
            eps: float, optional
                The small interval around the critical points to evaluate the second derivative at.
            max_iter: int, optional
                The maximum number of iterations to try to find an inflection point at a critical point.

        Returns:
            list of tuples
                A list of tuples representing the inflection points. Each tuple contains two elements:
                the x-coordinate of the inflection point and the y-coordinate of the inflection point.
    """

    # Calculate second derivative
    f_double_prime = sp.diff(f, x, 2)

    # Find critical points by setting f''(x) = 0
    critical_points = sp.solve(f_double_prime, x)
    inflection_points = []

    for point in critical_points:
        if not point.is_real:
            continue

        sign_changes = 0
        i = 0
        while i < max_iter:
            # Evaluate second derivative at points around critical point
            f_left = f_double_prime.subs(x, point - eps * (i + 1))
            f_right = f_double_prime.subs(x, point + eps * (i + 1))

            # Check for sign changes in the second derivative
            if f_left > 0 and f_right < 0:
                sign_changes += 1
                if sign_changes == 2:
                    inflection_points.append((point, f.subs(x, point)))
                    break
            elif f_left < 0 and f_right > 0:
                sign_changes += 1
                if sign_changes == 2:
                    inflection_points.append((point, f.subs(x, point)))
                    break
            i += 1

    return [ip for ip in inflection_points]