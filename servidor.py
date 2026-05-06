from flask import Flask, request, jsonify
import sqlite3
import bcrypt

app = Flask(__name__)

# =========================
# CREAR BASE DE DATOS
# =========================

def crear_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        contraseña BLOB
    )
    """)

    conn.commit()
    conn.close()

# =========================
# INICIO
# =========================

@app.route("/")
def inicio():
    return "Servidor Flask funcionando correctamente"

# =========================
# REGISTRO
# =========================

@app.route("/registro", methods=["POST"])
def registro():

    datos = request.get_json()

    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    if not usuario or not contraseña:
        return jsonify({
            "error": "Faltan datos"
        }), 400

    contraseña_hash = bcrypt.hashpw(
        contraseña.encode("utf-8"),
        bcrypt.gensalt()
    )

    try:
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO usuarios (usuario, contraseña)
        VALUES (?, ?)
        """, (usuario, contraseña_hash))

        conn.commit()
        conn.close()

        return jsonify({
            "mensaje": "Usuario registrado correctamente"
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# =========================
# LOGIN
# =========================

@app.route("/login", methods=["POST"])
def login():

    datos = request.get_json()

    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT contraseña FROM usuarios
    WHERE usuario = ?
    """, (usuario,))

    resultado = cursor.fetchone()

    conn.close()

    if resultado:

        contraseña_guardada = resultado[0]

        if bcrypt.checkpw(
            contraseña.encode("utf-8"),
            contraseña_guardada
        ):

            return jsonify({
                "mensaje": "Login correcto"
            }), 200

    return jsonify({
        "error": "Usuario o contraseña incorrectos"
    }), 401

# =========================
# TAREAS
# =========================

@app.route("/tareas", methods=["GET"])
def tareas():

    lista_tareas = [
        "Estudiar Flask",
        "Realizar PFO",
        "Probar API REST"
    ]

    return jsonify({
        "tareas": lista_tareas
    })

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    crear_db()
    app.run(debug=True)