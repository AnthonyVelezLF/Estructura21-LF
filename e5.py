#ejercicio5
#entrada
import math
a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))
c = int(input("ingrese el valor de c: "))

#proceso
d=(b*b)-4*a*c
if d<0:
    print("No existen soluciones reales!!")
else:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    
    print(".....Soluciones.....")
    print("X1:", "{:.2f}".format(x1))
    print("X2:", "{:.2f}".format(x2))