# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:43:37 2019

@author: reinaqu_2
"""

from collections import namedtuple
import statistics
from statistics import *

Pico = namedtuple("Pico", "nombre altitud provincia")



def mostrar_picos1(picos):
    for pico in picos:
        print(pico)

        # -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:43:37 2019

@author: reinaqu_2
"""

from typing import *

Pico = NamedTuple("Pico", [("nombre", str), ("altitud", int), ("provincia", str)])



def mostrar_picos1(picos):
    for pico in picos:
        print(pico)



# 2.1 Obtener una lista con los nombres de los picos ordenada alfabéticamente
# Resultado esperado: [‘Alcazaba’, ‘Llambrión’, ‘Mulhacén’, ‘Naranjo’, ‘Peña Santa’, ‘Teide’, ‘Torrecilla’, ‘Torreón’, ‘Veleta’

def mostrar_picos_alf(picos: List[Pico])-> List[str]:
    return sorted(p.nombre for p in picos)
    




# 2.2 Obtener una lista con la altitud en kms y el nombre de los picos
# Resultado esperado: [(3.479, ‘Mulhacén’), (1.648, ‘Torreón’), (2.596, ‘Peña Santa’), (2.519, ‘Naranjo’), (3.371, ‘Alcazaba’), (3.396, ‘Veleta’), (1.919, ‘Torrecilla’), (2.647, ‘Llambrión’), (3.718,
# ‘Teide’)]

def altitud_kms(picos:List[Pico])-> List[Tuple[float, str]]:
    return [(p.altitud/1000, p.nombre) for p in picos]


# 2.3 Obtener una lista con los picos que están en la provincia de Granada
# Resultado esperado: [(‘Mulhacén’, 3479, ‘Granada’), (‘Alcazaba’, 3371, ‘Granada’), (‘Veleta’, 3396,
# ‘Granada’)]

def picos_provincia(picos:List[Pico], provincia:str)-> List[Pico]:
    return [Pico[(p.nombre, p.altitud, p.provincia)] for p in picos if p.provincia == provincia]


# 2.4 Obtener una lista con la altitud y el nombre de los picos que tienen más de 2000
# metros de altitud, ordenada de mayor a menor altitud
# Resultado esperado: [(3718, ‘Teide’), (3479, ‘Mulhacén’), (3396, ‘Veleta’), (3371, ‘Alcazaba’), (2647,
# ‘Llambrión’), (2596, ‘Peña Santa’), (2519, ‘Naranjo’)]
def mostrar_picos_por_altitud_mayor(picos:List[Pico], umbral: int) -> List[Tuple[int, str]]:
    return sorted(((p.altitud, p.nombre) for p in picos if p.altitud > umbral), reverse = True)


# 2.5 Obtener la suma de las altitudes de los picos que están en la provincia de León
# Resultado esperado: 5243

def picos_altitud_provincia(picos:List[Pico], provincia:str)-> int:
    return sum(p.altitud for p in picos if p.provincia == provincia)
                                                                   
# 2.6 Obtener el nombre y la altitud del pico más alto de la lista
# Resultado esperado: (3718, ‘Teide’)

def pico_mas_alto(picos:List[Pico])-> Tuple[int, str]:
    return max((p.altitud, p.nombre)for p in picos)


# 2.7 Obtener la altitud media de los picos
# Resultado esperado: 2810.3333333333335

def altitud_mean(picos:List[Pico])-> float:
    return statistics.mean(p.altitud for p in picos)


# 2.8 Obtener una lista ordenada con las provincias donde hay picos, sin repetir ninguna
# Resultado esperado: [‘Asturias’, ‘Cádiz’, ‘Granada’, ‘León’, ‘Málaga’, ‘Santa Cruz de Tenerife’]

def provincias_con_picos(picos:List[Pico]) -> List[str]:
    return sorted({p.provincia for p in picos})