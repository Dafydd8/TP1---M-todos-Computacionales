import numpy as np
import matplotlib.pyplot as plt
from random import randint
from funciones import *

puntos_ejemplo = [[np.array([1, 6]), np.array([4, 9]), np.array([3, 9]), np.array([1, 0])]]
punto = puntos_ejemplo[0]


p0 = punto[0]
p1 = punto[1]
p2 = punto[2]
p3 = punto[3]

ej1 = []

tan_0 = np.array(3*p1-3*p0)
tan_1 = -1*np.array(3*p3-3*p2)

# Dibujar el vector usando plt.quiver
plt.quiver(p0[0], p0[1], tan_0[0], tan_0[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(p3[0], p3[1], tan_1[0], tan_1[1], angles='xy', scale_units='xy', scale=1, color='r')

for t in np.linspace(0, 1, 100):
    ej1.append(h(t, puntos_ejemplo[0]))

# Graficar las curvas resultantes de los ejemplos
graficar_curva(ej1, color='b', label='ej1')

colores = {1: '#020070', 2: '#007d11', 3: '#990000'}

for j, ejemplo in enumerate(puntos_ejemplo):
    for i in range(len(ejemplo)):
        graficar_punto(ejemplo[i], color=colores[j+1])  # p0


# Configurar el gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

# Mostrar el gráfico
plt.show()


