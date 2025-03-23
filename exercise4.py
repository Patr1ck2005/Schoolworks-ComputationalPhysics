import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp

# === Set Quad Precision using mpmath ===
mp.dps = 34  # Set precision to about 34 decimal places (quad precision approximation)

# === Quadratic Formula Calculation with Cancellation Error Analysis ===
# Function to round a number to n significant digits
def round_to_significant_digits(num, sig_digits):
    return float(np.format_float_positional(num, precision=sig_digits, unique=True, fractional=False))

# Set the precision to 3 significant digits for the coefficients
a = round_to_significant_digits(1.22, 3)
b = round_to_significant_digits(3.34, 3)
c = round_to_significant_digits(2.28, 3)

# Calculate the discriminant with 3 significant digits
approxi_discriminant = round_to_significant_digits(b**2, 3) - round_to_significant_digits(4 * a * c, 3)

# True roots (accurate results with higher precision)
true_discriminant = b**2 - 4 * a * c

# Calculate absolute errors
abs_error = abs(true_discriminant - approxi_discriminant)

# Calculate relative errors
rel_error = abs(abs_error / true_discriminant) if true_discriminant != 0 else float('inf')

# Print the results
print(f"Computed Root 1 (3 significant digits): {approxi_discriminant}")
print(f"True Root 1 (high precision): {true_discriminant}")
print(f"Absolute Error Root 1: {abs_error}")
print(f"Relative Error Root 1: {rel_error*100}%")

# === Define Functions for (x-1)^7 and Its Expanded Form ===
def x_minus_1_7(x):
    """Computes (x-1)^7 using mpmath for quad precision."""
    return (x - 1) ** 7

def expanded_form(x):
    """Computes the expanded form: x^7 - 7x^6 + 21x^5 - 35x^4 + 35x^3 - 21x^2 + 7x - 1."""
    return x**7 - 7*x**6 + 21*x**5 - 35*x**4 + 35*x**3 - 21*x**2 + 7*x - 1

# === Create x Values for Precision Testing ===
x_values = np.linspace(0.999, 1.001, 400)

# --- Compute (x-1)^7 in Different Precisions ---
# Single precision
single_precision_vals = np.array([x_minus_1_7(np.float32(x)) for x in x_values], dtype=np.float32)

# Double precision
double_precision_vals = np.array([x_minus_1_7(np.float64(x)) for x in x_values], dtype=np.float64)

# Quad precision using mpmath
quad_precision_vals = np.array([x_minus_1_7(mp.mpf(x)) for x in x_values], dtype=object)

# --- Compute the Expanded Form in Different Precisions ---
# Single precision
expanded_single_vals = np.array([expanded_form(np.float32(x)) for x in x_values], dtype=np.float32)

# Double precision
expanded_double_vals = np.array([expanded_form(np.float64(x)) for x in x_values], dtype=np.float64)

# Quad precision using mpmath
expanded_quad_vals = np.array([expanded_form(mp.mpf(x)) for x in x_values], dtype=object)

# === Plotting the Results ===
plt.figure(figsize=(12, 6))

# Plot for (x-1)^7
plt.subplot(1, 2, 1)
plt.plot(x_values, single_precision_vals, label="Single Precision", color='b')
plt.plot(x_values, double_precision_vals, label="Double Precision", color='g')
plt.plot(x_values, quad_precision_vals, label="Quad Precision (mpmath)", color='r')
plt.title("(x-1)^7")
plt.xlabel("x")
plt.ylabel("(x-1)^7")
plt.legend()

# Plot for the expanded form
plt.subplot(1, 2, 2)
plt.plot(x_values, expanded_single_vals, label="Single Precision", color='b')
plt.plot(x_values, expanded_double_vals, label="Double Precision", color='g')
plt.plot(x_values, expanded_quad_vals, label="Quad Precision (mpmath)", color='r')
plt.title("Expanded Form of (x-1)^7")
plt.xlabel("x")
plt.ylabel("Expanded Value")
plt.legend()

plt.tight_layout()
plt.show()
