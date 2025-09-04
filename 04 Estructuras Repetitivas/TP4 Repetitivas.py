
# RESPETAR TILDES Y PUNTOS FINALES

#Ejercicio 1
print ('Ejercicio 1')

for num in range(101):
    print(num)

print('')

#Ejercicio 2
print ('Ejercicio 2')

user_num = int(input('Ingrese un número entero: '))


n = abs(user_num) # se convierte en positivo

if n == 0:
    digits = 1
else:
    digits = 0
    while n > 0:
        n //= 10   # se quita el ultimo digito
        digits += 1

print(f'Tu número, "{user_num}" tiene {digits} dígito/s.')



print('')

#Ejercicio 3 
print ('Ejercicio 3')

num_a = int(input('Ingrese el primer número: '))
num_b = int(input('Ingrese el segundo número: '))


if num_a > num_b:
    num_a, num_b = num_b, num_a # num_a sea menor para que funcione la logica

counter = num_a + 1  # número siguiente a num_a
result = 0

while counter < num_b:  # mientras no lleguemos a num_b (num anterior)
    result += counter
    counter += 1 # 
    # print(result) (1 y 4) = (2+3) = 5

print(f'La suma entre los numeros comprendidos {num_a} y {num_b} es: {result}')


print('')

#Ejercicio 4
print ('Ejercicio 4')

from colorama import Fore, Style, init #pip install colorama

init(autoreset=True)

print(f'{Fore.CYAN}Recuerda, si desea salir, imprima un 0.')

result_4 = 0
user_num = None # ya que si colocamos 0 no entra en el bucle

while user_num != 0:
    user_num = int(input('Ingrese números para sumarlos: '))
    result_4 += user_num
    print(f'Su suma de números va siendo de: {result_4}') 
    
print(f'{Fore.MAGENTA}La suma final es de: {result_4}') 

print('')

#Ejercicio 5
print ('Ejercicio 5')

import random 

bot_num = random.randint(0,10) # random
user_num5 = int(input('Ingresa un número entre 0 y 9: ')) # usuario

counter = 1 

while bot_num != user_num5:
    counter += 1
    user_num5 = int(input(f'{Fore.RED} INCORRECTO. ingresa otro número entre 0 y 9: '))

print(f'{Fore.GREEN} CORRECTO El número era {bot_num}')
print(f'Tuviste que intentarlo {counter} veces.')

print('')

#Ejercicio 6
print ('Ejercicio 6')

for num_6 in range(100, -1, -1): # 100 a 0 | con paso -1
    if num_6 % 2 == 0:
        print(num_6)

print('')

#Ejercicio 7
print ('Ejercicio 7')

# Reciclar ejercicio 3

user_num7 = int(input('Ingrese el número: '))

counter = 1
result = 0

while counter < user_num7:  # mientras no lleguemos a user_num7 (num anterior)
    result += counter
    counter += 1 # 
    # print(result) (0 y 4) = (1+2+3) = 6

print(f'La suma entre los números comprendidos entre 0 y {user_num7} es: {result}')

print('')

#Ejercicio 8
print ('Ejercicio 8')

even = 0 # par
odd = 0 # impar
negative = 0 # positivo
positive = 0 # negativo


for user_num8 in range(100):
    user_num8 = int(input('Ingrese un número: '))

    if user_num8 % 2 == 0: # PAR
        even += 1
    elif user_num8 % 2 != 0: # IMPAR
        odd += 1
    
    if user_num8 < 0: # NEGATIVO
        negative += 1
    elif user_num8 > 0: # POSITIVO
        positive += 1

print(f' Los números pares ingresados son: {even} \n ' 
f'Los números impares ingresados son: {odd} \n ' 
f'Los números negativos ingresados son: {negative}\n ' 
f'Los números positivos ingresados son: {positive} \n ')

print('')

#Ejercicio 9
print ('Ejercicio 9')

from statistics import mode, median, mean #moda, mediana, media

numbers = [] # lista para ir guardando los numeros del usuario

for counter_9 in range(5):
    user_num9 = int(input('Ingrese un número: '))
    numbers.append(user_num9) # va a ir guardando los numeros en la lista

user_mean = mean(numbers)

print(f'La media de los números ingresados es: {user_mean}')

print('')

#Ejercicio 10
print ('Ejercicio 10')

reversed_num = 0

user_num10 = input ('Ingrese un número: ')
if user_num10.isdigit():
    reversed_num = user_num10[::-1] # slicing para invertir el orden (forma mas sencilla)
    print(f'El número invertido es: {int(reversed_num)}')

else:
    print('No es un número.')

""" while user_num10 > 0:
    digit = user_num10 % 10       # tomo el último dígito
    reversed_num = reversed_num * 10 + digit  # lo voy agregando al invertido
    user_num10 //= 10             # elimino el último dígito """ # forma matematica

print('')