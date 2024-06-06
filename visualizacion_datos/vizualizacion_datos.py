# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:47:10 2024

@author: william
"""
import pandas as pd

import cufflinks as cf

from IPython.display import display,HTML


# damos una configuración para compartir de manera única, que sea de tema blanco
#  y que se pueda tener offline
cf.set_config_file(sharing='public', theme='ggplot', offline=True)

# revisamos que más temas hay disponibles
# print(cf.getThemes())

pd.read_csv('population_total.csv')

df_population = pd.read_csv('population_total.csv')

#Primero necesitamos deshacernos de los valores nulos:
df_population = df_population.dropna()

#Ahora vamos a cambiar la forma del dataframe:
df_population = df_population.pivot(index='year', columns='country', values='population')

#Seleccionamos cinco de los paises de la lista:
df_population = df_population[['United States', 'India', 'China', 'Indonesia', 'Brazil']]
df_population

#primero vamos a construir un LinePlot:

#nos ayudamos de cufflinks para utilizar el método .iplot()
df_population.iplot(kind='line', xTitle= "Year", yTitle= 'Population', title= 'Year vs Population')


#Ahora lo siguiente que vamos a construir es un gráfico de barras que nos muestre la población para el año 2020:
df_population_2020 = df_population[df_population.index.isin([2020])]
#Cambiamos filas por columnas:
df_population_2020= df_population_2020.T
df_population_2020

#Ya estamos listos para el gráfico de barras:
df_population_2020.iplot(kind='bar', xTitle='Countries', yTitle='Population', title='Year vs Population', color='blue')

#Ahora vamos a construir multiples gráficos de barras:
df_population_sample = df_population[df_population.index.isin([1980, 1990, 2000, 2010, 2020])]
df_population_sample.iplot(kind='bar', xTitle='Countries', yTitle='Population', title='Year vs Population', )


#También podemos construir un Boxplot para vizualizar cantidades estadísticas de los datos:
#podemos construir una boxplot para un país en particular:
df_population['United States'].iplot(kind='box')

#podemos construir una boxplot para un conjunto de paises:
df_population.iplot(kind='box')

#También podemos construir histogramas:
#Podemos ver un histograma para un país en particular:
df_population['United States'].iplot(kind='hist')

#podemos construir dos histogramas un un solo gráfico:
df_population[['United States', 'Indonesia']].iplot(kind='hist')

#También podemos construir un gráfico de tipo Piechart:

df_population_2020 = df_population_2020.reset_index()
df_population_2020 = df_population_2020.rename(columns={2020:'2020'})
df_population_2020.iplot(kind='pie', labels='country', values='2020', title='Porcentaje por país')



#También podemos crear un gráfico de dispersión:

df_population.iplot(kind='scatter', 
                    mode='markers',
                    xTitle= "Year", 
                    yTitle= 'Population', 
                    title= 'Year vs Population')
