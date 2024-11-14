# -*- coding: utf-8 -*-
"""Laboratorio8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OX7WO-2fCBZZHOid-58Jkx8w_s73G0V-
"""

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import seaborn as sns
import pandas as pd

# Punto 1

productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E', 'Producto F', 'Producto G', 'Producto H']
ciudades = ['Bogotá', 'Cali', 'Bucaramanga']

# Datos de ventas ficticios para ilustrar
ventas = [
    [150, 200, 250],  # Producto A
    [100, 180, 220],  # Producto B
    [90, 150, 300],   # Producto C
    [120, 190, 210],  # Producto D
    [140, 160, 280],  # Producto E
    [110, 170, 260],  # Producto F
    [130, 210, 240],  # Producto G
    [105, 155, 290]   # Producto H
]

# Crear un gráfico de barras agrupadas
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.2
x = np.arange(len(productos))

for i, ciudad in enumerate(ciudades):
    ax.bar(x + i * bar_width, [venta[i] for venta in ventas], width=bar_width, label=ciudad)

# Personalizar el gráfico
ax.set_xlabel('Productos')
ax.set_ylabel('Ventas')
ax.set_title('Ventas de productos en Bogotá, Cali y Bucaramanga')
ax.set_xticks(x + bar_width)
ax.set_xticklabels(productos)
ax.legend()

# Estilo adicional
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Punto 2

meses = ['Enero', 'Febrero','Marzo', 'Abril', 'Mayo','Junio', 'Julio', 'Agosto']
producto = ['Papa (Cali)', 'Cebolla (Bogotá)', 'Tomate (Cartagena)']
evolucion = [
    [100, 90, 80],
    [150, 120, 110],
    [200, 160, 150],
    [250, 200, 190],
    [300, 240, 230],
    [400, 100, 330],
    [300, 200, 350],
    [150, 150, 240]
]

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))

# Definir colores y marcadores para cada producto
colores = ['blue', 'green', 'red']
marcadores = ['o', 's', '^']  # 'o' para círculo, 's' para cuadrado, '^' para triángulo

for i, prod in enumerate(producto):
    # Extraer la evolución de cada producto a través de los meses
    evolucion_producto = [evo[i] for evo in evolucion]
    plt.plot(
        meses, evolucion_producto,
        color=colores[i],
        marker=marcadores[i],
        label=prod
    )

# Personalizar el gráfico
plt.xlabel('Meses')
plt.ylabel('Evolución de Precio')
plt.title('Evolución de los Productos por Mes')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

#Punto 3

# Datos de ejemplo
horas_estudio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
puntuaciones = [50, 60, 65, 70, 75, 78, 80, 82, 85, 87, 90, 92, 94, 96, 98, 99, 100, 102, 103, 105]
nivel_motivacion = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115]

# Crear gráfico de dispersión con colores en función del nivel de motivación
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    horas_estudio, puntuaciones,
    c=nivel_motivacion, cmap='cool',  # Colores basados en nivel_motivacion y una paleta "cool"
    s=[mot * 0.8 for mot in nivel_motivacion],  # Tamaño de puntos basado en nivel_motivacion
    alpha=0.7
)

# Etiquetas
plt.xlabel('Horas de Estudio')
plt.ylabel('Puntuación en el Examen')
plt.title('Relación entre Estudio y Resultados')

# Barra de color para indicar el nivel de motivación
cbar = plt.colorbar(scatter)
cbar.set_label('Nivel de Motivación')

# Mostrar el gráfico
plt.show()

# Datos
puntuaciones = [50, 60, 65, 70, 75, 78, 80, 82, 85, 87, 90, 92, 94, 96, 98, 99,
                100, 102, 103, 105]
nivel_motivacion = ['Baja', 'Media', 'Media', 'Alta', 'Alta', 'Media', 'Media',
                    'Alta', 'Alta', 'Baja', 'Alta', 'Alta', 'Media', 'Alta',
                    'Alta', 'Media', 'Alta', 'Media', 'Baja', 'Alta']

# Crear un DataFrame con los datos
data = pd.DataFrame({'Puntuaciones': puntuaciones, 'Nivel_Motivacion': nivel_motivacion})

# Convertir 'Nivel_Motivacion' a tipo categórico
data['Nivel_Motivacion'] = pd.Categorical(data['Nivel_Motivacion'], categories=['Baja', 'Media', 'Alta'])

# Establecer estilo y paleta de colores fuertes
sns.set(style="whitegrid", palette="bright")

# Crear el histograma apilado
plt.figure(figsize=(10, 6))
hist_plot = sns.histplot(data=data, x='Puntuaciones', hue='Nivel_Motivacion', multiple='stack', bins=10)


# Personalización adicional
plt.title("Distribución de Puntuaciones en el Examen según Nivel de Motivación", fontsize=16)
plt.xlabel("Puntuaciones", fontsize=14)
plt.ylabel("Frecuencia", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Ajustar el diseño para reducir el espacio en blanco
plt.tight_layout()

plt.show()

# Parte 2 punto 2


meses = ['Enero', 'Febrero','Marzo', 'Abril', 'Mayo','Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
marcas = ['Suv', 'Sedan', 'Hatchback' ]
ventas = [
    [120, 100, 80],
    [130, 90, 85],
    [135, 95, 90],
    [140, 110, 95],
    [150, 120, 100],
    [160, 130, 105],
    [170, 140, 110],
    [180, 145, 115],
    [175, 150, 120],
    [185, 160, 125],
    [190, 170, 130],
    [200, 180, 135]
]

# Crear el gráfico de líneas
plt.figure(figsize=(10, 6))

# Definir colores y marcadores para cada producto
colores = ['magenta', 'purple', 'blue']
marcadores = ['v', 'p', 'h']  # 'o' para círculo, 's' para cuadrado, '^' para triángulo

for i, marca in enumerate(marcas):
    # Extraer la venta de cada carro a través de los meses
    ventas_carro = [venta[i] for venta in ventas]
    plt.plot(
        meses, ventas_carro,
        color=colores[i],
        marker=marcadores[i],
        label=marca
    )

# Personalizar el gráfico
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.title('Ventas de Carros por Mes')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

