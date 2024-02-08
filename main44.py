#Reto dia 4

usuarios = {}
identificador_actual = 1

while True:
    print("\n--- Menú ---")
    print("1. Registrar nuevo usuario")
    print("2. Listar IDs de usuarios registrados")
    print("3. Ver información de un usuario por ID")
    print("4. Editar información de un usuario por ID")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Registro de nuevo usuario ---")
        nombre = input("Ingrese el nombre del usuario: ")
        apellidos = input("Ingrese los apellidos del usuario: ")
        telefono = input("Ingrese el número de teléfono del usuario: ")
        correo = input("Ingrese el correo electrónico del usuario: ")

        usuarios[identificador_actual] = {
            "Nombre": nombre,
            "Apellidos": apellidos,
            "Teléfono": telefono,
            "Correo electrónico": correo
        }
        print(f"Usuario registrado con ID: {identificador_actual}")
        identificador_actual += 1

    elif opcion == "2":
        print("\n--- IDs de usuarios registrados ---")
        for usuario_id in usuarios:
            print(f"ID: {usuario_id}")

    elif opcion == "3":
        print("\n--- Información de usuario por ID ---")
        usuario_id = int(input("Ingrese el ID del usuario que desea ver: "))
        if usuario_id in usuarios:
            usuario = usuarios[usuario_id]
            print("Información del usuario:")
            for campo, valor in usuario.items():
                print(f"{campo}: {valor}")
        else:
            print("No se encontró ningún usuario con ese ID.")

    elif opcion == "4":
        print("\n--- Edición de información de usuario por ID ---")
        usuario_id = int(input("Ingrese el ID del usuario que desea editar: "))
        if usuario_id in usuarios:
            print(f"Información actual del usuario con ID {usuario_id}:")
            usuario = usuarios[usuario_id]
            for campo, valor in usuario.items():
                print(f"{campo}: {valor}")
            
            nombre = input("Ingrese el nuevo nombre del usuario: ")
            apellidos = input("Ingrese los nuevos apellidos del usuario: ")
            telefono = input("Ingrese el nuevo número de teléfono del usuario: ")
            correo = input("Ingrese el nuevo correo electrónico del usuario: ")

            usuarios[usuario_id] = {
                "Nombre": nombre,
                "Apellidos": apellidos,
                "Teléfono": telefono,
                "Correo electrónico": correo
            }
            print("Información del usuario actualizada.")
        else:
            print("No se encontró ningún usuario con ese ID.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor seleccione una opción del menú.")
