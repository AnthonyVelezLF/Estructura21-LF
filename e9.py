#ejercicio9
n = int(input("Ingresa un número binario de 4 dígitos: "))
b = n
suma = 0
while b > 0 :
    suma=suma + b%10
    b = b//10
    r = (n)
    
if suma % 2 == 0:
    print("\nParidad Par:\n")
    print("     P     BCD     ")
    print("     0     {}     \n".format(str(n).zfill(4)))
    print("Paridad Inpar:\n")
    print("     P     BCD     ")
    print("     1     {}     \n".format(str(n).zfill(4)))

else:
    print("\nParidad Par:\n")
    print("     P     BCD     ")
    print("     1     {}     \n".format(str(n).zfill(4)))
    print("Paridad Inpar:\n")
    print("     P     BCD     ")
    print("     0     {}     \n".format(str(n).zfill(4)))
