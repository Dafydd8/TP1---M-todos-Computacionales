import numpy as np
import matplotlib.pyplot as plt
from funciones import *

def puntosEnR2 ():
    p0 = np.random.rand(2) 
    p1 = np.random.rand(2) 
    p2 = np.random.rand(2) 
    p3 = np.random.rand(2) 
   
    puntos = np.array([p0, p1, p2, p3])
    return puntos

# Generar dos conjuntos de puntos 
puntos1 = puntosEnR2()
puntos2 = puntosEnR2()

# Generar las curvas x(t) e y(t)
t_values = np.linspace(0, 1, 100)
curva1 = np.array([bezier(t, puntos1) for t in t_values])
curva2 = np.array([bezier(t, puntos2) for t in t_values])

# Graficar la curva x(t) con sus puntos de control
plt.figure(figsize=(8, 6))
plt.plot(curva1[:, 0], curva1[:, 1], label='Curva x(t)')
plt.scatter(puntos1[:, 0], puntos1[:, 1], color='red', label='Puntos de control x(t)')
plt.title('Curva x(t) y Puntos de Control')
plt.legend()
plt.show()

# Graficar la curva y(t) con sus puntos de control
plt.figure(figsize=(8, 6))
plt.plot(curva2[:, 0], curva2[:, 1], label='Curva y(t)', color='green')
plt.scatter(puntos2[:, 0], puntos2[:, 1], color='blue', label='Puntos de control y(t)')
plt.title('Curva y(t) y Puntos de Control')
plt.legend()
plt.show()