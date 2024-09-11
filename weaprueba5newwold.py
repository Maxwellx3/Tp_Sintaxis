from graficador import GraficadorArbol
import parser_1 as analizador

archivo_a_ejecutar = "prueba.txt"  # Reemplaza con la ruta al archivo que deseas analizar
arbol_sintactico = analizador.AnalizadorSintactico(archivo_a_ejecutar)

if arbol_sintactico:
    graficador = GraficadorArbol(arbol_sintactico)  # Crear una instancia de la clase
    graficador.graficar()