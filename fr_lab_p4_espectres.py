# Física de Radiacions: Pràctica 4 

import csv
import matplotlib.pyplot as plt


# NA-22
# abrimos el archivo CSV
with open('na22_2.csv', 'r') as archivo:
  # leemos el archivo CSV
  lector_csv = csv.reader(archivo)
  # creamos las listas para cada columna
  channel_na = []
  counts_na = []
  # recorremos el archivo CSV
  for linea in lector_csv:
    channel_na.append(int(linea[0]))
    counts_na.append(int(linea[1]))

print("Na-22")
#print(channel_na)
#print(counts_na)

#Representación gráfica
plt.figure(figsize=(15, 8))
#plt.title("Cesi-137", fontsize="18")
plt.plot(channel_na, counts_na, 'o', markersize="3", color="blue")
plt.yscale("log")
#plt.plot(channel_na, counts_na, '-', linewidth="2", color="blue")
plt.ylabel('Comptes', fontsize="18")
plt.xlabel('Canal', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.legend(fontsize=15)
plt.minorticks_on()
plt.tick_params(which='both', width=1)
plt.tick_params(which='major', length=10)
plt.tick_params(which='minor', length=5)
plt.grid(True)
plt.show()


# COBALT-60
with open('cobalt60_2.csv', 'r') as archivo:
  lector_csv = csv.reader(archivo)
  channel_cobalt = []
  counts_cobalt = []
  for linea in lector_csv:
    channel_cobalt.append(int(linea[0]))
    counts_cobalt.append(int(linea[1]))

print("Cobalt-60")
#print(channel_cobalt)
#print(counts_cobalt)

#Representación gráfica
plt.figure(figsize=(15, 8))
#plt.title("Cobalt-60", fontsize="18")
plt.plot(channel_cobalt, counts_cobalt, 'o', markersize="3", color="blue")
plt.yscale("log")
#plt.plot(channel_cobalt, counts_cobalt, '-', linewidth="2", color="blue")
plt.ylabel('Comptes', fontsize="18")
plt.xlabel('Canal', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.legend(fontsize=15)
plt.minorticks_on()
plt.tick_params(which='both', width=1)
plt.tick_params(which='major', length=10)
plt.tick_params(which='minor', length=5)
plt.grid(True)
plt.show()


# ZINC-65
with open('zinc65_2.csv', 'r') as archivo:
  lector_csv = csv.reader(archivo)
  channel_zinc = []
  counts_zinc = []
  for linea in lector_csv:
    channel_zinc.append(int(linea[0]))
    counts_zinc.append(int(linea[1]))

print("Zinc-65")
#print(channel_zinc)
#print(counts_zinc)

#Representación gráfica
plt.figure(figsize=(15, 8))
#plt.title("Zinc-65", fontsize="18")
plt.plot(channel_zinc, counts_zinc, 'o', markersize="3", color="blue")
plt.yscale("log")
#plt.plot(channel_zinc, counts_zinc, '-', linewidth="2", color="blue")
plt.ylabel('Comptes', fontsize="18")
plt.xlabel('Canal', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.legend(fontsize=15)
plt.minorticks_on()
plt.tick_params(which='both', width=1)
plt.tick_params(which='major', length=10)
plt.tick_params(which='minor', length=5)
plt.grid(True)
plt.show()


# BARI-133
with open('bari133_2.csv', 'r') as archivo:
  lector_csv = csv.reader(archivo)
  channel_bari = []
  counts_bari = []
  for linea in lector_csv:
    channel_bari.append(int(linea[0]))
    counts_bari.append(int(linea[1]))

print("Bari-133")
#print(channel_bari)
#print(counts_bari)

#Representación gráfica
plt.figure(figsize=(15, 8))
#plt.title("Bari-133", fontsize="18")
plt.plot(channel_bari, counts_bari, 'o', markersize="3", color="blue")
plt.yscale("log")
#plt.plot(channel_bari, counts_bari, '-', linewidth="2", color="blue")
plt.ylabel('Comptes', fontsize="18")
plt.xlabel('Canal', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.legend(fontsize=15)
plt.minorticks_on()
plt.tick_params(which='both', width=1)
plt.tick_params(which='major', length=10)
plt.tick_params(which='minor', length=5)
plt.grid(True)
plt.show()


# CESI-137
with open('cesi137_2.csv', 'r') as archivo:
  lector_csv = csv.reader(archivo)
  channel_cesi = []
  counts_cesi = []
  for linea in lector_csv:
    channel_cesi.append(int(linea[0]))
    counts_cesi.append(int(linea[1]))

print("Cesi-137")
#print(channel_cesi)
#print(counts_cesi)

#Representación gráfica
plt.figure(figsize=(15, 8))
#plt.title("Cesi-137", fontsize="18")
plt.plot(channel_cesi, counts_cesi, 'o', markersize="3", color="blue")
plt.yscale("log")
#plt.plot(channel_cesi, counts_cesi, '-', linewidth="2", color="blue")
plt.ylabel('Comptes', fontsize="18")
plt.xlabel('Canal', fontsize="18")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
#plt.legend(fontsize=15)
plt.minorticks_on()
plt.tick_params(which='both', width=1)
plt.tick_params(which='major', length=10)
plt.tick_params(which='minor', length=5)
plt.grid(True)
plt.show()

