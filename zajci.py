# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:28:44 2020

@author: gaspe
"""


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# EPIDEMIJA
N = 1000
B0, I0 = 50, 0
D0 = N - B0 - I0
alfa, beta = 0.5, 1./10 
t = np.linspace(0, 160, 160)
def deriv(y, t, N, alfa, gamma):
    D, B, I = y
    dDdt = -alfa * D * B / N
    dBdt = alfa * D * B / N - beta * B
    dIdt = beta * B
    return dDdt, dBdt, dIdt
y0 = D0, B0, I0
ret = odeint(deriv, y0, t, args=(N, alfa, beta))
D, B, I = ret.T

#ZAJCIINLISICE
#Z =
#L =
# alfa rodnost Z, beta kako hitro L lovijo Z,
#gama smrtnost L, delta množenje L na račun Z
alfa, beta, gama, delta =0.9,0.2,0.7,0.2
Z0= 10
L0=5

t = np.linspace(1,40,80)
def enacbe(y,t,a,b,c,d):
    Z, L = y
    dZdt = a*Z - b*Z*L
    dLdt = -c*L+d*Z*L
    return dZdt, dLdt
y0 = Z0,L0
ret = odeint(enacbe, y0,t, args=(alfa,beta,gama,delta))
Z,L = ret.T

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, Z, 'b', alpha=0.5, lw=2, label='Zajci')
ax.plot(t, L, 'r', alpha=0.5, lw=2, label='Lisice')
ax.set_xlabel('Število dni')
ax.set_ylabel('Število živali')
ax.set_ylim(0,15)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=1, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(True)
plt.show()