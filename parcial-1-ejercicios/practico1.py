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
##
##        Armar una función que se llame buscarConcesionaria()
##        y reciba dos parámetros (datos, concesionaria) que serán un diccionario y un string.
##
##        Al invocarla deberá hacer una búsqueda binaria para encontrar
##        el índice de la concesionaria que se busca, y luego deberá realizar
##        una búsqueda secuencial en los registros para identificar los valores
##        de la concesionaria.
##
##        Finalmente deberá imprimir exactamente:
##
##        Registro Nro: {NRO_REGISTRO}
##        Concesionaria Nro: {NRO_CONCESIONARIA} - {NOMBRE_CONCESIONARIA}
##        Producto Nro: {NRO_PRODUCTO} - {NOMBRE_PRODUCTO}
##        Cantidad vendida: {VENTAS}


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

def binaria(lista, buscado) :
    """ Metodo de busqueda binaria """
    posicion = -1
    primero = 0
    ultimo = len(lista) - 1

    while (primero <= ultimo) and (posicion == -1) :
        medio = (primero + ultimo) // 2

        if (lista[medio] == buscado) :
            posicion = medio
        else :
            if (buscado < lista[medio]) :
                ultimo = medio - 1
            else :
                primero = medio + 1

    return posicion

def secuencial(lista, buscado) :
    """ Metodo de busqueda secuencial """
    posicion = -1

    for i in range(0, len(lista)) :
        if (lista[i]["nro_concesionaria"] == buscado) :
            posicion = i

    return posicion



def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] > lista[j+1]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]



def buscarConcesionaria(datos, concesionaria):
    #ORDENAMIENTO
    burbuja(datos["concesionarias"])
    #busqueda binaria para recibir indice de dato buscado en concesionarias
    posicionA=binaria(datos["concesionarias"], concesionaria)+1
    print(posicionA)
    #busqueda secuencial
    posicionB=secuencial(datos["registros"], int(posicionA))
    print(posicionB)
    print(datos["registros"][posicionB])
    imprimirdatos(datos,posicionB)


def imprimirdatos(datos, posicion):
    print(f"Nro de registro: {datos['registros'][posicion]['nro_registro']}")
    print(f"Nro de concesionaria: {datos['registros'][posicion]['nro_concesionaria']}")
    print(f"Nro de producto: {datos['registros'][posicion]['nro_producto']}")
    print(f"Nro de ventas: {datos['registros'][posicion]['ventas']}")


buscarConcesionaria(datos,"San Jorge")