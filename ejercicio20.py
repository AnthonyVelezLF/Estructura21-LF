#Realice una aplicacion que permita solicitar el prestamo de un libro
#los datos serán: nombre persona, nombre del libro, id, precio, envio
#entrada
nombrePersona = input("Ingrese el nombre de la persona: ")
nombreLibro = input("Ingrese el nombre del libro: ")
codigoLibro = int(input("Ingrese el codigo del libro: "))
precioLibro = float(input("Ingrese el precio del libro: "))
envio = input("Ingrese si desea el envio a domicilio (SI/NO) o (si/no): ")
#proceso
if envio.strip == "SI" or  envio.strip == "si": #para que sirve stip ? 
    print("El usuario {} ha solicitado el envio del libro".format(nombrePersona))
else:
    print("El usuario {} NO ha solicitado el envio del libro".format(nombrePersona))
    