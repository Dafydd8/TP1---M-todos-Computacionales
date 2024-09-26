import numpy as np
import matplotlib.pyplot as plt

# (a))
def envolvente_convexa(puntos, num_muestras=100):
    n = len(puntos)
    combinaciones = []
    
    for i in range(num_muestras):
        coeficientes = np.random.rand(n)
        coeficientes = coeficientes / coeficientes.sum()  # Normalizamos para que sumen 1
        combinacion = np.sum([coeficientes[i] * puntos[i] for i in range(n)], axis=0)
        combinaciones.append(combinacion)
    
    return np.array(combinaciones)

# Función para calcular una curva de Bézier a partir de puntos de control
def curva_bezier(puntos, num_muestras=100):
    n = len(puntos) - 1
    curva = []
    
    # Polinomio de Bernstein
    def bernstein(i, n, t):
        return np.math.comb(n, i) * (t**i) * ((1 - t)**(n - i))
    
    for t in np.linspace(0, 1, num_muestras):
        punto_bezier = sum(bernstein(i, n, t) * puntos[i] for i in range(n + 1))
        curva.append(punto_bezier)
    
    return np.array(curva)

# Función para graficar puntos individuales
def graficar_punto(punto, color='b', label=''):
    plt.scatter(punto[0], punto[1], color=color, label=label)

# Puntos de ejemplo en R2
puntos = [[1, 2], [5, 6], [2, 10]]

# Calculamos combinaciones convexas y curvas de Bézier
conv_S = envolvente_convexa(puntos, num_muestras=100)
curva_Bezier = curva_bezier(puntos)

# Graficar los puntos originales
graficar_punto(puntos[0], color='b', label='Original p0')  # p0
graficar_punto(puntos[1], color='g', label='Original p1')  # p1
graficar_punto(puntos[2], color='m', label='Original p2')  # p2

# Graficar algunas combinaciones convexas (F0 y F1)
t = 0.5
resultado_f0 = curva_bezier([puntos[0], puntos[1]], 1)[0]  # Combinación entre p0 y p1
resultado_f1 = curva_bezier([puntos[1], puntos[2]], 1)[0]  # Combinación entre p1 y p2

graficar_punto(resultado_f0, color='r', label='F0')  # Punto intermedio F0
graficar_punto(resultado_f1, color='y', label='F1')  # Punto intermedio F1

# Graficar la curva de Bézier
plt.plot(curva_Bezier[:, 0], curva_Bezier[:, 1], '-', label='Curva de Bézier', color='orange')

# Configurar el gráfico
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

# Mostrar el gráfico
plt.show()
