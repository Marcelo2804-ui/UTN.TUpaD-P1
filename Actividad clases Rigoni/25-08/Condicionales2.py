#lunes inicial | martes intermedio | miercoles avanzado | jueves practica hablada | viernes viajeros

#Validacion de datos de entrada
date = input(f'A continuacion ingrese la fecha con el siguiente formato: (dia, DD/MM): ')


parts = date.split(',')

if len(parts) != 2: # Usarlo sobre strings, no sobre INT
    print('Se produjo un error'); exit()


name_day = parts[0].strip()
name_day = name_day.lower()
date = parts[1].strip()

if '/' not in date: # Si no colocamos esto, el programa tira error si no esta la /, ej: lunes, 1212
    print('Se produjo un error'); exit()

date_day, date_month = date.split('/')

if len(date_day) != 2 or len(date_month) != 2: # Usarlo sobre strings, no sobre INT
    print('Se produjo un error'); exit()

date_day = int(date_day)
date_month = int(date_month)

#Diccionario de los dias y que se dicta
classes_day = {
    'lunes' : 'inicial',
    'martes' : 'intermedio',
    'miercoles' : 'avanzado',
    'jueves' : 'practica',
    'viernes' : 'viajeros'
} 

#Validacion de dias
if (date_day > 31 or date_day < 1):
    print('Se produjo un error'); exit()
elif (date_month > 12 or date_month < 1):
    print('Se produjo un error'); exit()
elif name_day not in classes_day:
    print('Se produjo un error'); exit()

#Validacion de examenes (lunes, martes, miercoles)
nivel = classes_day[name_day]
if (nivel == 'inicial' or nivel == 'intermedio' or nivel == 'avanzado'):
    answer = input('Se tomaron examenes?: si / no: ').lower()
    if (answer == 'si'):
        approved = int(input('Ingrese los aprobados: '))
        failed = int(input('Ingrese los desaprobados: '))
        total = float(approved + failed)

        if approved > 0:
            porc_approved = (approved / total) * 100
            print(f'El porcentaje de aprobados es de {porc_approved:.2f}%') # .2f usarlo en fstring para no usar round()
        else: 
            print('No hubo alumnos aprobados')

#Validacion de practica hablada (jueves)
if (nivel == 'practica'):
    porc_attendance = float(input('Ingrese el porcentaje de asistencia: '))
    if porc_attendance > 50: #Pide que sea mayor al 50%
        print('Asistio la mayoria')
    else:
        print('No asistio la mayoria')

#Validacion de viajeros (viernes)
if ((date_day == 1 and date_month == 1) or (date_day == 1 and date_month == 7)): #Solo funciona si es 01/01 o 01/07 indiferente del dia
    print('') # Espacio

    print('Comienzo de nuevo ciclo')
    students = int(input('Ingrese la cantidad de alumnos del nuevo ciclo: '))
    tariff = float(input('Ingrese el arancel en $ por cada alumno: $'))
    total_tariff = tariff * students # float
    print(f'El ingreso total es de ${total_tariff:.2f}')