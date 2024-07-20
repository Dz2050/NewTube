import re

def get_user_info():
    """Obtiene la información del usuario, la valida y la guarda en un archivo."""

    while True:
        try:
            user_id = input("Ingresa tu ID (alfanumérico): ")
            if not re.match("^[a-zA-Z0-9]+$", user_id):
                raise ValueError("ID en formato incorrecto. Debe capturar solo números y letras.")

            name = input("Ingresa tu nombre (alfabético): ")
            if not name.isalpha():
                raise ValueError("Nombre de usuario en formato incorrecto. Debe usar solo letras.")

            num_videos = int(input("Ingresa la cantidad de videos que subirás (numérico): "))
            if num_videos < 0:
                raise ValueError("Cantidad de vídeos en formato incorrecto. Debe capturar solo números.")

            confirmation = input(f"Bienvenido {name}, tu número de ID es {user_id} y estás intentando subir {num_videos} videos. ¿Es correcta la información? (Sí/No): ")
            if confirmation.lower() in ["si", "sí", "s"]:
                while True:
                    video_title = input("Ingresa el título del video (alfanumérico): ")
                    if not re.match("^[a-zA-Z0-9]+$", video_title):
                        raise ValueError("Título del vídeo en formato incorrecto. Debe capturar solo números y letras.")

                    video_name = input("Ingresa el nombre del archivo del video (alfanumérico): ")
                    if not re.match("^[a-zA-Z0-9]+$", video_name):
                        raise ValueError("Nombre del vídeo en formato incorrecto. Debe capturar solo números y letras.")

                    video_extension = input("Ingresa la extensión del video (por ejemplo, .mp4, .mov, etc.): ")
                    if not re.match("^[a-zA-Z0-9.]+$", video_extension):
                        raise ValueError("Extensión del vídeo en formato incorrecto. Debe capturar solo números y letras.")

                    video_size_mb = float(input("Ingresa el tamaño del video en MB (0-3): "))
                    if 0 <= video_size_mb <= 3:
                        # Guardar información en salida.txt
                        with open("salida.txt", "a") as file:
                            file.write(f"{user_id} | {name} | {num_videos} | {video_title} | {video_name} | {video_extension} | {video_size_mb}\n")
                        
                        print("Información guardada correctamente en salida.txt")
                        return
                    else:
                        print("El archivo no debe pesar más de 3 MB.")
            else:
                exit_confirmation = input("¿Deseas salir del sistema? (Sí/No): ")
                if exit_confirmation.lower() in ["si", "sí", "s"]:
                    print("Muchas gracias por haber usado nuestro sistema, hasta pronto.")
                    return
                else:
                    print("Por favor, ingresa la información nuevamente.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    user_info = get_user_info()
    if user_info:
        user_id, name, num_videos, video_title, video_name, video_extension, video_size_mb = user_info
        print("\nInformación confirmada:")
        print(f"ID: {user_id}")
        print(f"Nombre: {name}")
        print(f"Cantidad de videos: {num_videos}")
        print(f"Título del video: {video_title}")
        print(f"Nombre del archivo: {video_name}")
        print(f"Extensión: {video_extension}")
        print(f"Tamaño: {video_size_mb} MB")