# -*- coding: utf-8 -*-
"""fr_lab_p1a.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F3H_TNwrPqrQlc0yg9IY_mi4i--SBOiQ
"""

#Regresión lineal con el metodo de mínimos cuadrados

#Librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

# Datos para construir la recta de regresion: y = A + Bx
x = [630, 635, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020, 1040]
y = [0, 22.39, 25.18, 25.77, 28.20, 30.94, 32.48, 33.63, 34.74, 35.79, 37.07, 37.57, 40.14, 39.69, 40.59, 41.42, 41.66, 42.56, 44.44, 43.71, 54.82, 70.27, 224.99]

#Incertidumbre en los datos (no se usa para el cálculo de la recta de regresión)
e_x = []
e_y = [0, 0.43, 0.46, 0.48, 0.56, 0.59, 0.60, 0.61, 0.62, 0.63, 0.64, 0.65, 0.67, 0.66, 0.67, 0.68, 0.68, 0.69, 0.70, 0.70, 0.78, 0.88, 1.58]


#Representación gráfica
plt.figure(figsize=(15, 10))
#plt.title("Regresión lineal", fontsize="18")
plt.plot(x, y, 'o', markersize="7", color="blue")
plt.plot(x, y, '-', linewidth="1", color="blue")
plt.errorbar(x, y,yerr=e_y, fmt='none', ecolor="black", elinewidth=2, capsize=4, capthick=2)
#plt.plot(x, y_recta, '-' ,linewidth="1", color="blue", label="Recta de regresión")
plt.ylabel('Taxa de comptes (cps)', fontsize="18")
plt.xlabel('Voltatge (V)', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.minorticks_on()
plt.tick_params(which='both', width=1)
plt.tick_params(which='major', length=10)
plt.tick_params(which='minor', length=5)
#plt.legend(fontsize=15)
plt.grid(True)
plt.show()