"""
    Beta generation
"""
import numpy as np
import matplotlib.pyplot as plt
U = np.random.uniform(0,1,10000)
V = np.random.uniform(0,1,10000)
alpha = np.linspace(1,100,100) * np.array([0.1]*100)
probs = np.zeros((100,1))
i = 0
while i< 100:
    probs[i] = len(U[(U**(1/alpha[i])+V**(1/alpha[i]))<1])/10000
    i = i+1
plt.plot(alpha,probs)
plt.xlabel('expression(alpha==beta)')
plt.ylabel('frequency')
plt.show()
