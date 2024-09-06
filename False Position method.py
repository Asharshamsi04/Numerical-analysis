
# import math
# import numpy as np

# def f(x):
#     """
#     Function for which we are finding the root.
#     f(x) = math.exp(x) - 3 * x
#     """
#     return np.exp(x) - 3 * x

# def false_position_method(a, b, tol, max_iter=100):
#     """
#     Finds the root of the function f(x) using the False Position Method and prints
#     iteration details.

#     Parameters:
#     a : float
#         The lower bound of the interval.
#     b : float
#         The upper bound of the interval.
#     tol : float
#         The tolerance for the convergence criteria.
#     max_iter : int
#         The maximum number of iterations (default is 100).

#     Returns:
#     float
#         The approximate root of the function.
#     """

#     if f(a) * f(b) >= 0:
#         raise ValueError("No root found in the interval; f(a) and f(b) must have opposite signs.")

#     iteration = 0
#     previous_c = None

#     print(f"{'Iteration':<10}{'a':<20}{'b':<20}{'c':<20}{'Epsilon (%)':<20}{'f(c)'}")
#     print("-" * 90)

#     while iteration < max_iter:
#         # Calculate the point c where the function is zero
#         c = b - (f(b) * (b - a)) / (f(b) - f(a))
#         epsilon = 0
#         if previous_c is not None:
#             epsilon = abs((c - previous_c) / c) * 100

#         # Print the current iteration details
#         print(f"{iteration:<10}{a:<20.10f}{b:<20.10f}{c:<20.10f}{epsilon:<20.10f}{f(c):.10f}")

#         if abs(f(c)) < tol:
#             print(f"\nApproximate root found: {c}")
#             return c
#         elif f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c

#         previous_c = c
#         iteration += 1

#     print(f"\nApproximate root after {iteration} iterations: {c}")
#     return c

# # Example usage

# root = false_position_method(1, 2, 0.0001)
# print(f"\nRoot found: {round(root, 3)}")



##                       ||| FALSE POSITION METHOD WITH GRAPH  |||
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    Function for which we are finding the root.
    f(x) = math.exp(x) - 3 * x
    """
    return np.exp(x) - 3 * x  # Element-wise operations (assuming x is a NumPy array)

def false_position_method(a, b, tol, max_iter=100):
    """
    Finds the root of the function f(x) using the False Position Method and prints
    iteration details. Also plots the function and the approximation steps.

    Parameters:
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    tol : float
        The tolerance for the convergence criteria.
    max_iter : int
        The maximum number of iterations (default is 100).

    Returns:
    float
        The approximate root of the function.
    """

    if f(a) * f(b) >= 0:  # Ensures opposite signs at endpoints
        raise ValueError("No root found in the interval; f(a) and f(b) must have opposite signs.")

    iteration = 0
    previous_c = None
    c_values = []  # Store the values of c for plotting

    # Set up plot
    x = np.linspace(min(a, b) - 1, max(a, b) + 1, 400)  # Adjust plot range for exp(x)
    y = f(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x) = exp(x) - 3x', color='blue')  # Update label
    plt.axhline(0, color='black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')

    print(f"{'Iteration':<10}{'a':<20}{'b':<20}{'c':<20}{'Epsilon (%)':<20}{'f(c)'}")
    print("-" * 90)

    while iteration < max_iter:
        # Calculate the point c where the function is zero
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        epsilon = 0
        if previous_c is not None:
            epsilon = abs((c - previous_c) / c) * 100

        # Print the current iteration details
        print(f"{iteration:<10}{a:<20.10f}{b:<20.10f}{c:<20.10f}{epsilon:<20.10f}{f(c):.10f}")

        # Plot the approximation point
        plt.scatter(c, f(c), color='red', zorder=5, label=f"Iteration {iteration}")

        if abs(f(c)) < tol:
            print(f"\nApproximate root found: {c}")
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        previous_c = c
        iteration += 1

    plt.title('False Position Method Iterations')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"\nApproximate root after {iteration} iterations: {c}")
    return c

# Example usage
try:
    root = false_position_method(1, 2, 0.0001)
    print(f"\nRoot found: {round(root, 3)}")
except ValueError as e:
    print(e)
