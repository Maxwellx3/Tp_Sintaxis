import scanner

# def main():
    # Abrir el archivo
with open("prueba.txt", "r") as archivo:
        # Instanciar el analizador léxico con el objeto de archivo
        lexico = scanner.Lexico(archivo)
        token = lexico.siguienteComponenteLexico({})  # Obtenemos el siguiente token
        while token[0] != "peso" :
            print(token)  # Imprimimos el token obtenido
            token = lexico.siguienteComponenteLexico({})  # Obtenemos el siguiente token


