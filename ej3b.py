import numpy as np
import matplotlib.pyplot as plt
from random import randint
from funciones import *

# Puntos de ejemplo en R2
puntos = [[randint(0,10), randint(0,10)], [randint(0,10), randint(0,10)], [randint(0,10), randint(0,10)]]

#convertir los puntos a np.array
for i in range(len(puntos)):
    puntos[i] = np.array(puntos[i])

#generar la curva de Bézier
t_values = np.linspace(0, 1, 100)
curva = np.array([bezier(t, puntos) for t in t_values])

# Graficar la curva resultante del ejemplo
plt.plot(curva[:, 0], curva[:, 1], label='Curva de Bézier', color='blue')

# Grafico puntos
graficar_punto(puntos[0], color='b', label='p0')  # p0
graficar_punto(puntos[1], color='g', label='p1')  # p1
graficar_punto(puntos[2], color='m', label='p2')  # p2

graficar_poligono(puntos)

# Configurar el gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

plt.show()