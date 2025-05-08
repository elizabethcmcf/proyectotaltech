import matplotlib.pyplot as plt
import pandas as pd
import os
import pandas as pd

datos = pd.read_csv('areascultivadas.csv')
datos_filtrados = datos[
    (datos['Rubro'] == "Cebolla Junca") |
    (datos['Rubro'] == "Cilantro") |
    (datos['Rubro'] == "Lechuga") |
    (datos['Rubro'] == "Perejil") |
    (datos['Rubro'] == "Col") |
    (datos['Rubro'] == "Apio") |
    (datos['Rubro'] == "Eucalipto") |
    (datos['Rubro'] == "Espinaca")
]
datos_cebolla=datos_filtrados[datos_filtrados['Rubro']=="Cebolla Junca"]
datos_cilantro=datos_filtrados[datos_filtrados['Rubro']=="Cilantro"] 
datos_espinaca=datos_filtrados[datos_filtrados['Rubro']=="Espinaca"]
datos_perejil=datos_filtrados[datos_filtrados['Rubro']=="Perejil"]
datos_lechuga=datos_filtrados[datos_filtrados['Rubro']=="Lechuga"]
datos_col=datos_filtrados[datos_filtrados['Rubro']=="Col"]    
datos_apio=datos_filtrados[datos_filtrados['Rubro']=="Apio"]
datos_eucalipto=datos_filtrados[datos_filtrados['Rubro']=="Eucalipto"]

plt.figure(figsize=(12, 6))
plt.plot(datos_cebolla['Año'], datos_cebolla['Volumen Producción'], 
        color='#36ff33', marker='o')
plt.title('Volumen de Producción de Cebolla Junca por Año en Antioquia')
plt.xlabel('Año')
plt.ylabel('Volumen de Producción en Toneladas')
plt.xticks(datos_cebolla['Año'], rotation=45)
plt.tight_layout()
plt.savefig('ventas_totales_cebolla.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_cilantro['Año'], datos_cilantro['Volumen Producción'], 
        color='#36ff33', marker='o')
plt.title('Volumen de Producción de Cilantro por Año en Antioquia')
plt.xlabel('Año')
plt.ylabel('Volumen de Producción en Toneladas')
plt.xticks(datos_cilantro['Año'], rotation=45)
plt.tight_layout()
plt.savefig('ventas_totales_cilantro.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_espinaca['Año'], datos_espinaca['Volumen Producción'], 
        color='#36ff33', marker='o')
plt.title('Volumen de Producción de Espinaca por Año en Antioquia')
plt.xlabel('Año')
plt.ylabel('Volumen de Producción en Toneladas')
plt.xticks(datos_espinaca['Año'], rotation=45)
plt.tight_layout()
plt.savefig('ventas_totales_espinaca.png') 
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_perejil['Año'], datos_perejil['Volumen Producción'], 
        color='#36ff33', marker='o')
plt.title('Volumen de Producción de Perejil por Año en Antioquia') 
plt.xlabel('Año')
plt.ylabel('Volumen de Producción en Toneladas')
plt.xticks(datos_perejil['Año'], rotation=45)
plt.tight_layout()
plt.savefig('ventas_totales_perejil.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_lechuga['Año'], datos_lechuga['Volumen Producción'], 
        color='#36ff33', marker='o')
plt.title('Volumen de Producción de Lechuga por Año en Antioquia') 
plt.xlabel('Año')
plt.ylabel('Volumen de Producción en Toneladas')
plt.xticks(datos_lechuga['Año'], rotation=45)
plt.tight_layout()
plt.savefig('ventas_totales_lechuga.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_col['Año'], datos_col['Volumen Producción'], 
        color='#36ff33', marker='o')   
plt.title('Volumen de Producción de Col por Año en Antioquia')
plt.xlabel('Año')
plt.ylabel('Volumen de Producción en Toneladas')
plt.xticks(datos_col['Año'], rotation=45)
plt.tight_layout()
plt.savefig('ventas_totales_col.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_apio['Año'], datos_apio['Volumen Producción'], 
        color='#36ff33', marker='o')
plt.title('Volumen de Producción de Apio por Año en Antioquia')
plt.xlabel('Año')
plt.ylabel('Volumen de Producción en Toneladas')
plt.xticks(datos_apio['Año'], rotation=45)
plt.tight_layout()
plt.savefig('ventas_totales_apio.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(datos_eucalipto['Año'], datos_eucalipto['Volumen Producción'], 
        color='#36ff33', marker='o')
plt.title('Volumen de Producción de Eucalipto por Año en Antioquia')
plt.xlabel('Año')
plt.ylabel('Volumen de Producción en Toneladas')
plt.xticks(datos_eucalipto['Año'], rotation=45)
plt.tight_layout()
plt.savefig('ventas_totales_eucalipto.png')
plt.show()