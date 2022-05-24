from math import *
import numpy as np

y1  = np.random.rand(100)
y = np.random.randint(2, size=100)
print(y.tolist())
print(y1.tolist())
z = -1*(np.multiply(y,np.log2(y1))+np.multiply((1-y),np.log2(1-y1)))/100
op = np.sum(z)
print(op) 