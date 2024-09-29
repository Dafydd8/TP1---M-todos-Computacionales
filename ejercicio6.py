import numpy as np
import matplotlib.pyplot as plt
from funciones import *

# Función para generar puntos aleatorios en R2
def puntosEnR2 ():
    p0 = np.random.rand(2)
    p1 = np.random.rand(2) 
    p2 = np.random.rand(2) 
    p3 = np.random.rand(2) 
   
    puntos = np.array([p0, p1, p2, p3])
    return puntos

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

# Función para generar puntos aleatorios en R2
def puntosEnR2 ():
    p0 = np.random.rand(2)
    p1 = np.random.rand(2) 
    p2 = np.random.rand(2) 
    p3 = np.random.rand(2) 
   
    puntos = np.array([p0, p1, p2, p3])
    return puntos

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
puntos1 = puntosEnR2()
puntos2 = puntosEnR2()
print(puntos1)
print(puntos2)

# Generar las curvas x(t) e y(t)
t_values = np.linspace(0, 1, 100)
curva1 = np.array([bezier(t, puntos1) for t in t_values])
curva2 = np.array([bezier(t, puntos2) for t in t_values])

# Graficar la curva x(t) con sus puntos de control
plt.figure(figsize=(8, 6))
plt.plot(curva1[:, 0], curva1[:, 1], label='Curva x(t)', color='green')
plt.scatter(puntos1[:, 0], puntos1[:, 1], color='green', label='Puntos de control x(t)')
plt.title('Curva x(t) y Puntos de Control')
plt.legend()
plt.show()

# Graficar la curva y(t) con sus puntos de control
plt.figure(figsize=(8, 6))
plt.plot(curva2[:, 0], curva2[:, 1], label='Curva y(t)', color='blue')
plt.scatter(puntos2[:, 0], puntos2[:, 1], color='blue', label='Puntos de control y(t)')
plt.title('Curva y(t) y Puntos de Control')
plt.legend()
plt.show()

# Calcular la matriz de transformación
matriz = matriz_transformacion(puntos1, puntos2)

# Calcular y generar T(x(t))
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