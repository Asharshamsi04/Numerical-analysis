import numpy as np

def fixed_point_iteration(g, x0, tolerance=1e-6, max_iterations=100):
    """
    Perform fixed point iteration.
    
    Parameters:
    g : function
        The function g(x) used for iteration.
    x0 : float
        The initial guess.
    tolerance : float
        The convergence tolerance.
    max_iterations : int
        Maximum number of iterations.

    Returns:
    float
        The approximate fixed point.
    """
    x_n = x0
    for n in range(max_iterations):
        x_n1 = g(x_n)  # Compute the next approximation
        
        print(f"Iteration {n + 1}: x_n = {x_n:.6f}, g(x_n) = {x_n1:.6f}")
        
        # Check for convergence
        if abs(x_n1 - x_n) < tolerance:
            print(f"Converged to {x_n1:.6f} after {n + 1} iterations.")
            return x_n1
        
        x_n = x_n1

    print("Did not converge.")
    return None

# Example function g(x) = (x^3-x-1)
def g(x):
    return x**3-x-1

# Example usage
x0 = 1  # Initial guess
result = fixed_point_iteration(g, x0)

if result is not None:
    print(f"Fixed point: {result:.6f}")
