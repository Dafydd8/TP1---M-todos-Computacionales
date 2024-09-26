import numpy as np
import matplotlib.pyplot as plt
from funciones import *

# Puntos de ejemplo en R2
puntos = [np.array([1, 2]), np.array([5, 6]), np.array([2, 10])]

f0s = []
f1s = []
gs = []
for t in np.linspace(0, 1, 200):
    f0s.append(f0(t, puntos))
    f1s.append(f1(t, puntos))
    gs.append(g(t, puntos))

# Graficar las curvas f0, f1 y g
graficar_curva(f0s, color='b', label='f0')
graficar_curva(f1s, color='y', label='f1')
graficar_curva(gs, color='r', label='g')

# Graficar los puntos originales
graficar_punto(puntos[0], color='b', label='Original p0')  # p0
graficar_punto(puntos[1], color='g', label='Original p1')  # p1
graficar_punto(puntos[2], color='m', label='Original p2')  # p2



# Configurar el gráfico
#plt.xlim(-10, 10)
#plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

# Mostrar el gráfico
plt.show()