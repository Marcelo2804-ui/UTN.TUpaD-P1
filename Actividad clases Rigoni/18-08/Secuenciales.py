#Calculadora de propinas en un restaurante
""" Pedir al usuario el monto total de la cuenta.

Calcular la propina sugerida al 10%.

Calcular la propina sugerida al 15%.

Calcular el total a pagar en ambos casos (cuenta + propina).

Mostrar todos los resultados en pantalla. """

total_amount = float(input('Ingrese el monto de la cuenta: '))

suggested_tip_1 = 0.10  #Usar variable por si despues se quisiera cambiar el porcentaje
suggested_tip_2 = 0.15 

discount_1 = total_amount * suggested_tip_1 #Usar varias variables por si hay un error en los calculos no rebuscar en el print
discount_2 = total_amount * suggested_tip_2

total_amount_with_disc1 = total_amount + discount_1
total_amount_with_disc2 = total_amount + discount_2

print(f'Propina sugerida ({int(suggested_tip_1*100)}%): {discount_1}')
print(f'Total a pagar ({int(suggested_tip_1*100)}%): {total_amount_with_disc1}')

print(f'Propina sugerida ({int(suggested_tip_2*100)}%): {discount_2}')
print(f'Total a pagar ({int(suggested_tip_1*100)}%): {total_amount_with_disc2}')