import requests

URL = "http://127.0.0.1:5000"

def menu():

    while True:

        print("\n=== CLIENTE API ===")
        print("1. Registrar usuario")
        print("2. Login")
        print("3. Ver tareas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        # =========================
        # REGISTRO
        # =========================

        if opcion == "1":

            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")

            datos = {
                "usuario": usuario,
                "contraseña": contraseña
            }

            respuesta = requests.post(
                f"{URL}/registro",
                json=datos
            )

            print("\nRespuesta:")
            print(respuesta.json())

        # =========================
        # LOGIN
        # =========================

        elif opcion == "2":

            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")

            datos = {
                "usuario": usuario,
                "contraseña": contraseña
            }

            respuesta = requests.post(
                f"{URL}/login",
                json=datos
            )

            print("\nRespuesta:")
            print(respuesta.json())

        # =========================
        # VER TAREAS
        # =========================

        elif opcion == "3":

            respuesta = requests.get(
                f"{URL}/tareas"
            )

            datos = respuesta.json()

            print("\n=== LISTA DE TAREAS ===")

            for tarea in datos["tareas"]:
                print("-", tarea)

        # =========================
        # SALIR
        # =========================

        elif opcion == "4":

            print("Finalizando cliente...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()