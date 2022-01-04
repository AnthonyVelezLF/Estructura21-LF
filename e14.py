#ejercicio14
print("Ingrese una horas y minutos en hh mm (separados con espacio): ", end=" ")
h, m = map(int, input().split())
s = (h*3600)+(m*60)
print("las horas y minutos es: {} hora(s):{} minuto(s)".format(h,m))

print("\nllevadas a SEGUNDOS es: {} segundos".format(s))