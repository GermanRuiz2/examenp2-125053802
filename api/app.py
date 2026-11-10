from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "db"),
        database=os.environ.get("POSTGRES_DB", "datamart"),
        user=os.environ.get("POSTGRES_USER", "admin"),
        password=os.environ.get("POSTGRES_PASSWORD", "admin")
    )

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id SERIAL PRIMARY KEY,
            clave VARCHAR(255),
            valor NUMERIC
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/resultados', methods=['GET'])
def get_resultados():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT clave, valor FROM resultados;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"tienda": r[0], "ticket_promedio": float(r[1])} for r in rows])

# Aquí el filtro es por tu clave de pregunta de negocio (la tienda)
@app.route('/resultados/<clave>', methods=['GET'])
def get_resultado_by_clave(clave):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT clave, valor FROM resultados WHERE clave = %s;", (clave,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"tienda": r[0], "ticket_promedio": float(r[1])} for r in rows])

@app.route('/resultados', methods=['POST'])
def create_resultado():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO resultados (clave, valor) VALUES (%s, %s);", (data['clave'], data['valor']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)