# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:58:14 2021

@author: laura
"""

import random
import numpy as np

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

# 4. Una fábrica ha sido sometida a un programa de control de contaminación
# para lo cual se efectúa una revisión de los puntos de contaminación
# generados por la fábrica. El programa de control de contaminación consiste
# en medir los puntos que emite la fábrica en cinco días de una semana y si el
# promedio es superior a los 170 puntos entonces tendrá la sanción de parar su
# producción por una semana y una multa del 50% de las ganancias diarias
# cuando no se detiene la producción. Si el promedio obtenido de puntos es de
# 170 o menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la revisión.

puntos_dias = []
ganancias_diarias = []

for i in range(5):
    puntos_dias.append(int(input(f"Ingrese los puntos del día {i+1}: ")))
    ganancias_diarias.append(int(input(f"Ingrese las ganancias del día {i+1}: ")))

puntos_total = sum(puntos_dias)
ganancias_total = sum(ganancias_diarias)

if puntos_total > 170:
    multa = ganancias_total * 0.5
    print(f"El promedio de puntos emitidos es de: {puntos_total}")
    print("Esta fábrica deberá tener una sanción de una semana")
    print(f"Las ganancias totales es de: ${ganancias_total:,}")
    print(f"La multa a pagar es de: ${multa:,}")
else:
    multa = 0
    print(f"Las ganancias totales es de: ${ganancias_total:,}")
    print("Esta fábrica no tendrá sanción")
    print(f"La multa a pagar es de: ${multa:,}")
