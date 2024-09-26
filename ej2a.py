import numpy as np
import matplotlib.pyplot as plt
from funciones import *

coef0 = []
coef1 = []
coef2 = []
coef3 = []

for t in np.linspace(0, 1, 200):
    coef0.append(np.array([t, coef_p0(t)]))
    coef1.append(np.array([t, coef_p1(t)]))
    coef2.append(np.array([t, coef_p2(t)]))
    coef3.append(np.array([t, coef_p3(t)]))

# Graficar los coeficienes para 0<t<1
graficar_curva(coef0, color='b', label='coeficiente p0')
graficar_curva(coef1, color='y', label='coeficiente p1')
graficar_curva(coef2, color='r', label='coeficiente p2')
graficar_curva(coef3, color='g', label='coeficiente p3')

# Configurar el gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

# Mostrar el gráfico
plt.show()


