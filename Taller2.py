# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:58:14 2021

@author: laura
"""
# Taller condiconales

# 1. Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# de 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.

num_camisas = int(input("Ingrese cantidad de camisas a comprar: "))
valor_camisas = float(input("Ingrese valor por camisa: "))
total = num_camisas*valor_camisas
print(f"El total sin descuento es: ${total:,}")

if num_camisas >= 3:
    total = total - (total * 0.30)
    print(f"El total con un 30% de descuento es: ${total:,}")
else:
    total = total - (total * 0.10)
    print(f"El total con un 10% de descuento es: ${total:,}")
