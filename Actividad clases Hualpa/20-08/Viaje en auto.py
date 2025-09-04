""" Ejercicio 8: Viaje en auto
Un auto consume 8 litros cada 100 km. El usuario ingresa la distancia en km y el precio de la gasolina por litro.
El programa debe calcular:
cuántos litros se necesitan,
cuánto costará el viaje,
y cuántas horas tardará si la velocidad promedio es de 90 km/h. """

#Ejercicio 8
distancia = float(input("Ingrese la cantidad de km: "))
precio_nafta = float(input("Ingrese el precio de la gasolina por litro: "))

consumo_por_100km = 8 
velocidad_promedio = 90

litros_total = (distancia / 100) * consumo_por_100km
costo_total = litros_total * precio_nafta
tiempo_horas = distancia / velocidad_promedio 

litros_total_redondeado = round(litros_total, 2)
costo_total_redondeado = round(costo_total, 2)
tiempo_horas_redondeado = round(tiempo_horas, 2)

print("Se necesitan", litros_total_redondeado, "litros") #No anda print (f) en esta version de .py
print("El costo total del viaje es de: $", costo_total_redondeado)
print("El total de horas del viaje es de ", tiempo_horas_redondeado, "h")