import re

class Persona:
    def __init__(self):  # Constructor de la clase
        self.nombre = ""
        self.id = ""

    def capturar_nombre(self):
        """Solicita y almacena el nombre de la persona."""
        while True:
            nombre = input("Ingresa tu nombre (alfabético): ")
            if nombre.isalpha():
                self.nombre = nombre
                break
            else:
                print("Nombre de usuario en formato incorrecto. Debe usar solo letras.")

    def capturar_id(self):
        """Solicita y almacena el ID de la persona."""
        while True:
            id_input = input("Ingresa tu ID (alfanumérico): ")
            if id_input.isalnum():
                self.id = id_input
                break
            else:
                print("ID en formato incorrecto. Debe capturar solo números y letras.")

    def imprimir_nombre(self):
        """Imprime el nombre de la persona."""
        print(f"Nombre: {self.nombre}")

    def imprimir_id(self):
        """Imprime el ID de la persona."""
        print(f"ID: {self.id}")

class Videos:
    def __init__(self):
        self.nombre_video = ""
        self.extension_video = ""
        self.tamanio_video = 0.0

    def capturar_nombre_video(self):
        while True:
            nombre = input("Ingresa el nombre del video (alfanumérico): ")
            if re.match("^[a-zA-Z0-9]+$", nombre):
                self.nombre_video = nombre
                break
            else:
                print("Nombre del vídeo en formato incorrecto. Debe capturar solo números y letras.")

    def capturar_extension_video(self):
        while True:
            extension = input("Ingresa la extensión del video (por ejemplo, .mp4, .mov): ")
            if re.match("^[a-zA-Z0-9.]+$", extension):
                self.extension_video = extension
                break
            else:
                print("Extensión del vídeo en formato incorrecto. Debe capturar solo números y letras.")

    def capturar_tamanio_video(self):
        while True:
            try:
                tamanio = float(input("Ingresa el tamaño del video en MB (0-3): "))
                if 0 <= tamanio <= 3:
                    self.tamanio_video = tamanio
                    break
                else:
                    print("El archivo no debe pesar más de 3 MB.")
            except ValueError:
                print("Tamaño del video en formato incorrecto. Debe capturar solo números.")

    def imprimir_nombre_video(self):
        print(f"Nombre del video: {self.nombre_video}")

    def imprimir_extension_video(self):
        print(f"Extensión del video: {self.extension_video}")

    def imprimir_tamanio_video(self):
        print(f"Tamaño del video: {self.tamanio_video} MB")

if __name__ == "__main__":
    persona = Persona()
    video = Videos()

    persona.capturar_nombre()
    persona.capturar_id()

    video.capturar_nombre_video()
    video.capturar_extension_video()
    video.capturar_tamanio_video()

    with open("salida.txt", "a") as file:
        file.write(f"{persona.id} | {persona.nombre} | {video.nombre_video} | {video.extension_video} | {video.tamanio_video}\n")

    print("Información guardada correctamente en salida.txt")