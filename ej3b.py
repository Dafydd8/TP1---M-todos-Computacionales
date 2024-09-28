import numpy as np
import matplotlib.pyplot as plt
from random import randint
from funciones import *

# Puntos de ejemplo en R2
puntos3 = [[randint(0,10), randint(0,10)], [randint(0,10), randint(0,10)], [randint(0,10), randint(0,10)]]
puntos4 = [[randint(0,10), randint(0,10)], [randint(0,10), randint(0,10)], [randint(0,10), randint(0,10)], [randint(0,10), randint(0,10)]]

#convertir los puntos a np.array
for i in range(len(puntos3)):
    puntos3[i] = np.array(puntos3[i])
for i in range(len(puntos4)):
    puntos4[i] = np.array(puntos4[i])

#generar la curva de Bézier
t_values = np.linspace(0, 1, 100)
curva1 = np.array([bezier(t, puntos3) for t in t_values])
curva2 = np.array([bezier(t, puntos4) for t in t_values])

# Graficar la curva 1
plt.figure(figsize=(8, 6))
plt.title('Curva como combinación convexa')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(curva1[:, 0], curva1[:, 1], label='Curva de Bézier', color='blue')
graficar_punto(puntos3[0], color='b', label='p0')  # p0
graficar_punto(puntos3[1], color='g', label='p1')  # p1
graficar_punto(puntos3[2], color='m', label='p2')
graficar_poligono(puntos3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()
plt.show()

# Graficar la curva 2
plt.figure(figsize=(8, 6))
plt.title('Curva como combinación convexa')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(curva2[:, 0], curva2[:, 1], label='Curva de Bézier', color='blue')
graficar_punto(puntos4[0], color='b', label='p0')  # p0
graficar_punto(puntos4[1], color='g', label='p1')  # p1
graficar_punto(puntos4[2], color='m', label='p2')
graficar_punto(puntos4[3], color='y', label='p3')
graficar_poligono(puntos4)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()
plt.show()