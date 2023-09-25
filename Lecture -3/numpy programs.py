#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Create a NumPy array from a Python list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_array)


# In[2]:


# Python program to demonstrate
# basic operations on single array
import numpy as np
 
# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
               
# Adding 1 to every element
print ("Adding 1 to every element:", a + 1)
 
# Subtracting 2 from each element
print ("\nSubtracting 2 from each element:", b - 2)
 
# sum of array elements
# Performing Unary operations
print ("\nSum of all array "
       "elements: ", a.sum())
 
# Adding two arrays
# Performing Binary operations
print ("\nArray sum:\n", a + b)


# In[3]:


import numpy as np

# Array slicing with NumPy
my_array = np.array([1, 2, 3, 4, 5])

# Slicing from index 1 to 3 (exclusive)
sliced_array = my_array[1:3]

print("Sliced Array:")
print(sliced_array)


# In[4]:


import numpy as np

# Basic statistics with NumPy
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Mean
mean = np.mean(data)

# Median
median = np.median(data)

# Standard Deviation
std_dev = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)


# In[5]:


import numpy as np

# Perform operations on NumPy arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Addition
result_add = array1 + array2

# Multiplication
result_mul = array1 * array2

print("Addition Result:", result_add)
print("Multiplication Result:", result_mul)


# In[ ]:




