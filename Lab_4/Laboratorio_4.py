##Laboratorio 4
## Tema: Uso de Pandas y matplotlib

import pandas as pd
import matplotlib.pyplot as plt

#importando el archivo con pandas
datos = pd.read_csv('ventas.csv')
print("\nImprimiendo el arreglo original\n", datos)


#Calculando la ganancia y creando una columna nueva agregando los resultados al restar Ventas menos Gastos
datos['Ganancia']=datos['Ventas'] - datos['Gastos']
print("\nAgregando la columna nueva ganancia neta y mostrando como queda el dataframe\n", datos)

##realizando los pasos necesarios para crear el grafico
#extraer columnas del dataframe
ventas=datos['Ventas']
gastos=datos['Gastos']
ganancias=datos['Ganancia']
meses=datos['Mes']

#convirtiendo columnas en listas
mes=list(meses)
vent=list(ventas)
gast=list(gastos)
ganan=list(ganancias)

#agregando los datos del grafico
plt.plot(mes, vent, color='b', linestyle='solid', marker='o', label="Ventas")
plt.plot(mes, gast, color='r', linestyle='solid', marker='o', label="Gastos")
plt.plot(mes, ganan, color='g', linestyle='solid', marker='o', label="Ganancias")
plt.ylabel('Dolares')
plt.xticks(rotation=45)
plt.title('Ventas vrs Gastos Mensuales')
plt.legend()
plt.show()

#datos.plot(x='Ventas', y='Gastos')
#plt.show()
