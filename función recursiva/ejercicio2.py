#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniela
#
# Created:     16/09/2022
# Copyright:   (c) Daniela 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    diccionarios=[]
    diccionario= {}
    stock=[]
    montototal=[]

    def pedirdatos():
        isbn = input("Ingrese un ISBN")
        if(isbn != "0"):
            diccionario['isbn']= isbn
            diccionario['NombredelLibro']=input("Ingrese el nombre del libro")
            diccionario['Stock']=int(input("Ingrese el stock"))
            stock.append(diccionario['Stock'])
            diccionario['Precio']=int(input("Ingrese el precio del libro"))
            montototal.append(diccionario['Precio']*diccionario['Stock'])
            diccionarios.append(diccionario)
            pedirdatos()

        else:
            return

    pedirdatos()
    print(stock)

    if (diccionario != {}):
        print(diccionarios)
        acumstock=0
        for i in stock:
            acumstock += i
        acumtotal=0
        for i in montototal:
            acumtotal += i
        print("La cantidad total de libros es ", acumstock)
        print("El monto total de los libros es ", acumtotal)
        print("El valor promedio de los libros es ", acumtotal/acumstock)

if __name__ == '__main__':
    main()
