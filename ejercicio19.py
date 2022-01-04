#vamos a realizar una aplicacion si un padre puede asistir
#al juego de su hijo
#siempre y cuando este de vacaciones o tenga un dia de descanso
print("El juego de su hijo es el Sabado \n")
vacacion = input("Ese día está de vacaciones?: ")
libre = input("Ese día tiene libre?: ")
si= "si"
no= "no"
if  (vacacion == si) or (libre == si):
    print("Si puede")
elif (vacacion == no) or (libre == no):
    print("No puede")


