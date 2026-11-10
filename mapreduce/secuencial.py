import time
import pandas as pd

start_time = time.time()
# Lee el CSV desde tu ruta real
df = pd.read_csv('scripts/ventas_125053802.csv')
df['ingreso'] = df['cantidad'] * df['precio_unitario']
# Agrupa por tienda y saca el promedio del ingreso
resultado = df.groupby('tienda')['ingreso'].mean().reset_index()

print(resultado)
print(f"Tiempo de ejecución secuencial: {time.time() - start_time} segundos")