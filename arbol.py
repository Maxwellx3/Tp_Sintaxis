######################################################################################################
###########################################      ARBOL      ##########################################
######################################################################################################
class Nodo:

    def __init__(self, dato):   # Nodo() dato por defecto es "", Nodo(dato) dato debe ser str
        self.dato = dato
        self.hijos = []
        self.padre = None

    def agregarHijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

            # Devuelve True si el nodo es una hoja, False si no lo es
    def esHoja(self):
        return not self.hijos

    # Devuuelve True si el nodo es la raiz, False si no lo es
    def esRaiz(self):
        return self.padre is None

            # Metodos Getters
            # --------------------------------------------------------
            # Devuelve su correspondiente Nodo padre.
    def getPadre(self):
        return self.padre

            # Devuelve un array con todos los hijos del nodo
    def getHijos(self):
        return self.hijos

            # Devuelve el dato del nodo en crudo
            # Como siempre usamos strings como dato, devuelve String
    def getDato(self):
        return self.dato

    def __repr__(self):
        return f"{self.dato}"
