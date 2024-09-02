# def f(x):
#     """
#     Function for which we are finding the root.
#     f(x) = x^2 - 11
#     """
#     return x**2 - 11

# def bisection_method(a, b, tol):
#     """
#     Finds the root of the function f(x) using the bisection method and prints iteration details.
    
#     Parameters:
#     a : float
#         The lower bound of the interval.
#     b : float
#         The upper bound of the interval.
#     tol : float
#         The tolerance for the convergence criteria.
        
#     Returns:
#     float
#         The approximate root of the function.
#     """
#     if f(a) * f(b) > 0:
#         raise ValueError("No root found in the interval; f(a) and f(b) must have opposite signs.")
    
#     iteration = 0
#     previous_midpoint = None
#     print(f"{'Iteration':<10}{'a':<20}{'b':<20}{'Midpoint':<20}{'Epsilon (%)':<20}{'f(Midpoint)'}")
#     print("-" * 90)

#     while (b - a) / 2.0 > tol:
#         midpoint = (a + b) / 2.0
#         epsilon = 0
#         if previous_midpoint is not None:
#             epsilon = abs((midpoint - previous_midpoint) / midpoint) * 100
        
#         # Print the current iteration details
#         print(f"{iteration:<10}{a:<20.10f}{b:<20.10f}{midpoint:<20.10f}{epsilon:<20.10f}{f(midpoint):.10f}")
        
#         if f(midpoint) == 0:
#             print(f"\nExact root found: {midpoint}")
#             return midpoint
#         elif f(a) * f(midpoint) < 0:
#             b = midpoint
#         else:
#             a = midpoint
        
#         previous_midpoint = midpoint
#         iteration += 1
    
#     print(f"\nApproximate root after {iteration} iterations: {midpoint}")
#     return midpoint

# # Example usage
# try:
#     root = bisection_method(-1, 5, 0.00001)
#     print(f"\nRoot found: {round(root, 3)}")
# except ValueError as e:
#     print(e)


            #                                       || BISECTION METHOD with graphs ||

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    Function for which we are finding the root.
    f(x) = x^2 - 11
    """
    return x**2 - 11

def bisection_method(a, b, tol):
    """
    Finds the root of the function f(x) using the bisection method and plots the iterations.
    
    Parameters:
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    tol : float
        The tolerance for the convergence criteria.
        
    Returns:
    float
        The approximate root of the function.
    """
    if f(a) * f(b) > 0:
        raise ValueError("No root found in the interval; f(a) and f(b) must have opposite signs.")
    
    iteration = 0
    previous_midpoint = None
    midpoints = []
    a_values = [a]
    b_values = [b]
    
    # Initialize plot
    plt.figure(figsize=(12, 8))
    x = np.linspace(a - 2, b + 2, 400)
    plt.plot(x, f(x), label="f(x) = x^2 - 11", color='blue')
    
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        epsilon = 0
        if previous_midpoint is not None:
            epsilon = abs((midpoint - previous_midpoint) / midpoint) * 100
        
        # Collect midpoints and interval bounds for plotting
        midpoints.append(midpoint)
        a_values.append(a)
        b_values.append(b)
        
        # Print iteration details
        print(f"Iteration {iteration}: a = {a:.6f}, b = {b:.6f}, Midpoint = {midpoint:.6f}, f(Midpoint) = {f(midpoint):.6f}, Epsilon = {epsilon:.6f}%")
        
        if f(midpoint) == 0:
            print(f"Exact root found: {midpoint}")
            plt.scatter(midpoint, f(midpoint), color='red', zorder=5, label='Root')
            break
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        
        previous_midpoint = midpoint
        iteration += 1
    
    # Final midpoint plot
    plt.scatter(midpoint, f(midpoint), color='red', zorder=5, label='Root')
    plt.scatter(a_values, [f(val) for val in a_values], color='green', marker='x', label='a values')
    plt.scatter(b_values, [f(val) for val in b_values], color='purple', marker='o', label='b values')
    plt.scatter(midpoints, [f(val) for val in midpoints], color='orange', marker='s', label='Midpoints')
    
    # Add annotations for the initial interval and the midpoint
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method Iterations')
    plt.legend()
    plt.grid(True)
    
    # Add text annotations for key points
    for i in range(len(midpoints)):
        plt.annotate(f'{midpoints[i]:.2f}', (midpoints[i], f(midpoints[i])), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='orange')
    
    plt.show()
    
    print(f"\nApproximate root after {iteration} iterations: {midpoint:.6f}")
    return midpoint

# Example usage
try:
    root = bisection_method(-1, 5, 0.0001)
    print(f"\nRoot found: {round(root, 3)}")
except ValueError as e:
    print(e)
