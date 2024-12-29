import os
import random
import subprocess

# Ruta al directorio donde están las imágenes
directory = '/home/tu_usuario/Downloads/Telegram'

# Obtener la lista de archivos en el directorio
images = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Verificar que haya imágenes en el directorio
if images:
    # Elegir una imagen aleatoria
    selected_image = random.choice(images)
    
    # Crear la ruta completa a la imagen
    image_path = os.path.join(directory, selected_image)
    
    # Mostrar la imagen en la terminal usando w3m
    subprocess.run(['w3m', image_path])
else:
    print("No hay imágenes en el directorio.")
