# PFO 2 - API REST con Flask

## Descripción

Aplicación cliente-servidor desarrollada en Python utilizando Flask y SQLite.

El sistema permite:

- Registro de usuarios
- Login seguro
- Hash de contraseñas con bcrypt
- Consulta de tareas
- Cliente en consola

## Tecnologías utilizadas

- Python
- Flask
- SQLite
- bcrypt
- Requests

## Funcionalidades

### Registro de usuarios
Endpoint:
POST /registro

Permite registrar usuarios almacenando la contraseña de forma segura mediante hashing.

### Login
Endpoint:
POST /login

Verifica credenciales del usuario utilizando bcrypt.

### Tareas
Endpoint:
GET /tareas

Devuelve una lista de tareas en formato JSON.

## Archivos del proyecto

- servidor.py → API Flask
- cliente.py → Cliente consola
- usuarios.db → Base de datos SQLite

## Instalación

Instalar dependencias:

pip install flask bcrypt requests

## Ejecución

Ejecutar servidor:

python servidor.py

Ejecutar cliente:

python cliente.py

## Repositorio

https://github.com/rodrigochico2023/pfo2-api-flask