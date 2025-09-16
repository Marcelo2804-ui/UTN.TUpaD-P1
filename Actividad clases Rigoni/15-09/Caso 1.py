# Programa de gestión de biblioteca escolar usando listas paralelas

# Inicialización de listas
titulos = []
ejemplares = []

# Menú persistente
while True:
    print("\n--- Menú Biblioteca Escolar ---")
    print("1. Ingresar lista de títulos")
    print("2. Ingresar lista de ejemplares disponibles")
    print("3. Mostrar catálogo con stock")
    print("4. Consultar disponibilidad de un título")
    print("5. Listar títulos agotados")
    print("6. Agregar nuevo título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Ver catálogo")
    print("9. Salir")

    opcion = input("Seleccione una opción (1-9): ")

    if opcion == "1":
        titulos.clear()
        cantidad = int(input("¿Cuántos títulos desea ingresar?: "))
        for i in range(cantidad):
            titulo = input(f"Ingrese el título {i+1}: ").strip()
            if titulo != "":
                titulos.append(titulo)
            else:
                print("Título vacío no permitido.")
        ejemplares = [0] * len(titulos)

    elif opcion == "2":
        if len(titulos) == 0:
            print("Primero debe ingresar los títulos.")
        else:
            ejemplares.clear()
            for i in range(len(titulos)):
                while True:
                    try:
                        cantidad = int(input(f"Ingrese cantidad de ejemplares para '{titulos[i]}': "))
                        if cantidad >= 0:
                            ejemplares.append(cantidad)
                            break
                        else:
                            print("La cantidad debe ser cero o mayor.")
                    except:
                        print("Entrada inválida. Debe ser un número entero.")

    elif opcion == "3":
        if len(titulos) == 0:
            print("No hay títulos cargados.")
        else:
            print("\nCatálogo con stock:")
            for i in range(len(titulos)):
                print(f"{titulos[i]}: {ejemplares[i]} copias")

    elif opcion == "4":
        buscar = input("Ingrese el título a consultar: ").strip()
        if buscar in titulos:
            i = titulos.index(buscar)
            print(f"{buscar}: {ejemplares[i]} copias disponibles")
        else:
            print("Título no encontrado.")

    elif opcion == "5":
        agotados = []
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                agotados.append(titulos[i])
        if len(agotados) == 0:
            print("No hay títulos agotados.")
        else:
            print("Títulos agotados:")
            for titulo in agotados:
                print(titulo)

    elif opcion == "6":
        nuevo = input("Ingrese nuevo título: ").strip()
        if nuevo == "":
            print("Título vacío no permitido.")
        elif nuevo in titulos:
            print("El título ya existe.")
        else:
            while True:
                try:
                    cantidad = int(input("Ingrese cantidad inicial de ejemplares: "))
                    if cantidad >= 0:
                        titulos.append(nuevo)
                        ejemplares.append(cantidad)
                        print("Título agregado correctamente.")
                        break
                    else:
                        print("La cantidad debe ser cero o mayor.")
                except:
                    print("Entrada inválida. Debe ser un número entero.")

    elif opcion == "7":
        titulo = input("Ingrese el título a actualizar: ").strip()
        if titulo in titulos:
            i = titulos.index(titulo)
            print(f"Ejemplares actuales: {ejemplares[i]}")
            accion = input("¿Desea registrar un préstamo (P) o devolución (D)?: ").upper()
            if accion == "P":
                while True:
                    try:
                        cantidad = int(input("Cantidad a prestar: "))
                        if 0 <= cantidad <= ejemplares[i]:
                            ejemplares[i] -= cantidad
                            print("Préstamo registrado.")
                            break
                        else:
                            print("Cantidad inválida.")
                    except:
                        print("Entrada inválida.")
            elif accion == "D":
                while True:
                    try:
                        cantidad = int(input("Cantidad a devolver: "))
                        if cantidad >= 0:
                            ejemplares[i] += cantidad
                            print("Devolución registrada.")
                            break
                        else:
                            print("Cantidad inválida.")
                    except:
                        print("Entrada inválida.")
            else:
                print("Opción inválida.")
        else:
            print("Título no encontrado.")

    elif opcion == "8":
        if len(titulos) == 0:
            print("No hay títulos cargados.")
        else:
            print("Catálogo completo:")
            for titulo in titulos:
                print(titulo)

    elif opcion == "9":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
