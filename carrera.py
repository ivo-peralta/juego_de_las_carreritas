
from Personaje import Personaje
def menu():
    print("1. Ingresar participantes")
    print("2. Correr carrera")
    print("3. salir")
    opcion = input("Seleccione una opción: ")
    return opcion
participantes = []
while True:
    opcion = menu()
    if opcion == "1":
        nombre = input("Ingrese el nombre del participante: ")
        altura = float(input("Ingrese la altura del participante: "))
        velocidad = float(input("Ingrese la velocidad del participante: "))
        resistencia = float(input("Ingrese la resistencia del participante: "))
        fuerza = float(input("Ingrese la fuerza del participante: "))
        participante = Personaje(nombre, altura, velocidad, resistencia, fuerza)
        participantes.append(participante)
        print(f"Participante {nombre} ingresado exitosamente.")
    elif opcion == "2":
        distancia = float(input("Ingrese la distancia a recorrer: "))
        for participante in participantes:
            participante.correr(distancia)
    elif opcion == "3":
        print("saliendo wachin")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")