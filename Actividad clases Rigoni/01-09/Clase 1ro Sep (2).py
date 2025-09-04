import random

ganadas_jugador = 0
ganadas_computadora = 0

opciones = ["piedra", "papel", "tijera"]

print("¡Bienvenido al a la tercera ronda del juego del calamar! hoy jugaremos piedra, papel o tijera")
while True:

    print("\n--- ¡Elige tu jugada!y preparate para la batalla! ---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    opcion_jugador_str = input("Ingresa el número que dictara tu destino (1-4): ")
    if opcion_jugador_str == "4":
        break
    if opcion_jugador_str not in ["1", "2", "3"]:
        print("Por favor, elige un número del 1 al 4. NO te hagas el loco") 
        continue  
    opcion_jugador = opciones[int(opcion_jugador_str) - 1]
    opcion_computadora = random.choice(opciones)
    print(f"\nTu jugada: {opcion_jugador.upper()}")
    print(f"La jugada de la computadora: {opcion_computadora.upper()}")
    if opcion_jugador == opcion_computadora:
        print("¡Es un empate! 🤝")
    elif (opcion_jugador == "piedra" and opcion_computadora == "tijera") or \
         (opcion_jugador == "tijera" and opcion_computadora == "papel") or \
         (opcion_jugador == "papel" and opcion_computadora == "piedra"):
        print("¡Ganaste! 🎉")
        ganadas_jugador += 1
    else:
        print("¡Tranquilo campeon todas las IAS perdieron con Atari pero vos lo hiciste conmigo! 😢")
        ganadas_computadora += 1
    print(f"\n--- Marcador ---")
    print(f"Tú: {ganadas_jugador} | Computadora: {ganadas_computadora}")
    print(f"Pobre Mortal: {ganadas_computadora} | Terminator IA: {ganadas_jugador}")
print("\n--- Fin del juego ---")
print(f"Resultado final: Tú ganaste {ganadas_jugador} partidas y la computadora ganó {ganadas_computadora} partidas.")
if ganadas_jugador > ganadas_computadora:
    print("¡Eres el campeón! 🏆")
elif ganadas_computadora > ganadas_jugador:
    print("¡Fuiste eliminado por Terminator IA! 💀")
else:
    print("No se si decir que fue suerte o que sos bueno, pero fue un empate. 🤝")
