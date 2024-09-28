import matplotlib.pyplot as plt
from funciones import *

# Puntos de ejemplo en R2
punto_s1 = [1, 2]
puntos_s2 = [[1, 2], [5, 6]]
puntos_s3 = [[1, 2], [5, 6], [2, 10]]

conv_S1 = 1 * np.array(punto_s1)
conv_S2 = envolvente_convexa(puntos_s2, num_muestras=100)
conv_S3 = envolvente_convexa(puntos_s3, num_muestras=100)

#S1
plt.figure(figsize=(8, 6))
plt.title('conv(S1)')
plt.xlabel('x')
plt.ylabel('y')
graficar_punto(punto_s1, color='b', label='v1')  # p0
plt.scatter(conv_S1[0], conv_S1[1], color='orange', label='Puntos en envolvente convexa', alpha=0.5)
plt.legend()
plt.show()

#S2
plt.figure(figsize=(8, 6))
plt.title('conv(S2)')
plt.xlabel('x')
plt.ylabel('y')
graficar_poligono(puntos_s2, color='black')
graficar_punto(puntos_s2[0], color='b', label='v1')  
graficar_punto(puntos_s2[1], color='b', label='v2')  
plt.scatter(conv_S2[:, 0], conv_S2[:, 1], color='orange', label='Puntos en envolvente convexa', alpha=0.5)
plt.legend()
plt.show()

#S3
plt.figure(figsize=(8, 6))
plt.title('conv(S3)')
plt.xlabel('x')
plt.ylabel('y')
graficar_poligono(puntos_s3, color='black')
graficar_punto(puntos_s3[0], color='b', label='v1')  
graficar_punto(puntos_s3[1], color='b', label='v2') 
graficar_punto(puntos_s3[0], color='b', label='v3')
plt.scatter(conv_S3[:, 0], conv_S3[:, 1], color='orange', label='Puntos en envolvente convexa', alpha=0.5)
plt.legend()
plt.show()
