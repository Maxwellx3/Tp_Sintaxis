import scanner
import tablaDeSimbolos as tsim

    # Abrir el archivo
with open("prueba.txt", "r") as archivo:
        # Instanciar el analizador léxico con el objeto de archivo
        lexico = scanner.Lexico(archivo)
        token = lexico.siguienteComponenteLexico()  # Obtenemos el siguiente token
        while (token[0] != "peso") and (token[0] != "ErrorLexico"):
            print(token)  # Imprimimos el token obtenido
            token = lexico.siguienteComponenteLexico()  # Obtenemos el siguiente tokencle
        print(token)