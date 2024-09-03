# ###############################################################################################
####################################     ANALIZADOR SINTACTICO       #################################
######################################################################################################

import scanner as lex
import arbol as ar
import pila as p
import tablaDeSimbolos as ts 
import pandas as pd

class AnalizadorSintactico():
    ARCHIVO_TAS = r"D:\Facu\Sintaxis\Tp_Sintaxis\CSVTAS.csv"  # Ruta fija del archivoTAS

    def __init__(self, archivoAEjecutar):
        """
        Constructor de la clase AnalizadorSintactico.

        :param archivoAEjecutar: Ruta al archivo a ejecutar.
        """
        self.tablaSimbolos = ts.crearTS()  # Crea la tabla de símbolos
        self.arbol = ar.Nodo('prog')  # Crea el árbol con raíz S
        self.pila = p.Pila()  # Crea una sola pila para apilar lo que contiene un vector de la TAS
        self.pila.push('peso')  # Apilamos el símbolo final
        self.pila.push('prog')  # Apilamos la primera Variable
        self.nodoActual = self.arbol  # El nodo actual es la raíz
        self.archivo = open(archivoAEjecutar)
        self.Lexico = lex.Lexico(self.archivo)  # Creación del analizador léxico

        # Cargar la TAS desde el archivo CSV (ruta fija)
        self.TAS = self.cargarTAS()

    def cargarTAS(self):
        try:
            # Cargar el archivo CSV con la TAS (ruta fija)
            df = pd.read_csv(self.ARCHIVO_TAS, header=None)
            componente_lexico = df.iloc[0, 1:].tolist()
            variable = df.iloc[1:, 0].tolist()
            # Crear un diccionario de reglas de la TAS
            tas_dict = {}
            for var in range(len(variable)):
                for lex in range(1, len(componente_lexico) + 1):
                    regla = df.iloc[var + 1, lex]
                    if pd.notna(regla):
                        regla_componentes = regla.split(',')
                    else:
                        regla_componentes = []
                    tas_dict[(variable[var], componente_lexico[lex - 1])] = regla_componentes
            return tas_dict
        except Exception as e:
            print(f"Error al cargar la TAS desde el archivo: {e}")
            return {}
        finally:
            self.archivo.close()  # Cierra el archivo después de usarlo

    def analizarSintactico(self):
        resultado = 0  # resultado = 0 indica que el analizador Sintáctico debe seguir analizando
        token = self.Lexico.siguienteComponenteLexico()
        while resultado == 0:
            X = self.pila.popp()  # Desapila
            if X == 'peso' == token[0]:
                resultado = 1  # Proceso terminado con éxito
                print("Sintaxis correcta")
            elif X in lex.Terminal:
                if (X == token[0]) or (X == "epsilon"):
                    padre_actual = self.nodoActual.getPadre()
                    if padre_actual and self.nodoActual != padre_actual.hijos[0]:
                        indice_hijo_actual = padre_actual.hijos.index(self.nodoActual)
                        self.nodoActual = padre_actual.hijos[indice_hijo_actual - 1]
                    elif padre_actual and self.nodoActual == padre_actual.hijos[0]:
                        while padre_actual and self.nodoActual == padre_actual.hijos[0]:
                            self.nodoActual = padre_actual
                            padre_actual = self.nodoActual.getPadre()
                        if padre_actual is None:
                            self.nodoActual = None
                        else:
                            # Nos movemos al hermano izquierdo del nodo actual
                            indice_hijo_actual = padre_actual.hijos.index(self.nodoActual)
                            self.nodoActual = padre_actual.hijos[indice_hijo_actual - 1]
                    if X != "epsilon":
                        token = self.Lexico.siguienteComponenteLexico()
                else:
                    print("Error sintáctico")
                    resultado = -1  # Error
            elif X in lex.Variables:
                v = list(reversed(self.TAS[(X, token[0])]))
                if not v:
                    print("Error sintáctico")
                    resultado = -1  # Error
                else:
                    for dato in v:
                        nodo_hijo = ar.Nodo(dato)
                        self.nodoActual.agregarHijo(nodo_hijo)
                    self.nodoActual = self.nodoActual.getHijos()[-1]
                    self.pila.push(v)
            # print("Token: ",token[0])
            # print("X: ",X)
            # print("v: ",v)
            # print("Nodo actual: ",self.nodoActual)
            # # print("Padre del nodo: ",self.nodoActual.getPadre())
            # print("Pila: ",self.pila.lista)
            # print(" ")