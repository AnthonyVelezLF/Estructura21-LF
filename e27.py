#ejercicio27
c=int(input("Ingrese una contraseña de almenos 10 números: "))
d = len(str(c))
while d < 10:
     c=int(input("Ingrese una contraseña de almenos 10 números: "))
     d = len(str(c))
print("Contraseña Exitosa")