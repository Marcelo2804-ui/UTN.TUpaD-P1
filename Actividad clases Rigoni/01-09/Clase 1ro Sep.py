def encriptar_mensaje(mensaje, corrimiento):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    mensaje_encriptado = ""
    for caracter in mensaje:
        caracter_lower = caracter.lower() 
        if caracter_lower in alfabeto:
            indice_actual = alfabeto.find(caracter_lower)
            nuevo_indice = (indice_actual + corrimiento) % 27
            nueva_letra = alfabeto[nuevo_indice]
            if caracter.isupper():
                mensaje_encriptado += nueva_letra.upper()
            else:
                mensaje_encriptado += nueva_letra
        else:
            mensaje_encriptado += caracter
    return mensaje_encriptado
corrimiento = int(input("Ingresa el valor del corrimiento (un número entero): "))
mensajes_originales = [
    "Mensaje para oficial 1: ATACAR AL AMANECER",
    "Mensaje para oficial 2: LA CLAVE ES EXTRA",
    "Mensaje para oficial 3: MUEVANSE AL SECTOR G",
    "Mensaje para oficial 4: ESTO ES UNA PRUEBA",
    "Mensaje para oficial 5: ZETA ALFA OMEGA",]
print("\n--- Mensajes encriptados ---")
for i, mensaje_original in enumerate(mensajes_originales):
    mensaje_encriptado = encriptar_mensaje(mensaje_original, corrimiento)
    print(f"Mensaje {i+1} encriptado: {mensaje_encriptado}")