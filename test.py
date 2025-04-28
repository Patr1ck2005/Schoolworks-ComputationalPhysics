import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Set font for English display
plt.rcParams['font.sans-serif'] = ['Arial']  # Use Arial for English labels
plt.rcParams['axes.unicode_minus'] = False  # Ensure minus signs are displayed correctly

# Given data points
x_data = np.array([1, 2, 3, 4, 5, 6])
y_data = np.array([0.7, 1.7, 3.3, 7.3, 10.9, 22.7])

# Step 1: Take the natural logarithm of y
y_log = np.log(y_data)

# Step 2: Perform linear regression (y_log = intercept + slope * x)
slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_log)

# Step 3: Extract a and b from the regression result
b_fit = slope
a_fit = np.exp(intercept)

# Calculate uncertainties in parameters (from std_err)
a_err = a_fit * std_err  # Error in a is e^intercept * std_err
b_err = std_err          # The standard error of the slope is the uncertainty in b

# Display fitted parameters and their uncertainties
print(f"Fitted parameters: a = {a_fit:.3f} ± {a_err:.3f}")
print(f"                b = {b_fit:.3f} ± {b_err:.3f}")

# Generate the fitted curve for smooth plotting
x_fit = np.linspace(1, 6, 100)
y_fit = a_fit * np.exp(b_fit * x_fit)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'o', label='Experimental Data', color='red')
plt.plot(x_fit, y_fit, '--', label=f'Fitted Curve: y = {a_fit:.3f}e^({b_fit:.3f}x)', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Exponential Model Fit Results: a = {a_fit:.3f} ± {a_err:.3f}; b = {b_fit:.3f} ± {b_err:.3f}')
plt.legend()
plt.grid(True)
plt.show()
