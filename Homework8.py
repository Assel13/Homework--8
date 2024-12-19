#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

def f(x):
    return x**2

def gradient(x):
    return 2 * x

def gradient_descent(starting_point, learning_rate=0.1, iterations=100):
    x = starting_point
    history = [x]
    for _ in range(iterations):
        grad = gradient(x)
        x = x - learning_rate * grad
        history.append(x)
    return x, history

starting_point = 10  
learning_rate = 0.1
iterations = 100

min_x, history = gradient_descent(starting_point, learning_rate, iterations)

print(f"Минимальное значение x: {min_x}")
print(f"Минимальное значение функции: {f(min_x)}")


# In[ ]:




