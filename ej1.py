import numpy as np
import matplotlib.pyplot as plt
from funciones import *

# Puntos de ejemplo en R2
puntos = [np.array([1, 2]), np.array([5, 6]), np.array([2, 10])]

# Generar las curvas f0, f1 y g
t_values = np.linspace(0, 1, 100)
f0s = np.array([f0(t, puntos) for t in t_values])
f1s = np.array([f1(t, puntos) for t in t_values])
gs = np.array([g(t, puntos) for t in t_values])

# Graficar las curvas f0, f1 y g
plt.plot(f0s[:, 0], f0s[:, 1], label='Curva f0')
plt.plot(f1s[:, 0], f1s[:, 1], label='Curva f1')
plt.plot(gs[:, 0], gs[:, 1], label='Curva g')

# Graficar los puntos originales
graficar_punto(puntos[0], color='b', label='p0')  # p0
graficar_punto(puntos[1], color='g', label='p1')  # p1
graficar_punto(puntos[2], color='m', label='p2')  # p2

# Configurar el gráfico
plt.title('Curvas f0, f1 y g')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

# Mostrar el gráfico
plt.show()