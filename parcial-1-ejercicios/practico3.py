#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniela
#
# Created:     18/10/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
##    Armar una función que se llame rankingConcesionarias(datos)
##    y reciba un parámetro datos que será un diccionario.
##
##    Al invocarla deberá ordenar de mayor a menor las concesionarias según la cantidad de ventas.
##
##    Finalmente deberá imprimir exactamente:
##
##    {NOMBRE_CONCESIONARIA}: {VENTAS} ventas
##    {NOMBRE_CONCESIONARIA}: {VENTAS} ventas
##    {NOMBRE_CONCESIONARIA}: {VENTAS} ventas
##    {NOMBRE_CONCESIONARIA}: {VENTAS} ventas
##    {NOMBRE_CONCESIONARIA}: {VENTAS} ventas


def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j]["ventas"] < lista[j+1]["ventas"]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]

def rankingConcesionarias(datos):
#ordenar de mayor a menor segun ventas
    burbuja(datos["registros"])

    for registro in datos["registros"]:
        concesionaria=registro["nro_concesionaria"]
        nombreConcesionaria=datos["concesionarias"][concesionaria-1]
        print(f'{nombreConcesionaria}: {registro["ventas"]} ventas')


datos = {
        "autos": ["FIAT Cronos", "Peugeot 208", "Toyota Hilux", "Volkswagen Amarok", "Chevrolet Cruze"],
        "concesionarias": ["Valmotors FIAT", "Kansai Toyota", "Le Meridien Peugeot", "San Jorge", "Dietrich"],
        "registros": [
            {'nro_registro': 1, 'nro_concesionaria': 2, 'nro_producto': 3, 'ventas': 14543},
            {'nro_registro': 2, 'nro_concesionaria': 4, 'nro_producto': 5, 'ventas': 10605},
            {'nro_registro': 3, 'nro_concesionaria': 1, 'nro_producto': 1, 'ventas': 25580},
            {'nro_registro': 4, 'nro_concesionaria': 5, 'nro_producto': 4, 'ventas': 12525},
            {'nro_registro': 5, 'nro_concesionaria': 3, 'nro_producto': 2, 'ventas': 15282}
        ]
    }

rankingConcesionarias(datos)