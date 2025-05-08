import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('sipsaexporta.csv')


datos_cebolla=datos[datos['ARTICULO']=="Cebolla junca"]
datos_cilantro=datos[datos['ARTICULO']=="Cilantro"] 
datos_espinaca=datos[datos['ARTICULO']=="Espinaca"]
datos_perejil=datos[datos['ARTICULO']=="Perejil"]
datos_lechuga=datos[datos['ARTICULO']=="Lechuga crespa verde"]
datos_col=datos[datos['ARTICULO']=="Coles"]    
datos_apio=datos[datos['ARTICULO']=="Apio"]
datos_eucalipto=datos[datos['ARTICULO']=="Eucalipto"]

plt.figure(figsize=(12, 6))
plt.plot(datos_cebolla['FECHA'], datos_cebolla['PROMEDIO'], 
        color='#36ff33', marker='o')
plt.title('Precio Diario Mayorista de Cebolla Junca en Antioquia en el último mes')
plt.xlabel('Fecha')
plt.ylabel('Precio diario en peso colombiano')
plt.xticks(datos_cebolla['FECHA'], rotation=90)
plt.tight_layout()
plt.savefig('precio_cebolla.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_cilantro['FECHA'], datos_cilantro['PROMEDIO'], 
        color='#36ff33', marker='o')
plt.title('Precio Diario Mayorista de Cilantro en Antioquia en el último mes')
plt.xlabel('Fecha')
plt.ylabel('Precio diario en peso colombiano')
plt.xticks(datos_cilantro['FECHA'], rotation=90)
plt.tight_layout()
plt.savefig('precio_cilantro.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_espinaca['FECHA'], datos_espinaca['PROMEDIO'], 
        color='#36ff33', marker='o')
plt.title('Precio Diario Mayorista de Espinaca en Antioquia en el último mes')
plt.xlabel('Fecha')
plt.ylabel('Precio diario en peso colombiano')
plt.xticks(datos_espinaca['FECHA'], rotation=90)
plt.tight_layout()
plt.savefig('precio_espinaca.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_perejil['FECHA'], datos_perejil['PROMEDIO'], 
        color='#36ff33', marker='o')
plt.title('Precio Diario Mayorista de Perejil en Antioquia en el último mes')
plt.xlabel('Fecha')
plt.ylabel('Precio diario en peso colombiano')
plt.xticks(datos_perejil['FECHA'], rotation=90)
plt.tight_layout()
plt.savefig('precio_perejil.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_lechuga['FECHA'], datos_lechuga['PROMEDIO'], 
        color='#36ff33', marker='o')
plt.title('Precio Diario Mayorista de Lechuga en Antioquia en el último mes')
plt.xlabel('Fecha')
plt.ylabel('Precio diario en peso colombiano')
plt.xticks(datos_lechuga['FECHA'], rotation=90)
plt.tight_layout()
plt.savefig('precio_lechuga.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_col['FECHA'], datos_col['PROMEDIO'], 
        color='#36ff33', marker='o')
plt.title('Precio Diario Mayorista de Col en Antioquia en el último mes')
plt.xlabel('Fecha')
plt.ylabel('Precio diario en peso colombiano')
plt.xticks(datos_col['FECHA'], rotation=90)
plt.tight_layout()
plt.savefig('precio_col.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_apio['FECHA'], datos_apio['PROMEDIO'], 
        color='#36ff33', marker='o')
plt.title('Precio Diario Mayorista de Apio en Antioquia en el último mes')
plt.xlabel('Fecha')
plt.ylabel('Precio diario en peso colombiano')
plt.xticks(datos_apio['FECHA'], rotation=90)
plt.tight_layout()
plt.savefig('precio_apio.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_eucalipto['FECHA'], datos_eucalipto['PROMEDIO'], 
        color='#36ff33', marker='o')
plt.title('Precio Diario Mayorista de Eucalipto en Antioquia en el último mes')
plt.xlabel('Fecha')
plt.ylabel('Precio diario en peso colombiano')
plt.xticks(datos_eucalipto['FECHA'], rotation=90)
plt.tight_layout()
plt.savefig('precio_eucalipto.png')
plt.show()
