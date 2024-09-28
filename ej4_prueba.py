import numpy as np
import matplotlib.pyplot as plt
from random import randint
from funciones import *

# Puntos de ejemplo en R2
puntos_ejemplo = [np.array([1, 6]), np.array([4, 9]), np.array([3, 9]), np.array([1, 0])]

p0 = puntos_ejemplo[0]
p1 = puntos_ejemplo[1]
p2 = puntos_ejemplo[2]
p3 = puntos_ejemplo[3]

tan_0 = (np.array(3*p1-3*p0))
tan_1 = -1*np.array(3*p3-3*p2)

#normalizamos los vectores
tan_0 = tan_0/np.linalg.norm(tan_0) 
tan_1 = tan_1/np.linalg.norm(tan_1)

# Generar las curvas usando los puntos de ejemplo
t_values = np.linspace(0, 1, 100)
ej1 = np.array([h(t, puntos_ejemplo) for t in t_values])

# Graficar las curvas resultantes de los ejemplos
plt.plot(ej1[:, 0], ej1[:, 1], label='Curva de Bézier', color='blue')
for punto in puntos_ejemplo:
    graficar_punto(punto, color="blue")

# Dibujar los vectores tangentes
plt.quiver(p0[0], p0[1], tan_0[0], tan_0[1], angles='xy', scale_units='xy', scale=1, color='g', label = 'Tangente en t=0')
plt.quiver(p3[0], p3[1], tan_1[0], tan_1[1], angles='xy', scale_units='xy', scale=1, color='r', label = 'Tangente en t=1')

# Configurar el gráfico
plt.title('Vectores tangentes a curva de Bézier')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

# Mostrar el gráfico
plt.show()


