import psycopg2
import sys

try:
    conn = psycopg2.connect(host="db", database="datamart", user="admin", password="admin")
    cur = conn.cursor()
    
    with open('/data/input/mapreduce/output/part-00000', 'r') as f:
        for linea in f:
            clave, valor = linea.strip().split('\t')
            cur.execute("INSERT INTO resultados (clave, valor) VALUES (%s, %s);", (clave, float(valor)))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Datos cargados a PostgreSQL exitosamente.")
except Exception as e:
    print(f"Error al cargar datos: {e}")