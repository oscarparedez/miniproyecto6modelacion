import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Referencia: https://towardsdatascience.com/generate-random-variable-using-inverse-transform-method-in-python-8e5392f170a3

def discrete_inverse_trans(prob_vec):
    U=uniform.rvs(size=1)
    if U<=prob_vec[0]:
        return 1
    else:
        for i in range(1,len(prob_vec)+1):
            if sum(prob_vec[0:i])<U and sum(prob_vec[0:i+1])>U:
                return i+1

randomlist = np.array([])
meanList = np.array([])
orderedList = np.array([])
for i in range(0, 100000):
    # n = random.uniform(0.0, 1.0)
    n = discrete_inverse_trans(np.array([0.5,0.5])) -1
    randomlist = np.append(randomlist, n)
    orderedList = np.append(orderedList, i)
    meanList = np.append(meanList, np.mean(randomlist))
print(meanList)
plt.figure(figsize = (15,8))
plt.plot(orderedList, meanList, c = "blue", label="N Datos")
plt.axhline(y = 0.5, color = 'r', linestyle = '--', label='Media')
plt.legend(loc='upper right')
plt.xlabel('n')
plt.ylabel('Sn')
plt.title('Ley de los grande números')
plt.show()