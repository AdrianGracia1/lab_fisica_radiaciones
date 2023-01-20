#Fisica de Radiacions: Pràctica 3

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


#Practica 3a
x1 = [0, 5.4, 9.45, 13.51, 25.67, 31.07, 43.23, 64.84, 94.57, 135.1, 216.16, 270.2, 324.24, 405.3, 486.36]
e_x1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
y1 = [24.78, 23.07, 21.85, 19.30, 15.50, 13.82, 10.96, 6.40, 2.81, 0.94, 0.35, 0.34, 0.41, 0.34, 0.34]
e_y1 = [0.35, 0.34, 0.33, 0.31, 0.28, 0.26, 0.23, 0.15, 0.10, 0.06, 0.03, 0.03, 0.04, 0.03, 0.03]

plt.figure(figsize=(15, 8))
#plt.title("taxa en funcio del gruix", fontsize="18")
plt.plot(x1, y1, 'o', markersize="5", color="blue")
plt.plot(x1, y1, '-', linewidth="1", color="blue")
plt.errorbar(x1, y1, yerr=e_y1, fmt='none', ecolor="black", elinewidth=2, capsize=4, capthick=2)
plt.ylabel('Taxa de comptes $n$ (cps)', fontsize="18")
plt.xlabel('Gruix d\'alumini ($mg/cm^{2}$)', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.legend()
plt.grid(True)
plt.show()


#Practica 3b
x2 = [0, 5.4, 9.45, 13.51, 25.67, 31.07, 43.23, 94.57, 135.1, 216.16, 270.2, 324.24, 486.36, 945.7, 1080.8, 1215.9]

fr = [0.000, 0.302, 0.419, 0.536, 1.034, 1.259, 1.302, 1.905, 2.059, 2.199, 2.304, 2.363, 2.258, 2.249, 2.234, 2.314]
e_fr = [0.033, 0.040, 0.043, 0.046, 0.058, 0.063, 0.064, 0.078, 0.082, 0.085, 0.087, 0.089, 0.086, 0.086, 0.086, 0.088]

plt.figure(figsize=(15, 10))
#plt.title("factor de retrodispersió en funcio del gruix", fontsize="18")
plt.plot(x2, fr, 'o', markersize="5", color="blue")
plt.plot(x2, fr, '-', linewidth="1", color="blue")
plt.errorbar(x2, fr, yerr=e_fr, fmt='none', ecolor="black", elinewidth=2, capsize=4, capthick=2)
plt.ylabel('Factor de retrodispersió $f_{r}$', fontsize="18")
plt.xlabel('Gruix d\'alumini ($mg/cm^{2}$)', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.legend()
plt.grid(True)
plt.show()


#Practica 3b
x3 = [2.60, 3.55, 3.70, 3.77, 4.57, 5.73]

fr2 = [2.26, 3.49, 3.95, 3.20, 4.75, 6.05]
e_fr2 = [0.09, 0.11, 0.13, 0.11, 0.14, 0.18]


#Regresión Lineal 1:
x3_array = np.array(x3).reshape(-1,1)
fr2_array = np.array(fr2)

lr1 = LinearRegression()
lr1.fit(x3_array, fr2_array)
fr2_array_pred = lr1.predict(x3_array)
pendent_1 = lr1.coef_[0]
ordenada_1 = lr1.intercept_
R2_1 = r2_score(fr2_array, fr2_array_pred)

plt.figure(figsize=(15, 10))
#plt.title("factor de retrodispersió en funcio del gruix", fontsize="18")
plt.plot(x3, fr2, 'o', markersize="5", color="blue")
#plt.plot(x3, fr2, '-', linewidth="1", color="blue")
plt.errorbar(x3, fr2, yerr=e_fr2, fmt='none', ecolor="black", elinewidth=2, capsize=4, capthick=2)
plt.plot(x3_array, fr2_array_pred, '-' ,linewidth="1", color="blue", label="Recta de regresió")
plt.ylabel('Factor de retrodispersió $f_{r}$', fontsize="18")
plt.xlabel('$\sqrt{ {Z(Z+1)}/{M} }$', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)
plt.grid(True)
plt.show()

print("Pendent =", pendent_1)
print("ordenada =", ordenada_1)
print("R2 =", R2_1)