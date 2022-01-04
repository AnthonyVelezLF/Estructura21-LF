#Aplicacion que determina si una persona es mayor de edad
#entrada
nombres = input("ingrese los nombres de la persona: ")
apellidos = input("Ingrese los apellidos de la persona: ")
edad = int(input("Ingrese la edad: "))
#proceso)
if edad >= 18:
    print(nombres+" "+apellidos+" tiene "+str(edad)+" años a la actualidad y es mayor de edad" )
else:
    print(nombres+" "+apellidos+" tiene "+str(edad)+" años a la actualidad y es menor de edad" )
    