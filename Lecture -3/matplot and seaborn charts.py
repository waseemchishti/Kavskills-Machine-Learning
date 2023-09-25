#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

 
data = pd.read_csv('housing.csv')

# Create a Matplotlib histogram
plt.figure(figsize=(8, 6))
plt.hist(data['price'], bins=20, color='blue', alpha=0.7)
plt.title('Histogram of a Numeric Column')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)

# Display the Matplotlib chart
plt.show()

# Create a Seaborn scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='area', y='bedrooms', data=data, color='green', marker='o')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# Display the Seaborn chart
plt.show()

