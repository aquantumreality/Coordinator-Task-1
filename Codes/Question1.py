# Question 1 
import random as r
import math

n=100 # Set number of elements

y = [0] * n
y_hat = [0] * n

for k in range(n):
	y[k] = r.randint(0, 1)
	y_hat[k] = r.random()

o = 0
for j in range(n):
	o += (y[j]*math.log2(y_hat[j]) + (1-y[j])*math.log2(1-y_hat[j]))

o /= (-n)
print("The cross entropy loss is:", o)