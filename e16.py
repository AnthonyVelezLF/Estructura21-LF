#ejercicio1
n1= int(input("ingrese el primer número positivo: "))
n2= int(input("ingrese el segundo número positivo: "))
n3= int(input("ingrese el tercer número positivo: "))

if n3 > n2 > n1:
    print("\n el número mayor es: {} y el segundo mayor es {} ".format(n3,n2))
elif n3 > n1 > n2:
    print("\n el número mayor es: {} y el segundo mayor es {} ".format(n3,n1))
elif n2 > n3 > n1:
    print("\n el número mayor es: {} y el segundo mayor es {} ".format(n2,n3))
elif n2 > n1 > n3:
    print("\n el número mayor es: {} y el segundo mayor es {} ".format(n2,n1))
elif n1 > n2 > n3:
    print("\n el número mayor es: {} y el segundo mayor es {} ".format(n1,n2))
elif n1 > n3 > n2:
    print("\n el número mayor es: {} y el segundo mayor es {} ".format(n1,n3))
print("\nHAY NÚMEROS REPETIDOS: tienes que poner números distintos")
