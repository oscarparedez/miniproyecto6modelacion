import math
import random

e = math.e
ITER = 1000
LIM_SUP = 1e3
LIM_INF = -1e3
x1, x2, eq1, eq2, result = 0, 0, 0, 0, 0

for i in range(0, ITER):
    x1 = random.randint(0,LIM_SUP)
    x2 = random.randint(LIM_INF,0)
    eq1 =- (e**(-x1**2))/2
    eq2 =- (e**(-x2**2))/2
    result += eq1-eq2

print(result)     
