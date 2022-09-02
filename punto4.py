#-------------------------------------------------------------------------------
# Name:        punto4
# Purpose:
#
# Author:      Daniela
#
# Created:     02/09/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#define dos variables y devuelve una suma
def ejercicio1():
    num1= 1; num2 = 4
    print(num1 + num2)


if __name__ == '__main__':
    ejercicio1()

#define dos variables string y devuelve una suma
def ejercicio2():
    cadena1 = "Hola, que tal?"; cadena2 = "Me llamo Daniela"
    print (cadena1 + " " + cadena2)

if __name__ == '__main__':
    ejercicio2()

#pide nombre y dni, y los devuelve
def ejercicio3():
    nombre = input("Ingrese su nombre: ")
    dni = input("Ingrese su dni: ")

    print(f'Su nombre es {nombre}')
    print(f'Su DNI es {dni}')

if __name__ == '__main__':
    ejercicio3()