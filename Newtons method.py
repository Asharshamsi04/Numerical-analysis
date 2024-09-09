# import numpy as np

# # Define the function and its derivative
# def func(x):
#     return np.cos(x) - x * np.exp(x)

# def derivFunc(x):
#     return -np.sin(x) - np.exp(x) - x * np.exp(x)

# def newton_method(x0, tol=1e-6, max_iter=1000):
#     x = x0
#     for i in range(max_iter):
#         f_x = func(x)
#         df_x = derivFunc(x)
        
#         if df_x == 0:
#             print("Derivative is zero. Newton's method fails.")
#             return None
        
#         h = f_x / df_x
#         x = x - h
        
#         # Print iteration details
#         print(f"Iteration {i+1}: x = {x}, f(x) = {func(x)}")
        
#         if abs(h) < tol:
#             print(f"Convergence reached: x = {x}")
#             return x
    
#     print("Maximum iterations reached without convergence.")
#     return None

# # Initial guess
# x0 = 100
# root = newton_method(x0)
# if root is not None:
#     print(f"Root found: {root}")
# else:
#     print("No root found.")



#                                           ||| NEWTON'S METHOD WITH GRAPH  |||


import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
def func(x):
    return np.cos(x) - x * np.exp(x)

def derivFunc(x):
    return -np.sin(x) - np.exp(x) - x * np.exp(x)

def newton_method(x0, tol=1e-6, max_iter=1000):
    x = x0
    iterations = []
    values = []

    for i in range(max_iter):
        f_x = func(x)
        df_x = derivFunc(x)
        
        if df_x == 0:
            print("Derivative is zero. Newton's method fails.")
            return None, iterations, values
        
        h = f_x / df_x
        x = x - h
        
        # Store iteration details
        iterations.append(i+1)
        values.append(x)
        
        # Print iteration details
        print(f"Iteration {i+1}: x = {x}, f(x) = {func(x)}")
        
        if abs(h) < tol:
            print(f"Convergence reached: x = {x}")
            return x, iterations, values
    
    print("Maximum iterations reached without convergence.")
    return None, iterations, values

# Initial guess
x0 = 0

# Run Newton-Raphson
root, iterations, values = newton_method(x0)

if root is not None:
    print(f"Root found: {root}")
else:
    print("No root found.")

# Plotting
x = np.linspace(-2, 2, 400)
y = func(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = cos(x) - x * exp(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Plot iterations
if iterations:
    plt.scatter(values, [func(v) for v in values], color='red', zorder=5, label='Iterations')
    
    # Annotate each iteration point
    for i, val in enumerate(values):
        plt.annotate(f'Iter {i+1}', (val, func(val)), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='red')

# Highlight the root found
if root is not None:
    plt.scatter(root, func(root), color='green', zorder=10, label='Root')
    plt.annotate(f'Root: {root:.4f}', (root, func(root)), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='green')

plt.title('Newton's Method for Finding Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

