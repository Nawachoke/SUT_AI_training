import matplotlib.pyplot as plt
import numpy as np

a = np.matrix([[1,2,-1],
               [2,-1,1],
               [1,-1,-3]])

b = np.matrix([[3],[7],[-6]])
A_inv = np.linalg.inv(a)
x = A_inv * b
print(x)