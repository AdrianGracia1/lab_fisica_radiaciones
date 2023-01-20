#Regresión lineal con el metodo de mínimos cuadrados

#Librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

# Datos para construir la recta de regresion: y = A + Bx

#canal
x = [535, 1224, 1161, 1295, 319, 384, 705]
#energia
y = [511, 1275, 1173.23, 1332.49, 302.85, 356.01, 661.66]

#Incertidumbre en los datos (no se usa para el cálculo de la recta de regresión)
e_x = [43, 99, 94, 105, 26, 31, 57]

#Sumatorios para poder hacer los cálculos con mayor facilidad
sum_x = 0.
for i in range(len(x)):
  sum = x[i]
  sum_x = sum_x + sum

sum_x2 = 0.
for i in range(len(x)):
  sum = x[i]*x[i]
  sum_x2 = sum_x2 + sum

sum_y = 0.
for i in range(len(y)):
  sum = y[i]
  sum_y = sum_y + sum

sum_y2 = 0.
for i in range(len(y)):
  sum = y[i]*y[i]
  sum_y2 = sum_y2 + sum

sum_xy = 0.
for i in range(len(x)):
  sum = x[i]*y[i]
  sum_xy = sum_xy + sum

#Paso intermedio: valor del determinante
Delta = len(x) * sum_x2 - sum_x**2

#Valores de la ordenada de origen A y la pendiente B
A = (sum_y * sum_x2 - sum_x * sum_xy) / Delta
B = (len(x) * sum_xy - sum_x * sum_y)/ Delta

#Los parámetros A y B que mejor ajustan la recta son aquellos que hacen mínimo D2
D2 = 0.
for i in range(len(x)):
  sum = (y[i] - A - B*x[i])**2
  D2 = D2 + sum

#paso intermedio
sigma2 = (1 / (len(x)-2)) * D2

#Incertidumbre en A y en B
sigma_A = np.sqrt( (sigma2/Delta) * sum_x2 )
sigma_B = np.sqrt( (sigma2/Delta) * len(x) )

#Coeficiente de regresión
r2 = (len(x) * sum_xy - sum_x*sum_y)**2 / ((len(x) * sum_x2 - sum_x**2) * (len(x) * sum_y2 - sum_y**2))

#Output con los resultados
print("y = A + Bx")
print("A =", A, '+-', sigma_A)
print("B =", B, "+-", sigma_B)
print("r2 =", r2)

#Valor de y según la recta de regresión usando los valores de x
y_recta = []
for i in range(len(x)):
  n = A + B * x[i]
  y_recta.append(n)

#Representación gráfica
plt.figure(figsize=(15, 10))
#plt.title("Regresión lineal", fontsize="18")
plt.plot(x, y, 'o', markersize="8", color="blue")
#plt.plot(x, y, '-', linewidth="1", color="red")
plt.errorbar(x, y, xerr=e_x, fmt='none', ecolor="black", elinewidth=2, capsize=4, capthick=2)
plt.plot(x, y_recta, '-' ,linewidth="1", color="blue", label="Recta de regresió")
plt.ylabel('Energia (keV)', fontsize="18")
plt.xlabel('Canal', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)
plt.grid(True)
plt.show()