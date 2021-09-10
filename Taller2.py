# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:58:14 2021

@author: laura
"""

import random

# Taller condiconales

# 1. Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# de 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.

num_camisas = int(input("Ingrese cantidad de camisas a comprar: "))
valor_camisas = float(input("Ingrese valor por camisa: $"))
total = num_camisas*valor_camisas
print(f"El total sin descuento es: ${total:,}")

if num_camisas >= 3:
    total = total - (total * 0.30)
    print(f"El total con un 30% de descuento es: ${total:,}")
else:
    total = total - (total * 0.10)
    print(f"El total con un 10% de descuento es: ${total:,}")

# 2. En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

num_aleatorio = random.randint(0, 100)
totalCompra = float(input("Ingrese total de la compra: $"))
print(f"El número aleatorio es: {num_aleatorio}")

if num_aleatorio >= 74:
    descuento = totalCompra * 0.2
    total = totalCompra - descuento
    print(f"El 20% de descuento es de: ${descuento:,}")
    print(f"El total con un 20% de descuento es: ${total:,}")
else:
    descuento = totalCompra * 0.15
    total = totalCompra - descuento
    print(f"El 20% de descuento es de: ${descuento:,}")
    print(f"El total con un 15% de descuento es: ${total:,}")

# 3. Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que conssite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente.

monto = float(input("Ingrese monto de la fianza: $"))

if monto < 50000:
    interes = monto * 0.03
    monto_interes = monto + interes
    print(f"El interés del 3% es: ${interes:,}")
    print(f"La cuota con un 3% es: ${monto_interes:,}")
else:
    interes = monto * 0.02
    monto_interes = monto + interes
    print(f"El interés del 2% es: ${interes:,}")
    print(f"La cuota con un 2% es: ${monto_interes:,}")
