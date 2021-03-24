#Aqui se importan las librerias a usar

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Se crea una variable llamada dfArchivo, en el que guardara el CSV llamado "Covid_Frecuencias"
# header = 0 / Esto le hace saber a python que el documento cuenta con Encabezados, por lo que no dara un salto de linea,
# - Si a header se le agrega un 1 o un 2, etc..., se tomara la primer fila como encabezado del CSV

# Sep = "," / El CSV se separará con columnas mas juntas
dfArchivo = pd.read_csv("Covid_Frecuencias.csv",header=0,sep=",")


#Imprimimos el CSV = Mostrará los datos
print(dfArchivo)


# Se crea la primer linea representando los Contagios dentro de la grafica
plt.plot(dfArchivo["Meses"], dfArchivo["Contagios"],label="Contagios", linewidth=2,color="blue",marker="*",markersize=10)

# Se crea la segunda linea  representando los Contagios dentro de la grafica
plt.plot(dfArchivo["Meses"],dfArchivo["Fallecidos"],label="Fallecidos", linewidth=2, color="red",marker="*",markersize=10)


# Muestra el titulo de la Grafica
plt.title("Contagiados/Fallecidos por Covid 19")

# Muestra la etiqueta (Titulo) del eje  X
plt.xlabel("Meses")

# Muestra la etiqueta (Titulo) del eje  Y
plt.ylabel("Personas")

# Define la Escala a mostrar la Grafica, en este caso la escala seria los Meses del eje X
plt.xticks(dfArchivo["Meses"])

#Muestra una leyenda (Representan que son los datos )
plt.legend()

#Muestra una cuadricula dentro de la grafica
plt.grid()

#Muestra la Grafica
plt.show()
