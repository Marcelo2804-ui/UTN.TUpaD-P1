#Ejercicio 2 Clase
print ('Ejercicio 2 {Clase}')

name = input('Ingrese su nombre: ').title()
surname = input('Ingrese su apellido: ').title()
id_patient = input('Ingrese su numero de DNI (Solo numeros): ') # 'ID' es palabra reservada

if len(id_patient) < 7 or len(id_patient)>10 or not id_patient.isdigit(): #Si es argentino
    print('DNI Invalido')
    exit()

age = int(input('Ingrese su edad: '))
health_insurance = input('¿Posee obra social? [Si/No]: ').lower() #obra social
priority = int(input(
'Ingrese su prioridad (En numero)\n ' \
'1: Emergencia\n ' 
'2: Urgencia\n ' 
'3: Control\n '))

if priority == 1:
    attention = 'Asignar a emergencia'
elif priority == 2:
    if health_insurance == 'si':
        attention = 'Turno en menos de 24 hs'
    else:
        attention = 'Turno en menos de 48 hs'
elif priority == 3:
    if age > 65:
        attention = 'Turno preferencial en 72 hs'
    else:
        attention = 'Turno normal en 7 dias'

print(f'✔ Paciente: {name} {surname}')
print(f'DNI: {id_patient}')
print(f'Edad: {age}')
print(f'Prioridad: {priority}')
print(f'Turno asignado: {attention}')

print('')

#📘 Ejercicios de Tarea — Programación 1 

#Ejercicio 1
print ('Ejercicio 1')

name1 = input('Ingrese su/s nombre/s: ').title()
surname1 = input('Ingrese su/s apellido/s: ').title()
age1 = int(input('Ingrese su edad: '))
annual_income = float(input('Coloque su ingreso anual: '))

if annual_income < 500000: #500k
    tax = 0
elif annual_income < 2000000: #2M
    tax = 0.1
elif annual_income < 5000000: #5M
    tax = 0.2
else:
    tax = 0.35

if (age1 > 65) and (annual_income > 500000):
    tax *= 0.5 #Reduccion del 50%, si hacia /= multiplicaba * 2

tax_amount = annual_income * tax

if tax == 0:
    user_tax = 'No paga impuestos.'
else:
    user_tax = (f'Paga: {tax*100:.1f}%') #No colocar print

print(f'✔ Nombre completo: {name1} {surname1}')
print(f'Ingresos: ${annual_income}')
print(f'Edad: {age1}')
print(f'Impuesto final: {user_tax}')

print('')

#Ejercicio 2
print ('Ejercicio 2')

from colorama import Fore, Style, init #pip install colorama

init(autoreset=True) #Inicializar colorama y se resetee conc ada print


name2 = input('Ingrese su nombre: ').title()
student_file = int(input('Ingrese su legajo (Solo numeros): '))
grades = [] #Lista de las notas
for i in range(3): #Usar for porque ya se de antemano que son 3 notas
    user_grade = int(input(f'Ingrese la nota {i+1} (Enteros entre 0 y 10): '))
    grades.append(user_grade)

mean = sum(grades) / 3 #Suma lo de dentro de la lista grades

if any(grade < 4 for grade in grades): #Revisa en la lista grades si hay alguna nota menor a 4
    status = f'{Fore.RED}Desaprobado directo'

elif mean < 6:
    status = f'{Fore.RED}Desaprobado' #Si uso print, da None

elif 6 <= mean < 8:
    status = f'{Fore.YELLOW}Aprobado con final'
else:
    status = f'{Fore.GREEN}Promocionado'

print(f'✔ Alumno: {Fore.CYAN} {name2}')
print(f'Legajo: {Fore.CYAN} {student_file}')
print(f'Notas: {Fore.CYAN} {grades}')
print(f'Promedio: {Fore.CYAN} {mean:.2f}')
print(f'Estado académico: {status}')

print('')

#Ejercicio 3
print ('Ejercicio 3')

from colorama import Fore, init

init(autoreset=True)

# Datos del usuario
user_name = input('Ingrese su nombre: ').title()
user_pin = input('Ingrese su PIN (Solo números): ')
initial_balance = 50000  # Saldo inicial fijo en el sistema

# Verifica el PIN (3 intentos)
for attempt in range(3):
    pin = input('Coloque su PIN: ')
    if pin == user_pin:
        print(f'{Fore.GREEN}PIN correcto\n')
        break
    else:
        print(f'{Fore.RED}PIN incorrecto. Intento {attempt+1} de 3')
