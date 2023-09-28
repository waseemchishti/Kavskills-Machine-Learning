#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.linalg import solve

# Define the coefficients and constants of the linear equation Ax = b
A = np.array([[2, 3], [1, -2]])
b = np.array([8, -4])

# Solve for x in Ax = b
x = solve(A, b)

print("Solution x:", x)


# In[2]:


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Sample data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 4, 6, 8, 10])

# Define a function to fit the data
def linear_function(x, m, b):
    return m * x + b

# Fit the data using curve_fit
params, covariance = curve_fit(linear_function, x, y)

# Extract the fitted parameters
m, b = params

# Plot the original data and the fitted line
plt.scatter(x, y, label="Data")
plt.plot(x, linear_function(x, m, b), label="Fitted Line", color='red')
plt.legend()
plt.show()


# In[3]:


import numpy as np
from scipy.integrate import quad

# Define the function to integrate
def func(x):
    return x**2

# Integrate the function from 0 to 1
result, error = quad(func, 0, 1)

print("Integral result:", result)
print("Error estimate:", error)


# In[4]:


import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Sample data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Create an interpolation function
f = interp1d(x, y, kind='linear')

# Generate new x values for interpolation
x_new = np.linspace(0, 4, 10)
y_new = f(x_new)

# Plot the original data and the interpolated curve
plt.scatter(x, y, label="Data")
plt.plot(x_new, y_new, label="Interpolated", color='red')
plt.legend()
plt.show()


# In[5]:


from scipy.optimize import minimize

# Define an objective function to minimize
def objective(x):
    return (x[0] - 2) ** 2 + (x[1] - 3) ** 2

# Initial guess
x0 = [0, 0]

# Perform the optimization
result = minimize(objective, x0)

print("Optimal solution:", result.x)

