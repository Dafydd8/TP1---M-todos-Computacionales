import numpy as np
import matplotlib.pyplot as plt
from funciones import *

# Generar las curvas de los coeficientes en funcion de t
t_values = np.linspace(0, 1, 100)
coef0 = np.array([coef_p0(t) for t in t_values])
coef1 = np.array([coef_p1(t) for t in t_values])
coef2 = np.array([coef_p2(t) for t in t_values])
coef3 = np.array([coef_p3(t) for t in t_values])

# Graficar los coeficienes para 0<t<1
plt.plot(t_values, coef0[:], label='Curva coef0')
plt.plot(t_values, coef1[:], label='Curva coef1')
plt.plot(t_values, coef2[:], label='Curva coef2')
plt.plot(t_values, coef3[:], label='Curva coef3')

# Configurar el gráfico
plt.title('Curvas de los coeficientes de la función h(t)')
plt.xlabel('t')
plt.ylabel('coeficiente')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.legend()

# Mostrar el gráfico
plt.show()


