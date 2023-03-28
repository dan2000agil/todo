import os
import re

# Definir la carpeta a buscar y la palabra a buscar
carpeta = '/ruta/a/la/carpeta'
palabra = 'buscar'

# Iterar sobre todos los archivos en la carpeta
for nombre_archivo in os.listdir(carpeta):
    ruta_archivo = os.path.join(carpeta, nombre_archivo)
    
    # Comprobar si el objeto en la carpeta es un archivo
    if os.path.isfile(ruta_archivo):
        
        # Abrir el archivo y leer su contenido
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            
            # Buscar la palabra en el contenido
            if re.search(palabra, contenido):
                print(f'La palabra "{palabra}" ha sido encontrada en el archivo {nombre_archivo}')
