ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encriptar(mensaje: str, n: int) -> str:
    """Encripta un mensaje usando cifrado César circular (+N) en mayúsculas."""
    desplazamiento = n % len(ALFABETO)
    resultado = []

    for caracter in mensaje.upper():
        if caracter in ALFABETO:
            indice_actual = ALFABETO.index(caracter)
            nuevo_indice = (indice_actual + desplazamiento) % len(ALFABETO)
            resultado.append(ALFABETO[nuevo_indice])
        else:
            resultado.append(caracter)

    return "".join(resultado)


def desencriptar(mensaje: str, n: int) -> str:
    """Desencripta un mensaje desplazando N posiciones hacia atrás."""
    desplazamiento = n % len(ALFABETO)
    resultado = []

    for caracter in mensaje.upper():
        if caracter in ALFABETO:
            indice_actual = ALFABETO.index(caracter)
            nuevo_indice = (indice_actual - desplazamiento) % len(ALFABETO)
            resultado.append(ALFABETO[nuevo_indice])
        else:
            resultado.append(caracter)

    return "".join(resultado)


def solicitar_desplazamiento() -> int | None:
    """Solicita y valida que N sea un número entero mayor o igual a 0."""
    entrada = input("Ingrese el desplazamiento N: ").strip()
    try:
        valor = int(entrada)
        if valor < 0:
            print("Error: el desplazamiento N debe ser un entero mayor o igual a 0.")
            return None
        return valor
    except ValueError:
        print("Error: debe ingresar un número entero válido.")
        return None


def mostrar_menu() -> None:
    """Imprime el menú principal del sistema."""
    print("\nSISTEMA DE CIFRADO CÉSAR MODIFICADO")
    print("=================================")
    print("1. Encriptar mensaje (Opción de Guardar mensaje (S/N))")
    print("2. Desencriptar mensaje")
    print("3. Imprimir mensajes guardados")
    print("4. Salir")
    print("=================================")


def main() -> None:
    mensajes_guardados: list[dict[str, object]] = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mensaje = input("Ingrese el mensaje: ").strip()
            n = solicitar_desplazamiento()
            if n is None:
                continue

            original = mensaje.upper()
            cifrado = encriptar(mensaje, n)

            print(f"Mensaje original: {original}")
            print(f"Mensaje encriptado: {cifrado}")

            guardar = input("¿Desea guardar el mensaje? (S/N): ").strip().upper()
            if guardar == "S":
                mensajes_guardados.append({
                    "original": original,
                    "cifrado": cifrado,
                    "n": n,
                })
                print("Mensaje guardado correctamente.")
            elif guardar != "N":
                print("Respuesta no reconocida; el mensaje no se guardó.")

        elif opcion == "2":
            mensaje_cifrado = input("Ingrese el mensaje encriptado: ").strip()
            n = solicitar_desplazamiento()
            if n is None:
                continue

            mensaje_desencriptado = desencriptar(mensaje_cifrado, n)
            print(f"Mensaje desencriptado: {mensaje_desencriptado}")

        elif opcion == "3":
            if not mensajes_guardados:
                print("No hay mensajes guardados")
            else:
                print("\nMENSAJES GUARDADOS")
                for indice, registro in enumerate(mensajes_guardados, start=1):
                    print(f"{indice}. Original: {registro['original']}")
                    print(f"   Encriptado: {registro['cifrado']}")
                    print(f"   Desplazamiento: {registro['n']}")

        elif opcion == "4":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Error: opción no válida. Seleccione una opción del 1 al 4.")


if __name__ == "__main__":
    main()