import matplotlib.pyplot as plt
from funciones import *

# Puntos de ejemplo en R2
puntos = [[1, 2], [5, 6], [2, 10]]
conv_S = envolvente_convexa(puntos, num_muestras=100)

# Graficos
graficar_punto(puntos[0], color='b', label='Original p0')  # p0
graficar_punto(puntos[1], color='g', label='Original p1')  # p1
graficar_punto(puntos[2], color='m', label='Original p2')  # p2


plt.scatter(conv_S[:, 0], conv_S[:, 1], color='orange', label='Puntos en envolvente convexa', alpha=0.5)

plt.plot([puntos[0][0], puntos[1][0]], [puntos[0][1], puntos[1][1]], color="black")
plt.plot([puntos[0][0], puntos[2][0]], [puntos[0][1], puntos[2][1]], color="black")
plt.plot([puntos[1][0], puntos[2][0]], [puntos[1][1], puntos[2][1]], color="black")

#plt.xlim(-10, 10)
#plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

plt.show()