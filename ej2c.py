import numpy as np
import matplotlib.pyplot as plt
from random import randint
from funciones import *

# Generar 3 conjuntos de puntos aleatorios para los ejemplos
puntos_ejemplo = []
for i in range(3):
    p0 = np.array([randint(0, 10), randint(0, 10)])
    p1 = np.array([randint(0, 10), randint(0, 10)])
    p2 = np.array([randint(0, 10), randint(0, 10)])
    p3 = np.array([randint(0, 10), randint(0, 10)])
    puntos_ejemplo.append([p0, p1, p2, p3])

# Generar las curvas usando los puntos de ejemplo
t_values = np.linspace(0, 1, 100)
ej1 = np.array([h(t, puntos_ejemplo[0]) for t in t_values])
ej2 = np.array([h(t, puntos_ejemplo[1]) for t in t_values])
ej3 = np.array([h(t, puntos_ejemplo[2]) for t in t_values])

# Graficar las curvas resultantes de los ejemplos
plt.plot(ej1[:, 0], ej1[:, 1], label='Ejemplo 1', color='blue')
plt.plot(ej2[:, 0], ej2[:, 1], label='Ejemplo 2', color='green')
plt.plot(ej3[:, 0], ej3[:, 1], label='Ejemplo 3', color='red')


# Graficar cada conjunto de puntos
colores = {1: '#020070', 2: '#007d11', 3: '#990000'}
for i, puntos in enumerate(puntos_ejemplo):
    for punto in puntos:
        plt.scatter(punto[0], punto[1], color=colores[i+1], label=f'Puntos control ejemplo {i+1}' if punto is puntos[0] else '')

# Configurar el gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

# Mostrar el gráfico
plt.show()


