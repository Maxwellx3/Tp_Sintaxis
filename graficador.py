from graphviz import Digraph
import arbol

class GraficadorArbol:
    def __init__(self, arbol_sintactico):
        self.arbol = arbol_sintactico
        self.dot = Digraph(comment='Árbol Sintáctico')

    def graficar(self):
        # Comienza la graficación desde la raíz del árbol sintáctico
        self._agregar_nodos_aristas(self.arbol)
        self.dot.render('arbol_sintactico', format='png', cleanup=True)

    def _agregar_nodos_aristas(self, nodo, nodo_id='0'):
        # Verifica que el nodo sea una instancia de la clase correcta
        if isinstance(nodo.getRaiz(), arbol.Nodo):
            self.dot.node(nodo_id, repr(nodo))  # Usa repr(nodo) para obtener la cadena representativa del nodo
            for i, hijo in enumerate(nodo.getHijos()):
                hijo_id = f"{nodo_id}_{i}"
                self.dot.edge(nodo_id, hijo_id)
                self._agregar_nodos_aristas(hijo, hijo_id)
        else:
            print(f"Error: Nodo {nodo_id} no es una instancia válida de la clase Nodo")