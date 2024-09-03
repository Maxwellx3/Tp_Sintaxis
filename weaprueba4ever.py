import parser_1 as p

archivo_a_ejecutar = "prueba.txt"  # Reemplaza con la ruta al archivo que deseas analizar

# Crear una instancia de AnalizadorSintactico
analizador = p.AnalizadorSintactico(archivo_a_ejecutar)

# Ejecutar el análisis sintáctico
analizador.analizarSintactico()
