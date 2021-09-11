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
ganancias_dia = []

for i in range(5):
    puntos_dias.append(int(input(f"Ingrese los puntos del día {i+1}: ")))
    ganancias_dia.append(int(input(f"Ingrese las ganancias del día {i+1}: ")))

puntos_total = sum(puntos_dias)
ganancias_total = sum(ganancias_dia)

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

# 5. Una persona se encuentra con un problema de comprar un automóvil o un
# terreno, los cuales cuestan exactamente lo mismo. Sabe que mientras el
# automóvil se devalúa, con el terreno sucede lo contrario. Esta persona
# comprará el automóvil si al cabo de tres años la devaluación de este no es
# mayor que la mitad del incremento del valor del terreno. Ayúdale a esta
# pesona a determinar si debe o no comprar el automóvil.

precio_autoT = float(input("Ingrese el valor del automóvil y terreno: $"))
incremento = float(input("Ingrese el incremento anual del terreno en %: "))
devaluacion = float(input("Ingrese la devaluación anual del automóvil en %: "))

incremento = (((precio_autoT * incremento) / 100) * 3) / 2
devaluacion = ((precio_autoT * devaluacion) / 100) * 3
print(f"La mitad del incremento del terreno en 3 años es de: ${incremento}")
print(f"La devaluación del automóvil en 3 años es de: ${devaluacion}")

if devaluacion < incremento:
    print("Al cliente le conviene comprar el automóvil")
else:
    print("Al cliente le conviene comprar el terreno")

# 6. En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que compre. Si las
# computadoras son menos de cinco se les dará un 10% de descuento sobre el
# total de la compra; si el número de computadoras es mayor o igual a cinco
# pero menos de diez se le otorga un 20% de descuento; y si son 10 o más se
# les da un 40%. El precio de cada computadora es de $11.000.

num_computadores = int(input("Ingrese número de computadores a comprar: "))
total_comp = num_computadores * 11000

if num_computadores > 10:
    descuento = total_comp - (total_comp * 0.4)
    print(f"El total con el 40% de descuento es de: ${descuento}")
    print(f"El descuento del 40% es de: ${total_comp * 0.4}")
elif num_computadores >= 5 and num_computadores < 10:
    descuento = total_comp - (total_comp * 0.2)
    print(f"El total con el 20% de descuento es de: ${descuento}")
    print(f"El descuento del 20% es de: ${total_comp * 0.2}")
else:
    descuento = total_comp - (total_comp * 0.1)
    print(f"El total con el 10% de descuento es de: ${descuento}")
    print(f"El descuento del 10% es de: ${total_comp * 0.1}")

# 7. Un proveedor de estéreos ofrece un descuento del 10% sobre el precio
# sin IVA, de algún aparato si este cuesta $2000 o más. Además,
# independientemente de esto, ofrece un 5% de descuento si la marca es NOSY.
# Determinar cuanto pagará, con IVA incluido, un cliente cualquiera por la
# compra de su aparato. IVA es del 16%.

precio_aparato = float(input("Ingrese precio del aparato: $"))
marca = input("Ingrese marca del aparato: ")

if (marca == "NOSY" or marca == "nosy") and precio_aparato >= 2000:
    descuentoAparato = precio_aparato * 0.15
elif precio_aparato >= 2000:
    descuentoAparato = precio_aparato * 0.1

total = precio_aparato - descuentoAparato
total_iva = total + (total * 0.16)

print(f"El total a pagar con IVA y descuento es: ${total_iva:,}")
print(f"El total con descuento es: ${total:,}")
print(f"Con un descuento de ${descuentoAparato:,}")

# 8. Una empresa quiere hacer una compra de varias piezas de la misma clase a
# una fábrica de refacciones. La empresa, dependiendo del monto total de la
# compra, decidirá que hacer para pagar al fabricante. Si el monto total de la
# compra excede de $500.000 la empresa tendrá la capacidad de invertir de su
# propio dinero un 55% del monto de la compra, pedir prestado al banco un 30%
# y el resto lo pagará solicitando un crédito al fabricante. Si el monto total
# de la compra no excede de $500.00 la empresa tendrá capacidad de invertir de
# su propio dinero un 70% y el restante 30% lo pagará solicitando crédito
# al fabricante. El fabricante cobra por concepto de interes un 20% sobre la
# cantidad que se le pague a crédito. Obtener la cantidad a inverir, valor del
# préstamo, valor del crédito y los intereses.

monto_compra = float(input("Ingrese monto total de la compra: $"))

if monto_compra > 500000:
    inversion = monto_compra * 0.55
    prestamo = monto_compra * 0.3
    credito = monto_compra * 0.15
else:
    inversion = monto_compra * 0.7
    prestamo = 0
    credito = monto_compra * 0.3

interes = credito * 0.2

print(f"La cantidad a invertir es de: ${inversion:,}")
print(f"El valor del préstamo es de: ${prestamo:,}")
print(f"El valor del crédito es de: ${credito:,}")
print(f"Los intereses son de: ${interes}")
