import parser_1 as p
import scanner as s

#<prog> ::= <sent> ";" <G>
def evaluarPrograma(arbol):
    evaluarSentencia(arbol.hijos[-1])
    evaluarG(arbol.hijos[0])

#<G> ::= <sent> ";" <G> | ε
def evaluarG(arbol):
    if len(arbol.hijos)>=1:
        evaluarSentencia(arbol.hijos[-1])
        evaluarG(arbol.hijos[0])

#<sent> ::= “var” <variable> | <ciclo> | <condIf> | <lect> | <escr> | <asig>
def evaluarSentencia(arbol):
    if arbol.hijos[-1] == "var":
        evaluarVar(arbol.hijos[1])
    elif arbol.hijos[-1] == "ciclo":
        evaluarCiclo(arbol.hijos[0])
    elif arbol.hijos[0] == "condIf":
        evaluarCondIf(arbol.hijos[0])
    elif arbol.hijos[0] == "lect":
        evaluarLect(arbol.hijos[0])
    elif arbol.hijos[0] == "escr":
        evaluarEscr(arbol.hijos[0])
    elif arbol.hijos[0] == "asig":
        evaluarAsig(arbol.hijos[0])

#<variable> ::= "id" <H>
def evaluarVar(arbol):
    # Agregar el identificador a la tabla de símbolos
    # ts.agregarIdentificador(arbol.hijos[0].dato)
    # Evaluar la parte <H> de la producción
    evaluarH(arbol.hijos[0])

#<H> ::= “,” "id" <H> | ε
def evaluarH(arbol):
    if len(arbol.hijos)>=1:
        # Agregar el identificador a la tabla de símbolos
        # ts.agregarIdentificador(arbol.hijos[1].dato)
        # Evaluar la siguiente parte de <H>
        evaluarH(arbol.hijos[0])

#<asig> ::= “id” ":" <expArit>
def evaluarAsig(arbol):
    id_nombre = arbol.hijos[-1]
    # Evaluar la expresión aritmética (lado derecho de la asignación)
    valor = evaluarExpArit(arbol.hijos[0])
    # Asignar el valor al identificador en la tabla de símbolos
    # ts.asignarValor(id_nombre, valor)

#<expArit> ::= <A> <X>
def evaluarExpArit(arbol):
    # Evaluar la parte <A>
    evaluarA(arbol.hijos[-1])
    # Evaluar la parte <X>
    evaluarX(arbol.hijos[0])
    
#<X> ::= "+" <A> <X> | "-" <A> <X> | ε
def evaluarX(arbol):
    if len(arbol.hijos) == 0:
        # Caso epsilon (ε): no hay operación adicional, devolver 0
        return 0
    # Verificar si hay un operador '+' o '-'
    operador = arbol.hijos[0].dato
    if operador in ["+", "-"]:
        # Evaluar el lado derecho <A>
        valorA = evaluarA(arbol.hijos[1])
        # Evaluar recursivamente <X>
        valorX = evaluarX(arbol.hijos[2])
        if operador == "+":
            return valorA + valorX
        else:
            return valorA - valorX

#<A> ::= <B> <Y> 
def evaluarA(arbol):
    # Evaluar la parte <B>
    valorB = evaluarB(arbol.hijos[0])
    # Evaluar la parte <Y>
    valorY = evaluarY(arbol.hijos[1])
    # Combinar los valores de <B> y <Y>
    return valorB * valorY

#<Y> ::= "*" <B> <Y> | "/" <B> <Y> | ε
def evaluarY(arbol):
    if len(arbol.hijos) == 0:
        # Caso epsilon (ε): no hay operación adicional, devolver 1
        return 1
    # Verificar si hay un operador '*' o '/'
    operador = arbol.hijos[0].dato
    if operador in ["*", "/"]:
        # Evaluar el lado derecho <B>
        valorB = evaluarB(arbol.hijos[1])
        # Evaluar recursivamente <Y>
        valorY = evaluarY(arbol.hijos[2])
        if operador == "*":
            return valorB * valorY
        else:
            if valorB == 0:
                print("Error: División por cero en <Y>.")
                return 1
            return valorY / valorB
    else:
        print("Error: Se esperaba un operador '*' o '/' en <Y>.")
        return 1

