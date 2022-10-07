# Referencia: https://towardsdatascience.com/generate-random-variable-using-inverse-transform-method-in-python-8e5392f170a3

import numpy as np
from scipy.stats import uniform

def discrete_inverse_trans(prob_vec):
    U=uniform.rvs(size=1)
    if U<=prob_vec[0]:
        return 1
    else:
        for i in range(1,len(prob_vec)+1):
            if sum(prob_vec[0:i])<U and sum(prob_vec[0:i+1])>U:
                return i+1

def discrete_samples(prob_vec,n=1):
    sample=[]
    for i in range(0,n):
        sample.append(discrete_inverse_trans(prob_vec))
    return np.array(sample)


def discrete_simulate(prob_vec,n=1):
    sample_disc=discrete_samples(prob_vec,n)
    unique, counts=np.unique(sample_disc,return_counts=True)
     
    fig=plt.figure()
    ax=fig.add_axes([0,0,1,1])
    prob=counts/n
    return "# de ocurrencias", str(counts), "Probabilidad actual", str(prob_vec), "Probabilidad calculada", str(prob)

# Probabilidad mujer con lentes
prob_vec = np.array([0.25,0.75])
distrib1 = discrete_simulate(prob_vec, n=100)
# Probabilidad hombre sin lentes que sea varon
prob_vec = np.array([0.65,0.35])
distrib2 = discrete_simulate(prob_vec, n=100)

print(distrib1)
print(distrib2) 
