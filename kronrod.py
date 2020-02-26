# Author: Luciano de Oliveira Daniel
# https://sites.google.com/site/professorlucianodaniel

import numpy as np
from scipy import integrate
from math import inf

def pause():
    input("Press the <ENTER> key to continue...")

f = lambda x: x**8
print('Resultado analítico para f=x**8:', 1/9.0, 'seconds', '\n')
A1 = integrate.quadrature(f, 0.0, 1.0)
print('Quadratura para "f=x**8" de 0 a 1:', A1, '\n')
pause()

g = lambda x: 1/np.sqrt(np.pi) * np.exp(-x**2)
A2 = integrate.quadrature(g, 0.0, 1.0)
print('Quadratura para "g = 1/np.sqrt(np.pi) * np.exp(-x**2)" de 0 a 1:', A2, '\n')
pause()