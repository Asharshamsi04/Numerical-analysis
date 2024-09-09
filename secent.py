# import numpy as np

# # Define the function
# def func(x):
#     return np.cos(x) - x * np.exp(x)

# def secant_method(x0, x1, tol=1e-6, max_iter=1000):
#     for i in range(max_iter):
#         f_x0 = func(x0)
#         f_x1 = func(x1)
        
#         if f_x1 == f_x0:
#             print("Division by zero in Secant method.")
#             return None
        
#         # Secant method formula
#         x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
#         if abs(x2 - x1) < tol:
#             print(f"Convergence reached: x = {x2}")
#             return x2
        
#         # Update for next iteration
#         x0, x1 = x1, x2
    
#     print("Maximum iterations reached without convergence.")
#     return None

# # Initial guesses
# x0 = 0
# x1 = 1

# # Run Secant Method
# root = secant_method(x0, x1)

# if root is not None:
#     print(f"Root found: {root}")
# else:
#     print("No root found.")


##                                         ||| SECENT METHOD WITH ITERATION TABLE |||

import numpy as np

# Define the function
def func(x):
    return np.cos(x) - x * np.exp(x)

def secant_method(x0, x1, tol=1e-6, max_iter=1000):
    iterations = []
    values = []
    
    for i in range(max_iter):
        f_x0 = func(x0)
        f_x1 = func(x1)
        
        if f_x1 == f_x0:
            print("Division by zero in Secant method.")
            return None, iterations, values
        
        # Secant method formula
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        # Store iteration details
        iterations.append(i + 1)
        values.append(x2)
        
        # Print iteration details
        print(f"Iteration {i+1}: x = {x2}, f(x) = {func(x2)}")
        
        if abs(x2 - x1) < tol:
            print(f"Convergence reached: x = {x2}")
            return x2, iterations, values
        
        # Update for next iteration
        x0, x1 = x1, x2
    
    print("Maximum iterations reached without convergence.")
    return None, iterations, values

# Initial guesses
x0 = 0
x1 = 1

# Run Secant Method
root, iterations, values = secant_method(x0, x1)

if root is not None:
    print(f"Root found: {root}")
else:
    print("No root found.")

# Display iteration table
print("\nIteration Table:")
print(f"{'Iteration':<10}{'x value':<20}{'f(x)'}")
print("-" * 40)

for iter_num, val in zip(iterations, values):
    print(f"{iter_num:<10}{val:<20.10f}{func(val):.10f}")


#             ||| SECENT METHOD WITH GRAPH |||


# import numpy as np
# import matplotlib.pyplot as plt

# # Define the function
# def func(x):
#     return np.cos(x) - x * np.exp(x)

# def secant_method(x0, x1, tol=1e-6, max_iter=1000):
#     iterations = []
#     values = []
    
#     for i in range(max_iter):
#         f_x0 = func(x0)
#         f_x1 = func(x1)
        
#         if f_x1 == f_x0:
#             print("Division by zero in Secant method.")
#             return None, iterations, values
        
#         # Secant method formula
#         x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
#         # Store iteration details
#         iterations.append(i+1)
#         values.append(x2)
        
#         # Print iteration details
#         print(f"Iteration {i+1}: x = {x2}, f(x) = {func(x2)}")
        
#         if abs(x2 - x1) < tol:
#             print(f"Convergence reached: x = {x2}")
#             return x2, iterations, values
        
#         # Update for next iteration
#         x0, x1 = x1, x2
    
#     print("Maximum iterations reached without convergence.")
#     return None, iterations, values

# # Initial guesses
# x0 = 0
# x1 = 1

# # Run Secant Method
# root, iterations, values = secant_method(x0, x1)

# if root is not None:
#     print(f"Root found: {root}")
# else:
#     print("No root found.")

# # Plotting
# x = np.linspace(-2, 2, 400)
# y = func(x)

# plt.figure(figsize=(10, 6))
# plt.plot(x, y, label='f(x) = cos(x) - x * exp(x)', color='blue')
# plt.axhline(0, color='black', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)

# # Plot iterations
# if iterations:
#     plt.scatter(values, [func(v) for v in values], color='red', zorder=5, label='Iterations')
    
#     # Annotate each iteration point
#     for i, val in enumerate(values):
#         plt.annotate(f'Iter {i+1}', (val, func(val)), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='red')

# # Highlight the root found
# if root is not None:
#     plt.scatter(root, func(root), color='green', zorder=10, label='Root')
#     plt.annotate(f'Root: {root:.4f}', (root, func(root)), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='green')

# plt.title('Secant Method for Finding Roots')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.grid(True)
# plt.show()
