#El resultado de cada ejercicio debe mostrarse por pantalla. Y las variables deben quedar todas en el archivo entregado.

#EJERCICIO 1
print('EJERCICIO 1')
numero1 = 14
print (numero1)

print('') # Espacio

#EJERCICIO 2
print('EJERCICIO 2')
numero2 = 7.3
print (numero2)

print('') # Espacio

#EJERCICIO 3
print('EJERCICIO 3')
suma = (numero1 + numero2)
print (suma)

print('') # Espacio

#EJERCICIO 4
print('EJERCICIO 4')
resta = (numero1 - numero2)
multiplicacion = (numero1 * numero2)
division = round(numero1 / numero2, 2)
print(resta)
print(multiplicacion)
print(division)

print('') # Espacio

#EJERCICIO 5
print('EJERCICIO 5')
nombre = 'Santiago'
print (nombre)

print('') # Espacio

#EJERCICIO 6
print('EJERCICIO 6')
precio = 777.99
print(precio)

print('') # Espacio

#EJERCICIO 7
print('EJERCICIO 7')
descuento = 0.50
print(f'{descuento}%')   

print('') # Espacio

#EJERCICIO 8
print('EJERCICIO 8')
precio_final = round((precio * descuento), 2) # $388.995
print(f'${precio_final}')

print('') # Espacio

#EJERCICIO 9
print('EJERCICIO 9')
cadena = 'Hola como estas'
print(cadena)

print('') # Espacio

#EJERCICIO 10
print('EJERCICIO 10')
longitud = len(cadena) #Empieza desde el 1
print (longitud)

print('') # Espacio 

#EJERCICIO 11
print('EJERCICIO 11')
precio = 7.33
precio = int(precio)
tipo_precio = type(precio)
print(f'{precio}\n{tipo_precio}')

print('') # Espacio

#EJERCICIO 12
print('EJERCICIO 12')
nombre = 'Pepe'
apellido = 'Argento'
nombre_completo = (f'{nombre} {apellido}')
print(nombre_completo)

print('') # Espacio

#EJERCICIO 13
print('EJERCICIO 13')
edad = 20
print(edad)
edad = edad + 5
print(f'{edad} (Edad incrementada + 5)')
edad = edad - 10
print (f'{edad} (Edad disminuida - 10)')

print('') # Espacio

#EJERCICIO 14
print('EJERCICIO 14')
altura = 1.70
print(altura)
altura = altura * 4
print(f'{altura} (Altura multiplicada por 4)')
altura = round(altura / 3, 2)
print(f'{altura} (Altura dividida por 3)')

print('') # Espacio

#EJERCICIO 15
print('EJERCICIO 15')
mi_nombre = 'SANTIAGO BARRETTO'
print(mi_nombre)
mi_nombre_minusc = mi_nombre.lower()
print(f'{mi_nombre_minusc} (En minusculas)')

print('') # Espacio 

#EJERCICIO 16
print('EJERCICIO 16')
mi_nombre_mayus = mi_nombre.capitalize()

#mi_nombre_mayus = mi_nombre.title()  // Hace que se ponga mayuscula la primera letra despues de un espacio

print(mi_nombre_mayus)

print('') # Espacio 