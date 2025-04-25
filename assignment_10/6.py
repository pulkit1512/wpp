import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**3 - 6*x**2 + 4*x + 12  # Example polynomial function

# Implement the Bisection Method
def bisection_method(func, a, b, tolerance=1e-6):
    history = []  # To store midpoints for visualization
    while abs(b - a) > tolerance:
        mid = (a + b) / 2
        history.append(mid)  # Keep track of midpoint updates
        if func(mid) == 0:  # Found exact root
            break
        elif func(mid) * func(a) < 0:
            b = mid
        else:
            a = mid
    return mid, np.array(history)

# Initial interval (chosen based on sign change of f)
a, b = -2, 5  # Adjust these based on the polynomial
root, updates = bisection_method(f, a, b)

# Print the root and visualize
print(f"Root found at x = {root:.6f}")

# Plot the updates
plt.plot(range(len(updates)), updates, marker='o', label="Midpoint Updates")
plt.axhline(root, color='r', linestyle='--', label=f"Root ~ {root:.6f}")
plt.xlabel("Iteration")
plt.ylabel("Midpoint Value")
plt.title("Bisection Method Root-Finding Process")
plt.legend()
plt.show()
