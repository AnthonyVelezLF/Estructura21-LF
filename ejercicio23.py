#si es primo o no
numero = int(input("Ingrese un numero: "))
antecesor=numero-1
cont = 0
residuo=0
while antecesor >1:
    cont= cont+1
    if numero&cont== 0:
        cont=cont+1
if cont < 2:
    print("si es primo")
else:
    print("no es primo")
    
