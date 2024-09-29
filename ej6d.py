import numpy as np
import matplotlib.pyplot as plt
from funciones import *

#ESTE ARCHIVO FUE MERAMENTE PARA PRUEBAS

# Función para calcular la matriz de transformación
def matriz_transformacion(puntos_p, puntos_q):
    p0 = np.array(puntos_p[0])
    p3 = np.array(puntos_p[3])
    q0 = np.array(puntos_q[0])
    q3 = np.array(puntos_q[3])
    if (p0[0] == 0 or p0[1]*p3[0] == p0[0]*p3[1]):
        print("La transformación no es posible")
        return
    denom = p0[1]*p3[0] - p0[0]*p3[1]
    a = (-1*p3[1]*q3[0] + p0[1]*q0[0]) / denom
    b = (p3[0]*q3[0] - p0[0]*q0[0]) / denom
    c = (-1*p3[1]*q3[1] + p0[1]*q0[1]) / denom
    d = (p3[0]*q3[1] - p0[0]*q0[1]) / denom
    return np.array([[a, b], [c, d]])

# Generar dos conjuntos de puntos 
puntos1 = np.array([[0.5531947, 0.53209561], [0.78724484, 0.38112949], [0.11631642, 0.18606128], [0.49731911, 0.1886042]])
puntos2 = np.array([[0.70264984, 0.18325078], [0.10376381, 0.23703703], [0.64034005, 0.82573804], [0.09974225, 0.49082618]])
#puntos1 = np.array([[1, 3], [2, 2], [6, 0], [1, 0]])
#puntos2 = np.array([[5, 0], [2, 0], [3, 4], [1, 3]])

# Generar las curvas x(t) e y(t)
t_values = np.linspace(0, 1, 100)
curva2 = np.array([bezier(t, puntos2) for t in t_values])

# Calcular la matriz de transformación
matriz = matriz_transformacion(puntos1, puntos2)

# Calcular T(x(t))
nuevos_puntos1 = matriz @ puntos1.T
nuevos_puntos1 = nuevos_puntos1.T
curva1 = np.array([bezier(t, nuevos_puntos1) for t in t_values])

# Graficar la union de las curvas T(x(t)) e y(t)
plt.figure(figsize=(8, 6))
plt.plot(curva1[:, 0], curva1[:, 1], label='Curva T(x(t))', color = 'red')
plt.plot(curva2[:, 0], curva2[:, 1], label='Curva y(t)', color='blue')
plt.scatter(nuevos_puntos1[:, 0], nuevos_puntos1[:, 1], color='red', label='Puntos de control T(x(t))')
plt.scatter(puntos2[:, 0], puntos2[:, 1], color='blue', label='Puntos de control y(t)')
plt.title('Curva T(x(t)) y Curva y(t)')
plt.legend()
plt.show()
