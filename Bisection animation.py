import numpy as np
import matplotlib.pyplot as plt

# Define the function whose roots are required
def f(x):
    return (x**3) - 0.165 * (x**2) + 3.9993 * (10**(-4))

# Input Parameters
N = 50           # Max. number of iterations
eps = 5          # Acceptable Error (%) 
xl = 0           # Lower bound on the root
xu = 0.11        # Upper bound on the root

# Initialize figure for plotting
fig = plt.figure(figsize=(8, 8), dpi=120)

# Plot the given function
x = np.arange(xl - 0.5, xu + 0.5, 0.00001)
y = f(x)
plt.plot(x, y, linewidth=3)
plt.axhline(y=0, c='black', linewidth=1)

# Check if initial guesses bracket a root
if f(xl) * f(xu) >= 0:
    print("Bisection method fails.")
    plt.show()
    exit()

# Print the table header
print('------------------------------------------------------------------------------------------------')
print('iter \t\t xl \t\t xu \t\t xm \t\t Epsilon% \t f(xm)')
print('------------------------------------------------------------------------------------------------')

xm_list = []
Epsilon = [100]

for i in range(N):
    xm = (xl + xu) / 2
    xm_list.append(xm)

    # Plot the current iteration
    plt.title(f"Iteration #{i+1}\n\nxl = {xl:.8f}; xu = {xu:.8f}; xm = ?; f(xm) = ?")
    plt.xlabel('x')
    plt.ylabel('y')

    # Plot and annotate points
    plt.scatter(xl, f(xl), c='blue', s=250, alpha=0.5)
    plt.scatter(xu, f(xu), c='blue', s=250, alpha=0.5)
    plt.axvline(x=xl, c='blue', linewidth=2, alpha=0.5)
    plt.axvline(x=xu, c='blue', linewidth=2, alpha=0.5)
    plt.annotate('f(xl)', [xl, f(xl)])
    plt.annotate('f(xu)', [xu, f(xu)])
    plt.pause(2.0)

    # Update plot with xm point
    plt.title(f"Iteration #{i+1}\n\nxl = {xl:.8f}; xu = {xu:.8f}; xm = {xm:.8f}; f(xm) = {f(xm):.8f}")
    plt.annotate('f(xm)', [xm, f(xm)])
    plt.scatter(xm, f(xm), c='red', s=250, alpha=0.5)
    plt.axvline(x=xm, c='red', linewidth=2, alpha=0.5)
    plt.autoscale()
    plt.pause(2.0)

    # Compute Epsilon
    if f(xm) == 0:
        print(f'Root found: {xm}')
        plt.text(0.5, 0.5, f'Root found.\n\n Epsilon% = {np.round(Epsilon[i], 5)}\n\nRoot ≈ {np.round(xm, 7)}\n\nf(xm) ={f(xm)}', 
                 fontsize=16, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes,
                 bbox=dict(facecolor='papayawhip', alpha=0.6, edgecolor='papayawhip'))
        plt.pause(5.0)
        break
    elif i >= 1:
        Epsilon.append(abs((xm_list[i] - xm_list[i - 1]) / xm_list[i] * 100))
        print(f'{i+1}\t\t{xl: .8f}\t{xu: .8f}\t{xm: .8f}\t{Epsilon[i]: .8f}\t{f(xm): .8f}')
    else:
        print(f'{i+1}\t\t{xl: .8f}\t{xu: .8f}\t{xm: .8f}\t{Epsilon[0]: .8f}\t{f(xm): .8f}')

    # Update bounds based on function signs
    if f(xl) * f(xm) < 0:
        xu = xm
        plt.text(0.5, 0.2, 'f(xl) * f(xm) < 0\n\n xu = xm', fontsize=16, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes,
                 bbox=dict(facecolor='whitesmoke', alpha=0.5, edgecolor='whitesmoke'))
    else:
        xl = xm
        plt.text(0.5, 0.2, 'f(xm) * f(xu) < 0\n\n xl = xm', fontsize=16, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes,
                 bbox=dict(facecolor='whitesmoke', alpha=0.5, edgecolor='whitesmoke'))

    plt.scatter(xl, f(xl), c='yellow', s=175, alpha=1)
    plt.scatter(xu, f(xu), c='yellow', s=175, alpha=1)
    plt.pause(2.0)
    plt.clf()
    x = np.arange(xl - (xu - xl) / 2, xu + (xu - xl) / 2, 0.00001)
    y = f(x)
    plt.plot(x, y, linewidth=3)
    plt.axhline(y=0, c='black', linewidth=1)

plt.show()
print('--------------------------------------------------------------------------')
