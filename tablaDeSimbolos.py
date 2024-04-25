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


def devolverIdDato(ts, id: str): #devuelve el valor del correspondiente id en la diccionario si se encuentra
    if ts.get(id)!= None:
        return ts[id]

def actualizarTS(ts, id: str, res: str):  #modifica el valor del id en la tabla de simbolo, si no se encuentra lo crea
    ts[id] = res
    return ts