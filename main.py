import math
#Calcular el producto entre un número entero a y un número entero c
#También deberá calcular el doble del número a
print("Para calcular el producto entre dos números y el doble del primero")
na = int(input("Ingrese un número a: "))
nc = int(input("Ingrese un número c: "))

producto = na*nc
print()
print ("La multiplicación entre a y b es: " + str(producto))
doble_a = 2*na
print ("El doble de a es: " + str(doble_a))
print()

#Calcular el cuadrado del numero entero b
print("Para calcular el cuadrado de un número")
nb = int(input("Ingrese un numero b: "))
potencia = nb*nb
print(str(nb) + " al cuadrado es: " + str(potencia))
print()

#Y la raiz cuadrada del numero d
print("Para calcular la raiz cuadrada de un número")
nd = int(input("Ingrese un numero d: "))
raiz = math.sqrt(nd)
print ("La raiz de d es: " + str(raiz))
print()

#Solucion de la cuadrática
print("Para obtener los resultados de una cuadratica")
print("NOTA: Si aparece un erro de 'math domain', la cuadratica no tiene solución en los reales, ya que la raiz cuadrada de un numero negativo es un número imaginario")
ax2 = int(input("Escriba la variable a, que es la que acompaña a la X^2: "))
bx = int(input("Escriba la variable b, que es la que acompaña a la X: "))
c = int(input("Escriba la variable c, que es el número unitario: "))

#d = discriminante de la cuadratica
d = math.sqrt((bx*bx)-(4*ax2*c))

#cuando d>0
cuadratica_pos = (-bx + d)/(2 * ax2)
cuadratica_neg = (-bx - d)/(2 * ax2)
#cuando d=0
cuadratica_d0 = -bx/(2*ax2)
#cuando d<0
#no tiene solucion en los números reales

if d > 0 :
    print ("Solución 1: " + str(cuadratica_pos))
    print ("Solución 2: " + str(cuadratica_neg))

elif d == 0 :
    print ("Única solución: " + str(cuadratica_d0))

else:
    d < 0
    print("No existe solución en los números reales")

