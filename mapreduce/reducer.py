#!/usr/bin/env python3
import sys

tienda_actual = None
ingreso_total = 0.0
conteo_tickets = 0

for linea in sys.stdin:
    linea = linea.strip()
    try:
        tienda, valores = linea.split('\t', 1)
        ingreso_str, conteo_str = valores.split(',')
        ingreso = float(ingreso_str)
        conteo = int(conteo_str)
    except ValueError:
        continue

    if tienda_actual == tienda:
        ingreso_total += ingreso
        conteo_tickets += conteo
    else:
        if tienda_actual:
            # Calculamos el ticket promedio (Ingreso / Cantidad de ventas)
            ticket_promedio = ingreso_total / conteo_tickets
            print(f"{tienda_actual}\t{ticket_promedio}")
        tienda_actual = tienda
        ingreso_total = ingreso
        conteo_tickets = conteo

# Imprimir la última tienda iterada
if tienda_actual == tienda:
    ticket_promedio = ingreso_total / conteo_tickets
    print(f"{tienda_actual}\t{ticket_promedio}")