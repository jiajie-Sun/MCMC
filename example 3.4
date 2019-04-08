"""
    A first Monte Carlo integration
"""
import matplotlib.pyplot as plt
import numpy as np
NSIM = 10000
u = np.random.rand(10000)
den = np.arange(1,10001)
# 定义需要计算的函数
def f(x):
    y = (np.cos(50 * x) + np.sin(20 * x)) ** 2
    return y

x = np.linspace(0,1,50)
# mci_ex = (np.cos(50*x)+np.sin(20*x))**2
mci_ex = f(x)
plt.subplot(1,3,1)
plt.plot(x,mci_ex)
plt.subplot(1,3,2)
hint = f(u)
hplot = hint.cumsum()/den
hint2 = hint**2
stdh = np.sqrt(hint2.cumsum()/den - (hplot)**2)
plt.hist(hint,color='green')
plt.xlabel('Generated Values of Function')
plt.subplot(1,3,3)
y1 = hplot + stdh / np.sqrt(den)
y2 = hplot - stdh / np.sqrt(den)
plt.plot(hplot,color = 'red',linewidth = 0.4)
plt.plot(y1,color = 'green',linewidth = 0.4)
plt.plot(y2,color = 'green',linewidth = 0.4)
plt.xlabel('Mean and Standard Errors')
plt.xlim((1,NSIM+1))
plt.ylim((0.9,1.1))
plt.show()
