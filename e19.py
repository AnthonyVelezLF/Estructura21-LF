#ejercicio19
masa=float(input("Ingrese su masa (en libras): "))
e=float(input("Ingrese su estatura (en centimetros): "))
kg=masa*0.45359237
m=e/100
icm=kg/(m**2)
print("\nSu peso es: {}".format(kg))
print("El valor de su ICM es: {}".format(icm))
if icm < 16:
    print("Su clasificación es: Criterio de ingreso")
elif icm < 17:
    print("Su clasificación es: Infra peso")
elif icm < 18.5:
    print("Su clasificación es: Bajo peso")
elif icm < 25:
    print("Su clasificación es: Peso normal")
elif icm < 30:
    print("Su clasificación es: Sobrepeso")
elif icm < 35:
    print("Su clasificación es: Obesidad pre-mórbida.")
elif icm < 45.1 and icm > 39.9:
    print("Su clasificación es: Obesidad mórbida")
elif icm > 45:
    print("Su clasificación es: Obesidad híper-mórbida")