#<B> ::= <C> <Z>
def evaluarB(arbol):
    # Evaluar la parte <C>
    valorC = evaluarC(arbol.hijos[0])
    # Evaluar la parte <Z>
    valorZ = evaluarZ(arbol.hijos[1])
    # Combinar los valores de <C> y <Z>
    return valorC ** valorZ

#<Z> ::= "**" <C> <Z> | "*/" <C> <Z> | ε
def evaluarZ(arbol):
    if len(arbol.hijos) == 0:
        # Caso epsilon (ε): no hay operación adicional, devolver 1
        return 1
    # Verificar si hay un operador '**' o '*/'
    operador = arbol.hijos[0].dato
    if operador in ["**", "*/"]:
        # Evaluar el lado derecho <C>
        valorC = evaluarC(arbol.hijos[1])
        # Evaluar recursivamente <Z>
        valorZ = evaluarZ(arbol.hijos[2])
        if operador == "**":
            return valorC ** valorZ
        else:
            # Aquí puedes definir qué significa '*/' en tu contexto
            print("Error: Operador '*/' no definido en <Z>.")
            return 1
    else:
        print("Error: Se esperaba un operador '**' o '*/' en <Z>.")
        return 1

#<C> ::= "(" <expArit> ")" | "real" | "id"
def evaluarC(arbol):
    # Verificar la producción de <C>
    if arbol.hijos[0].dato == "(":
        # Evaluar la expresión aritmética entre paréntesis
        return evaluarExpArit(arbol.hijos[1])
    elif arbol.hijos[0].dato == "real":
        # Retornar el valor numérico real
        return float(arbol.hijos[0])
    elif arbol.hijos[0].dato == "id":
        # Obtener el valor del identificador desde la tabla de símbolos
        return ts.obtenerValor(arbol.hijos[0].dato)
    else:
        print("Error: Se esperaba '(', 'real' o 'id' en <C>.")
        return 0

#<Ciclo> ::= "mientras" <Condición> <Bloque>

#<Condición> ::= <SigCondición> <K>

#<SigCondición> ::= <ExpArit> "opRel" <ExpArit> | "--" <SigCondición> | “{“ <Condicion> ”}”

#<K> ::= "+-" <SigCondición> <K> | "++" <SigCondición> <K> | ε

#<J> ::= "<>" <ExpArit> | "=" <ExpArit> | "<" <ExpArit> | ">" <ExpArit> | "<=" <ExpArit> | ">=" <ExpArit>

#<CondicionalIf> ::= "si" <Condición> <Bloque> <F>

#<F> ::= "sino" <Bloque> | ε

#<Bloque> ::= "[" <Programa> "]"

#<Lectura> ::= "leer" "(" "cadena" "," "id" ")"
def evaluarLect(arbol):
    if len(arbol.hijos[2].hijos) == 1:
        print(arbol.hijos[2].hijos[0])
    aux = input()
    tsim.actualizarTS(ts,arbol.hijos[4].hijos[0], aux)

#<Escritura> ::= "escribir" "(" "cadena" "," <ExpArit> ")"
def evaluarEscr(arbol):
    if len(arbol.hijos[2].hijos) == 1:
        print(arbol.hijos[2].hijos[0])
    res = evaluarExprArit(arbol.hijos[4])
    print(res)

archivoAEjecutar = "prueba.txt"
sint = p.AnalizadorSintactico(archivoAEjecutar) #crea el Analizador Sintactico
arb = sint.analizarSintactico() #Analiza sintacticamente obteniendo un arbol
if arb is not None:
    evaluarPrograma(arb)  # Evalúa la raíz con el árbol obtenido
else:
    print("No se puede ejecutar el programa debido a errores de sintaxis.")