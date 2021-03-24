import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfArchivo = pd.read_csv("Covid_Frecuencias.csv",header=0,sep=",")

print(dfArchivo)



plt.plot(dfArchivo["Meses"], dfArchivo["Contagios"],label="Contagios", linewidth=2,color="blue",marker="*",markersize=10)

plt.plot(dfArchivo["Meses"],dfArchivo["Fallecidos"],label="Fallecidos", linewidth=2, color="red",marker="*",markersize=10)



plt.title("Contagiados/Fallecidos por Covid 19")
plt.xlabel("Meses")
plt.ylabel("Personas")

plt.xticks(dfArchivo["Meses"])

plt.legend()
plt.grid()
plt.show()
