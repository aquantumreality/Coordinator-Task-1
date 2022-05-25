import random as r
import math 

y1 = []
y2 = []

for i in range (0,100):
    y1.append(r.randint(0, 1))
    y2.append(r.random())

   
expressionO = 0

for i in range (0,100):
    expressionO += (-1/100)*((y1[i] * math.log2(y2[i]) + (1 - y1[i]) * math.log2(1 - y2[i])))

print(expressionO)
