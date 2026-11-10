#!/usr/bin/env python3
import sys

for linea in sys.stdin:
    linea = linea.strip()
    
    if not linea or linea.startswith("id,"):
        continue 
    
    campos = linea.split(",")
    if len(campos) != 8:
        continue 
    
    try:
        tienda = campos[2]
        cantidad = float(campos[5])
        precio_unitario = float(campos[6])
        
        ingreso = cantidad * precio_unitario
        # Emitimos: Tienda \t Ingreso,Conteo(1)
        print(f"{tienda}\t{ingreso},1")
    except Exception:
        continue