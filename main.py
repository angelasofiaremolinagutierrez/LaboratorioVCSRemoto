import math
#Calcular el producto entre un número entero a y un número entero c
#También deberá calcular el doble del número a

na = int(input("Ingrese un número a: "))
nc = int(input("Ingrese un número c: "))

producto = na*nc
print()
print ("La multiplicación entre a y b es: " + str(producto))
print()
doble_a = 2*na
print ("El doble de a es: " + str(doble_a))
print()

#Calcular el cuadrado del numero entero b

nb = int(input("Ingrese un numero b: "))
potencia = nb*nb
print(str(nb) + " al cuadrado es: " + str(potencia))
print()

#Y la raiz cuadrada del numero d

nd = int(input("Ingrese un numero d: "))
raiz = math.sqrt(nd)
print ("La raiz de d es: " + str(raiz))