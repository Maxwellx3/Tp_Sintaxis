import arbol as ar

# Crear un nodo padre
nodo_padre = ar.Nodo("Padre")

# Supongamos que tienes un array de datos para los hijos
datos_hijos = ["Hijo1", "Hijo2", "Hijo3"]

# Crear nodos hijos y agregarlos al nodo padre
for dato in reversed(datos_hijos):
    nodo_hijo = ar.Nodo(dato)
    nodo_padre.agregarHijo(nodo_hijo)

# Ahora los hijos están agregados al nodo padre
print("Hijos del nodo padre:", [hijo.dato for hijo in nodo_padre.hijos])

# Obtener los hijos del nodo padre
hijos_padre = nodo_padre.getHijos()
hijo_actual = hijos_padre[-1]

indice_ultimo_hijo = nodo_padre.hijos.index(hijo_actual)

# Verificar si el último hijo tiene un hermano anterior
if indice_ultimo_hijo > 0:
    # Obtener el hermano anterior al último hijo
    hermano_anterior_ultimo = nodo_padre.hijos[indice_ultimo_hijo - 1]
    print("El hermano anterior al último hijo es:", hermano_anterior_ultimo.dato)
else:
    print("El último hijo no tiene un hermano anterior.")