else:
    print(f'{Fore.RED}Demasiados intentos fallidos. Cuenta bloqueada')
    exit()

# Retiro de dinero
while True:
    print(f'Usted tiene ${initial_balance}')
    withdraw = input("Si desea cancelar, escriba 'cancelar'\nIngrese lo que desea retirar: $")

    if withdraw.lower() == 'cancelar':
        print(f'{Fore.CYAN}\nHasta luego')
        break

    # Verifica si se coloca numero
    if not withdraw.isdigit():
        print(f'{Fore.RED}Debe ingresar un numero valido.')
        continue

    withdraw = float(withdraw)

    # Validaciones
    if withdraw % 1000 != 0:
        print(f'{Fore.RED}El monto debe ser multiplo de 1000.')
        continue

    if withdraw > initial_balance:
        print(f'{Fore.RED}El monto supera su saldo disponible.')
        continue

    # Comisión si supera 20.000
    if withdraw > 20000:
        commission = withdraw * 0.02
        total_withdraw = withdraw + commission
        if total_withdraw > initial_balance:
            print(f'{Fore.RED}Saldo insuficiente')
            continue
        print(f'{Fore.YELLOW}Se cobrará una comision del 2% (${commission}).')
        withdraw = total_withdraw

    # Actualizar saldo
    initial_balance -= withdraw
    print(f'{Fore.GREEN}Retiro hecho. Su saldo actualizado es: ${initial_balance}')


print('')

#Ejercicio 4
print ('Ejercicio 4')

name4 = input('Ingrese su nombre: ').title()
age4 = int(input('Ingrese su edad: '))
years_experience = int(input('Ingrese sus años de experiencia conduciendo: '))

if age4 < 18:
    result = 'No puede conducir'
elif age4 < 21 and years_experience < 1:
    result = 'Principiante'
elif age4 < 30 and ( 1 <= years_experience <= 5):
    result = 'Conductor intermedio'
elif age4 >= 30 and (years_experience > 10):
    result = 'Conductor profesional'
else:
    result = 'Conductor estándar'

if age4 >= 18:
    print(f'Usted es un {result}') # Suena raro si tiene menos de 18 años
else:
    print(result)

print('')

#Ejercicio 5
print ('Ejercicio 5')

name5 = input('Ingrese su nombre: ').title()
products = int(input('Ingrese la cantidad de productos: '))
total_purchase = float(input('Ingrese el total de su compra: '))

if products < 1:
    print('INCORRECTO, no puede llevar menos de 1 producto')
    exit()

if total_purchase < 0:
    print('INCORRECTO, no hay productos gratis ni con precio negativo')
    exit()

payment_method = input('Que medio de pago utilizara: (efectivo/debito/credito/MP): ').lower()

# Diccionario de metodos de pago
methods = {
    'efectivo': -0.15,  # Descuento 15%
    'debito': -0.10,    # Descuento 10%
    'credito': 0.05,    # Recargo 5%
    'mp': -0.20         # Descuento 20% pero si supera los 10k
}

# Verificacion de methods
if payment_method not in methods:
    print('Medio de pago invalido')
    exit()

# Verificar descuento de MP
pm_rate = methods[payment_method]  # pm abreviacion de payment_method
if payment_method == 'mp' and total_purchase <= 10000:
    pm_rate = 0.0  # Sin descuento

# Calcular segun medio de pago
pm_amount = total_purchase * pm_rate  # Negativo (descuento) | Positivo (recargo)
subtotal = total_purchase + pm_amount

# Defino las variables que se van a usar
extra_rate = 0.0
extra_rate_str = '0%'
extra_amount = 0.0
final_total = subtotal

# Si el cliente compro mas de 10 productos
if products > 10:
    extra_rate = -0.05
    extra_rate_str = f'{-extra_rate*100:.0f}%'  # muestra "5%"
    extra_amount = subtotal * extra_rate
    final_total = subtotal + extra_amount

print(f'{Fore.MAGENTA} ---- Resumen de compra ---- ')
print(f'Cliente: {name5}')
print(f'Cantidad de productos: {products}')
print(f'Total inicial: ${total_purchase:.3f}')
print(f'Medio de pago: {payment_method}')
print(f'Ajuste por medio de pago: ${pm_amount:.3f}')
print(f'Subtotal tras medio de pago: ${subtotal:.3f}')

if extra_rate != 0:  # Si compro mas de 10
    print(f'Descuento por comprar mas de 10 productos ({extra_rate_str}): ${extra_amount:.3f}')

print(f'Total a pagar: ${final_total:.3f}')

print('')