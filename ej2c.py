import numpy as np
import matplotlib.pyplot as plt
from random import randint
from funciones import *

puntos_ejemplo = []
for i in range(3):
    p0 = np.array([randint(0, 10), randint(0, 10)])
    p1 = np.array([randint(0, 10), randint(0, 10)])
    p2 = np.array([randint(0, 10), randint(0, 10)])
    p3 = np.array([randint(0, 10), randint(0, 10)])
    puntos_ejemplo.append([p0, p1, p2, p3])

ej1 = []
ej2 = []
ej3 = []

for t in np.linspace(0, 1, 100):
    ej1.append(h(t, puntos_ejemplo[0]))
    ej2.append(h(t, puntos_ejemplo[1]))
    ej3.append(h(t, puntos_ejemplo[2]))

# Graficar las curvas resultantes de los ejemplos
graficar_curva(ej1, color='b', label='ej1')
graficar_curva(ej2, color='g', label='ej2')
graficar_curva(ej3, color='r', label='ej3')

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


