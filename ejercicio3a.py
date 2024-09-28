import matplotlib.pyplot as plt
from funciones import *

# Puntos de ejemplo en R2
puntos = [[1, 2], [5, 6], [2, 10]]
conv_S = envolvente_convexa(puntos, num_muestras=100)

# Grafico puntos
graficar_punto(puntos[0], color='b', label='p0')  # p0
graficar_punto(puntos[1], color='g', label='p1')  # p1
graficar_punto(puntos[2], color='m', label='p2')  # p2

# Graficar algunos puntos de envolvente convexa
plt.scatter(conv_S[:, 0], conv_S[:, 1], color='orange', label='Puntos en envolvente convexa', alpha=0.5)

# Graficar poligono formado por puntos
graficar_poligono(puntos)

#plt.xlim(-10, 10)
#plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

plt.show()