 #######################################################################################################
#########################################  TABLA DE SIMBOLOS  #########################################
#######################################################################################################



def crearTS():  #crea la tabla de simbolo que es un diccionario
    if 'ts' not in globals():  # Verifica si la TS ya existe
        # Si no existe, crea la TS
        ts = {
            "leer": 0,
            "escribir": 1,
            "var": 2,
            "mientras": 3,
            "si": 4,
            "sino": 5
        }
        globals()['ts'] = ts  # Guarda la TS en el ámbito global
    return globals()['ts']  # Devuelve la TS


def devolverIdDato(id): #devuelve el valor del correspondiente id en la diccionario si se encuentra
    ts = crearTS()
    if id in ts:
        return ts[id]  # Devuelve el valor asociado al ID
    else:
        return f"El ID '{id}' no se encuentra en la tabla de símbolos."

def agregaraTS(id, valor):
    ts = crearTS()  # Asegúrate de que la tabla de símbolos esté creada
    if id in ts:
        return f"El ID '{id}' ya existe en la tabla de símbolos con el valor {ts[id]}."
    else:
        ts[id] = valor  # Agrega el nuevo ID y su valor a la tabla de símbolos
        return f"El ID '{id}' ha sido agregado con el valor {valor}."

# def agregaraTSenTupla(tupla):
#     ts = crearTS()  # Asegúrate de que la tabla de símbolos esté creada
#     id, valor = tupla
#     if id in ts:
#         return f"El ID '{id}' ya existe en la tabla de símbolos con el valor {ts[id]}."
#     else:
#         ts[id] = valor  # Agrega el nuevo ID y su valor a la tabla de símbolos
#         return f"El ID '{id}' ha sido agregado con el valor {valor}."

def actualizarTS(id, valor):  #modifica el valor del id en la tabla de simbolo, si no se encuentra lo crea
    ts = crearTS()  # Asegúrate de que la tabla de símbolos esté creada
    if id in ts:
        ts[id] = valor  # Actualiza el valor del ID existente
        return f"El ID '{id}' ha sido actualizado con el nuevo valor {valor}."
    else:
        return f"El ID '{id}' no existe en la tabla de símbolos."