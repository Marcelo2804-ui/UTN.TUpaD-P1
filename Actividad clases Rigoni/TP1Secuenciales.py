# primer ejercicio
print("Hola Mundo!") 
name_completo_input = input("Ingrese su nombre completo: ")

# segundo ejercicio
print(f"Mucho gusto, {name_completo_input}") 
print(f"Me presento soy un programa en desarrollo")
nacionalidad = input(f"{name_completo_input}, de que pais eres? ")
edad = input("cual es tu edad? ")

# tercer ejercicio
print(f"{nacionalidad}, que bello pais, ademas tienes {edad} años. ") 

#ejercicio 4 
import math 
radio_str = input(f"{name_completo_input} me dirias el radio, asi calculamos area y perimetro? = ")
radio = float(radio_str)
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#ejercicio 5
segundos_str = input(f"{name_completo_input}, podrias ingresar una cantidad de segundos (asi afinamos mis mateticas): ")
segundos = float(segundos_str)
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

#ejercicio 6    
print(f"{name_completo_input} gracias por tu ayuda, seguimos con matematicas! :)")
numero_str = input("Ingresa un número para ver su tabla de multiplicar: ")
numero = int(numero_str)
print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#Ejercicio 7
print(f"{name_completo_input} , yo tambien estoy cansado pero la practica hace al maestro xD, te voy a solicitar 2 numeros para hacer unas operaciones.")
num1_str = input("Ingresa el primer número: ")
num2_str = input("Ingresa el segundo número: ")
num1 = float(num1_str)
num2 = float(num2_str)
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")

#Ejercicio 8 
print(f"{name_completo_input} Ahora toca saber el indice de masa corporal, te voy a pedir peso y altura(no uses coma)")
peso_str = input("Ingresa tu peso en kg: ")
altura_str = input("Ingresa tu altura en metros: ")
peso = float(peso_str)
altura = float(altura_str)
imc = peso / (altura**2)
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

#Ejercicio 9
print(f"{name_completo_input}, que pasa que mis circuitos se congelan?.. Ahhh eso me da una idea pasemos de Celius a Fahrenheit ")
celsius_str = input("Ingresa la temperatura en grados Celsius: ")
celsius = float(celsius_str)
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#Ejercicio 10
print(f"{name_completo_input}, se me terminaron las ideas, lo ultimo por hoy :D ")
num1_str = input("Ingresa el primer número: ")
num2_str = input("Ingresa el segundo número: ")
num3_str = input("Ingresa el tercer número: ")
num1 = float(num1_str)
num2 = float(num2_str)
num3 = float(num3_str)
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")

print(f"{name_completo_input}, Gracias por participar en mi aprendizaje") 

