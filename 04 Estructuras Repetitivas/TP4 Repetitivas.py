# RESPETAR TILDES Y PUNTOS FINALES

# Ejercicio 1
print('Ejercicio 1')

for num in range(101):
    print(num)

print('')

# Ejercicio 2
print('Ejercicio 2')

user_num = int(input('Ingrese un número entero: '))
n = abs(user_num)  # Lo convertimos en positivo para contar dígitos sin drama.

if n == 0:
    digits = 1
else:
    digits = 0
    while n > 0:
        n //= 10  # Le sacamos el último dígito.
        digits += 1

print(f'Tu número, "{user_num}" tiene {digits} dígito/s.')

print('')

# Ejercicio 3
print('Ejercicio 3')

num_a = int(input('Ingrese el primer número: '))
num_b = int(input('Ingrese el segundo número: '))

if num_a > num_b:
    num_a, num_b = num_b, num_a  # Aseguramos que num_a sea menor para que la lógica no se rompa.

counter = num_a + 1
result = 0

while counter < num_b:
    result += counter
    counter += 1

print(f'La suma entre los números comprendidos {num_a} y {num_b} es: {result}')

print('')

# Ejercicio 4
print('Ejercicio 4')

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    print("Colorama no está instalado. Ejecutá 'pip install colorama' para usar colores.")
    Fore = Style = lambda x: ''  # Fallback para que no explote el código.

print(f'{Fore.CYAN}Recuerda, si desea salir, imprima un 0.')

result_4 = 0
user_num = None

while user_num != 0:
    user_num = int(input('Ingrese números para sumarlos: '))
    result_4 += user_num
    print(f'Su suma de números va siendo de: {result_4}')

print(f'{Fore.MAGENTA}La suma final es de: {result_4}')

print('')

# Ejercicio 5
print('Ejercicio 5')

import random

bot_num = random.randint(0, 9)  # Número secreto entre 0 y 9.
user_num5 = int(input('Ingresa un número entre 0 y 9: '))
counter = 1

while bot_num != user_num5:
    counter += 1
    user_num5 = int(input(f'{Fore.RED}INCORRECTO. Intenta de nuevo: '))

print(f'{Fore.GREEN}CORRECTO. El número era {bot_num}.')
print(f'Tuviste que intentarlo {counter} veces.')

print('')

# Ejercicio 6
print('Ejercicio 6')

for num_6 in range(100, -1, -1):
    if num_6 % 2 == 0:
        print(num_6)

print('')

# Ejercicio 7
print('Ejercicio 7')

user_num7 = int(input('Ingrese el número: '))
counter = 1
result = 0

while counter < user_num7:
    result += counter
    counter += 1

print(f'La suma entre los números comprendidos entre 0 y {user_num7} es: {result}')

print('')

# Ejercicio 8
print('Ejercicio 8')

even = 0
odd = 0
negative = 0
positive = 0

for _ in range(100):
    user_num8 = int(input('Ingrese un número: '))

    if user_num8 % 2 == 0:
        even += 1
    else:
        odd += 1

    if user_num8 < 0:
        negative += 1
    elif user_num8 > 0:
        positive += 1

print(f'Los números pares ingresados son: {even}.')
print(f'Los números impares ingresados son: {odd}.')
print(f'Los números negativos ingresados son: {negative}.')
print(f'Los números positivos ingresados son: {positive}.')

print('')

# Ejercicio 9
print('Ejercicio 9')

from statistics import mean

numbers = []

for _ in range(5):
    user_num9 = int(input('Ingrese un número: '))
    numbers.append(user_num9)

user_mean = mean(numbers)
print(f'La media de los números ingresados es: {user_mean}')

print('')

# Ejercicio 10
print('Ejercicio 10')

user_num10 = input('Ingrese un número: ')

if user_num10.isdigit():
    reversed_num = user_num10[::-1]
    print(f'El número invertido es: {int(reversed_num)}')
else:
    print('No es un número.')

print('')
