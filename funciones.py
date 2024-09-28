import numpy as np
import matplotlib.pyplot as plt

######################
#FUNCIONES AUXILIARES#
######################

# Función para graficar puntos individuales
def graficar_punto(punto, color='black', label='', size = 30):
    plt.scatter(punto[0], punto[1], color=color, label=label, s=size)


def graficar_poligono(puntos, color='black', label=''):
    for i in range(len(puntos)):
        if i == len(puntos)-1:
            plt.plot([puntos[i][0], puntos[0][0]], [puntos[i][1], puntos[0][1]], color=color, label=label)
        else:
            plt.plot([puntos[i][0], puntos[i+1][0]], [puntos[i][1], puntos[i+1][1]], color=color, label=label)

#########################
#FUNCIONES DE EJERCICIOS#
#########################

#Ejercicio 1
def f0(t, puntos):
    return (1-t)*puntos[0] + t*puntos[1]

def f1(t, puntos):
    return (1-t)*puntos[1] + t*puntos[2]

def g(t, puntos): 
    p0 = puntos[0]
    p1 = puntos[1]
    p2 = puntos[2]
    return t*t*(p0-2*p1+p2) + t*(2*p1-2*p0) + p0

#Ejercicio 2
def coef_p3(t):
    return t**3

def coef_p2(t):
    return 3*t**2 - 3*t**3

def coef_p1(t):
    return 3*t**3 - 6*t**2 + 3*t

def coef_p0(t):
    return 3*t**2 - t**3 -3*t + 1

def h(t, puntos):
    p0 = puntos[0]
    p1 = puntos[1]
    p2 = puntos[2]
    p3 = puntos[3]
    return coef_p3(t)*p3 + coef_p2(t)*p2 + coef_p1(t)*p1 + coef_p0(t)*p0
 
#Ejercicio 3
def envolvente_convexa(puntos, num_muestras=100):
    puntos = np.array(puntos)  # Convertimos los puntos a un array de numpy
    n = len(puntos)
    combinaciones = []
    
    for _ in range(num_muestras):
        coeficientes = np.random.rand(n)
        coeficientes = coeficientes / coeficientes.sum()  # Normalizamos para que sumen 1
        combinacion = np.sum([coeficientes[i] * puntos[i] for i in range(n)], axis=0)
        combinaciones.append(combinacion)
    
    return np.array(combinaciones)

def bezier(t, puntos):
    p0 = puntos[0]
    p1 = puntos[1]
    p2 = puntos[2]
    if len(puntos) == 4:
        p3 = puntos[3]
        return coef_p3(t)*p3 + coef_p2(t)*p2 + coef_p1(t)*p1 + coef_p0(t)*p0
    elif len(puntos) == 3:
        return t**2*p2 + (2*t-2*t**2)*p1 + (t**2-2*t+1)*p0