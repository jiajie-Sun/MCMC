"""
    cauchy prior
"""
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    y1 = x/(1+x**2)
    return y1

def f2(x):
    y2 = 1/(1+x**2)
    return y2

N = 1000
M = 1000

uper = round(0.95*M)
loer = round(0.05*M)
uppa = np.zeros((1,N))
lowa = uppa
avery = lowa
var = avery
var1 = avery
var2 = avery
cova = avery
Xlo = lowa
Xhi = lowa
kapa = lowa
estim1 = np.zeros((N,1))
estim2 = np.zeros((N,1))
estim = estim1
i = 0
while i < N:
    norma = np.random.normal(0, 1, M)+2.5
    ash1 = f1(norma)
    ash2 = f2(norma)
    estim1 = estim1 + ash1
    estim2 = estim2 + ash2
    # estim3 = estim1/estim2
    estim = np.sort(estim1/estim2)
    avery[i] = np.mean(estim)
    lowa[i] = estim[loer]
    uppa[i] = estim[uper]
    Xlo[i] = estim.min()
    Xhi[i] = estim.max()
    kapa[i] = np.mean((estim2)/(i+1))
    var1[i] = np.var(estim2)
    var2[i] = np.var(estim2)
    cova[i] = np.cov(np.transpose(estim1),np.transpose(estim2) )
    var[i] = (var1[i]-2*avery[i]*cova[i]+avery[i]**2*var2[i])/((i+1)*kapa[i]**2)

plt.plot(avery)
plt.ylim((0.5, 4.5))
plt.show()
