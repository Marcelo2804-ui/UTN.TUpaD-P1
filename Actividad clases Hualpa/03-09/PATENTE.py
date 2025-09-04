#PATENTE
''' En el siguiente ejercicio hay que pasar una patente (arg) que ingresa el usuario a un valor numerico. 
Para tener en cuenta las patentes argentinas son por ejemplo AAA000, serian 3 letras al inicio y tres numeros.
El programa debe convertir las letras a numeros (A=1, B=2, C=3, etc) y luego concatenar los numeros al final. '''

 #EJERCICIO INGRESAR PATENTE DEVUELVE NUMERO

patent = input('Ingresa la patente (formato AAA000): ')


if len(patent) != 6 or not patent[:3].isalpha() or not patent[3:].isdigit():
    print('Formato de patente inválido.')

else:
    # convertir letras a números
    letters = patent[:3]# el [:3] toma las 3 primeras posiciones del length (0,1,2)
    numbers = patent[3:] # el [3:] toma las 3 últimas posiciones del length (3,4,5)
    value = ''
    for letter in letters:
        value += str(ord(letter.upper()) - 64)  # A=1, B=2, C=3, etc.
    value += numbers
    print(f'El valor numérico de la patente es: {value}')



# EJERCICIO INGRESAR NUMERO DEVUELVE PATENTE
number_2 = int(input('Ingresa un número de 6 dígitos (formato 000000): ')) 

MINIMUM_PATENT = 000000 # AAA000
MAXIMUM_PATENT = 17576000 # ZZZ999


if number_2 < MINIMUM_PATENT or number_2 > MAXIMUM_PATENT:
    print('Número para patente inválido.')

else:
    # separar letras y numeros
    letter_num = number_2 // 1000 # cociente para llegar a AAA
    numbers_2 = number_2 % 1000 # resto para 000


    letter_2 = ''
    for i in range(3):    # resto [ 0, 25 ]
        letter_2 = chr((letter_num % 26) + 65) + letter_2 # 65 = A, B= 66, etc, 90 = Z
        letter_num //= 26 # para avanzar al siguiente digito

new_patent = f'{letter_2} {numbers_2:03}' # 03 rellena de digitos

print(f'La patente correspondiente es: {new_patent}')