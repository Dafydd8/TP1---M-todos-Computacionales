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
curva = []
for t in np.linspace(0, 1, 100):
    curva.append(bezier(t, puntos))

# Graficar la curva resultante del ejemplo
graficar_curva(curva, color='b', label='Curva de Bézier')

# Grafico puntos
graficar_punto(puntos[0], color='b', label='Original p0')  # p0
graficar_punto(puntos[1], color='g', label='Original p1')  # p1
graficar_punto(puntos[2], color='m', label='Original p2')  # p2


plt.plot([puntos[0][0], puntos[1][0]], [puntos[0][1], puntos[1][1]], color="black")
plt.plot([puntos[0][0], puntos[2][0]], [puntos[0][1], puntos[2][1]], color="black")
plt.plot([puntos[1][0], puntos[2][0]], [puntos[1][1], puntos[2][1]], color="black")

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

plt.show()