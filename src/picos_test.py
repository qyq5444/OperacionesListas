# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:43:48 2019

@author: reinaqu_2
"""
from picos import *

def test_mostrar_picos_alf(picos:List[Pico])->None:
    res = mostrar_picos_alf(picos)
    print(f"Los nombres ordenados son: {res}")

def test_altitud_kms(picos:List[Pico])->None:
    res = altitud_kms(picos)
    print(f"Las altitudes son: {res}")

def test_picos_provincia(picos:List[Pico], provincia:str)-> None:
    res = picos_provincia(picos, provincia)
    print(f"Los picos de la provincia {provincia} son {res}")

def test_mostrar_picos_por_altitud_mayor(picos:List[Pico], umbral:int)->None:
    res = mostrar_picos_por_altitud_mayor(picos, umbral)
    print(f"Los picos con una altitud superior a {umbral} son: {res}")

def test_picos_altitud_provincia(picos:List[Pico], provincia:str)->None:
    res = picos_altitud_provincia(picos, provincia)
    print(f"La suma de las altitudes de los picos en la provincia de {provincia} es: {res}")

def test_pico_mas_alto(picos:List[Pico])-> None:
    res = pico_mas_alto(picos)
    print(f"El pico más alto es: {res}")

def test_altitud_mean(picos:List[Pico])->None:
    res = altitud_mean(picos)
    print(f"La media de altitud es: {res}")

def test_provincias_con_picos(picos:List[Pico])-> None:
    res = provincias_con_picos(picos)
    print(f"Las provincias con picos son: {res}")
    

if __name__=='__main__':
    PICOS = [Pico("Mulhacén", 3479, "Granada"), 
             Pico("Torreón", 1648, "Cádiz"),
             Pico("Peña Santa", 2596, "León"), 
             Pico("Naranjo", 2519, "Asturias"),
             Pico("Alcazaba", 3371, "Granada"), 
             Pico("Veleta", 3396, "Granada"),
             Pico("Torrecilla", 1919, "Málaga"), 
             Pico("Llambrión", 2647, "León"),
             Pico("Teide", 3718, "Santa Cruz de Tenerife")]
             
    mostrar_picos1(PICOS)
    test_mostrar_picos_alf(PICOS)
    test_altitud_kms(PICOS)
    test_picos_provincia(PICOS, "Granada")
    test_mostrar_picos_por_altitud_mayor(PICOS, 2000)
    test_picos_altitud_provincia(PICOS, "León")
    test_pico_mas_alto(PICOS)
    test_altitud_mean(PICOS)
    test_provincias_con_picos(PICOS)
    