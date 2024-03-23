import os

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()

# Verificar si los archivos están en el directorio actual
archivos_presentes = all(
    [
        os.path.isfile(os.path.join(directorio_actual, archivo))
        for archivo in ["weaprueba.py", "scanner.py", "archivo.py", "tablaDeSimbolos.py"]
    ]
)

if archivos_presentes:
    print("Los archivos están en el mismo directorio.")
else:
    print("Algunos archivos no están en el mismo directorio.")
