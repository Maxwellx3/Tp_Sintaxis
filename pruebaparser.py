# Importamos el módulo del analizador sintáctico
import parser_1

# Ruta al archivo de entrada que contiene el código fuente a analizar
archivo_entrada = "C:\\Users\\mache\\OneDrive\\Documentos\\sintaxisTAS\\TAS.csv"

# Creamos una instancia del analizador sintáctico con el archivo de entrada
analizador = parser_1.AnalizadorSintactico(archivo_entrada)

# Ejecutamos el análisis sintáctico
analizador.analizarSintactico()

# El análisis habrá finalizado en este punto. Podemos imprimir el árbol resultante
print("Árbol de Análisis Sintáctico:")
print(analizador.arbol)

# Podemos realizar otras operaciones o inspecciones según sea necesario
# Por ejemplo, imprimir la tabla de símbolos
print("Tabla de Símbolos:")
print(analizador.tablaSimbolos)


