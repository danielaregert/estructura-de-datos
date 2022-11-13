##        Ejercicio 1
##        Para probar los distintos algoritmos de ordenamiento vistos (Burbuja, Selección,
##        Inserción, Rápido y Mezcla):
##        a) Generar una lista de elementos aleatorios de distintos tamaños (100.000,
##        1.000.000, 10.000.000)
##        b) Medir y mostrar su tiempo de ejecución
##        c) Medir y mostrar la cantidad de comparaciones realizadas
##        d) Deberá indicar nombre y tiempo del método más rápido
##        e) Deberá indicar nombre y cantidad del método que realiza menos comparaciones

import random
import time


#random.randint(0, 100)
#time.time()
#CREO LAS LISTAS

cien =[]
mil =[]
diezmil =[]


for i in range(100):
    aux=random.randint(0,1000)
    cien.append(aux)


for i in range(1000):
    aux=random.randint(0,1000)
    mil.append(aux)

for i in range(10000):
    aux=random.randint(0,10000)
    diezmil.append(aux)


#BURBUJA

def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] > lista[j+1]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]


#PRUEBA con lista de CIEN ELEMENTOS
print("Inicio método burbuja con cien elementos")
tiempoinicial=time.time()

burbuja(cien)

print(cien[99]) #me imprimo un ultimo valor para verificar q los orden{o

tiempofinal=time.time()

print(f'El tiempo inicial fue {tiempoinicial} y el final fue {tiempofinal}')
print("La diferencia con cien elementos es de", tiempofinal-tiempoinicial)

#PRUEBA con lista de MIL ELEMENTOS
print("Inicio método burbuja con mil elementos")
tiempoinicial=time.time()

burbuja(mil)
print(diezmil[999])

tiempofinal=time.time()

print(f'El tiempo inicial fue {tiempoinicial} y el final fue {tiempofinal}')
print("La diferencia con mil elementos es de", tiempofinal-tiempoinicial)

#DIEZMIL MIL ELEMENTOS
print("Inicio método burbuja con cienmil elementos")
tiempoinicial=time.time()

burbuja(diezmil)
print(diezmil[9999])

tiempofinal=time.time()

print(f'El tiempo inicial fue {tiempoinicial} y el final fue {tiempofinal}')
print("La diferencia con diez mil elementos es de", tiempofinal-tiempoinicial)
