# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:50:37 2021

@author: william
"""

#extraer datos de empresas 
import numpy as np
from datetime import datetime

def read_file(filename):
    infile = open(filename, 'r')
    infile.readline()   #leer encabezados de clumnas
    dates = []; prices = []
    for line in infile:
        words= line.split(',')
        dates.append(words[0])
        prices.append(float(words[-1]))
    infile.close()
    dates.reverse()
    prices.reverse()
    #covertir fechas de la forma año-mes-día 
    datefmt = '%Y-%m-%d'
    dates = [datetime.strptime(_date, datefmt).date()
             for _date in dates]
    prices = np.array(prices)
    return dates[1:], prices[1:]


#podemos generalizar el programa a un número arbitrario de empresas 


dates = {}; prices = {}

import glob

filenames= glob.glob('D:/Desktop/curso phyton física/stockprices_*.csv')
companies= []
for filename in filenames:
    company = filename[12: -4]
    d, p= read_file(filename)
    dates[company]= d
    prices[company]= p

#lo que sigue es normalizar los precios para que coincidadn en una fecha determinada, 
# elegimos esta fecha como el primer mes del que disponemos 
# de datos de la empresa mas joen. En listas de objetos de fecha o fecha y hora, 
# podmos podemos usar las funciones max y min de Python para extraer 
# la fecha más nueva y más antigua

first_months = [dates[company][0] for company in dates]
normalize_date = max(first_months)
for company in dates:
    index= dates[company].index(normalize_date)
    prices[company] /= prices[company][index]
    
#gráfica log de precios versus fechas 

import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter

fig, ax = plt.subplots()
legends = []

for company in prices:
        ax.plot_date(dates[company], np.log(prices[company]),
                     '-', label = company)
        legends.append(company)
ax.legend(legends, loc = 'upper left')
ax.set_ylabel('logarithm of normalized value')

#formatear las ticks

years = YearLocator(5)
months = MonthLocator(6)
yearsfmt = DateFormatter('%Y')
ax.xaxis.set_major_formatter(yearsfmt)
ax.xaxis.set_minor_locator(months)
ax.autoscale_view()
fig.autofmt_xdate()

plt.savefig('tmp.pdf'); plt.savefig('tmp.png')
plt.show()

# los precios normalizados varían mucho, por lo que para ver mejor la evolución
# durante 30 años, decidimos tomar el logaritmo de los precios. El procedimieto de trazado es algo ocmplicado, 
# por lo que el lector deber tomar el código mas como una receta que como una secuencia de declaraciones para 
# comprender realmente.














