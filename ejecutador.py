import parser_1 as p
import tablaDeSimbolos as tsim

#<prog> ::= <sent> ";" <G>
def evaluarPrograma(arbol):
    evaluarSentencia(arbol.hijos[-1])
    evaluarG(arbol.hijos[0])

#<G> ::= <sent> ";" <G> | ε
def evaluarG(arbol):
    if (len(arbol.hijos)>=1) and (arbol.hijos[0].dato != "epsilon"):
        evaluarSentencia(arbol.hijos[-1])
        evaluarG(arbol.hijos[0])

#<sent> ::= “var” <variable> | <ciclo> | <condIf> | <lect> | <escr> | <asig>
def evaluarSentencia(arbol):
    if len(arbol.hijos) > 0:
        if arbol.hijos[-1].dato == "var":
            evaluarVar(arbol.hijos[0])
        elif arbol.hijos[0].dato == "ciclo":
            evaluarCiclo(arbol.hijos[0])
        elif arbol.hijos[0].dato == "condIf":
            evaluarCondIf(arbol.hijos[0])
        elif arbol.hijos[0].dato == "lect":
            evaluarLect(arbol.hijos[0])
        elif arbol.hijos[0].dato == "escr":
            evaluarEscr(arbol.hijos[0])
        elif arbol.hijos[0].dato == "asig":
            evaluarAsig(arbol.hijos[0])

#<variable> ::= "id" <H>
def evaluarVar(arbol):
    # Agregar el identificador a la ts
    tsim.agregaraTS(arbol.hijos[-1].dato[1],arbol.hijos[-1].dato[1])
    evaluarH(arbol.hijos[0])

#<H> ::= “,” "id" <H> | ε
def evaluarH(arbol):
    if (len(arbol.hijos)>=1) and (arbol.hijos[0].dato != "epsilon"):
        # Agregar el identificador a la ts
        tsim.agregaraTS(arbol.hijos[1].dato[1],arbol.hijos[1].dato[1])
        evaluarH(arbol.hijos[0])

#<asig> ::= “id” ":" <expArit>
def evaluarAsig(arbol):
    id_nombre = arbol.hijos[-1].dato[1]
    # Evaluar la expresión aritmética
    valor = evaluarExpArit(arbol.hijos[0])
    # Actualiza el valor al identificador en la ts
    tsim.actualizarTS(id_nombre,valor)

#<expArit> ::= <A> <X>
def evaluarExpArit(arbol):
    valorA = evaluarA(arbol.hijos[-1])
    valorX = evaluarX(arbol.hijos[0],valorA)
    return valorX
    
#<X> ::= "+" <A> <X> | "-" <A> <X> | ε
def evaluarX(arbol,res):
    if arbol.hijos[0].dato == "epsilon":
        # Caso ε
        return res
    operador = arbol.hijos[-1].dato
    if operador in ["mas", "menos"]:
        valorA = evaluarA(arbol.hijos[1])
        if operador == "mas":
            res1 = res + valorA
        else:
            res1 = res - valorA
        valorX = evaluarX(arbol.hijos[0],res1)
        return valorX

#<A> ::= <B> <Y> 
def evaluarA(arbol):
    valorB = evaluarB(arbol.hijos[-1])
    valorY = evaluarY(arbol.hijos[0],valorB)
    return valorY

#<Y> ::= "*" <B> <Y> | "/" <B> <Y> | ε
def evaluarY(arbol,res):
    if arbol.hijos[0].dato == "epsilon":
        # Caso ε
        return res
    operador = arbol.hijos[-1].dato
    if operador in ["por", "dividido"]:
        valorB = evaluarB(arbol.hijos[1])
        if operador == "por":
            res1 = res * valorB
        else:
            if valorB == 0:
                print("Error: División por cero en <Y>.")
            else:
                res1 = res / valorB
        valorY = evaluarY(arbol.hijos[0], res1)
        return valorY

#<B> ::= <C> <Z>
def evaluarB(arbol):
    valorC = evaluarC(arbol.hijos[-1])
    valorZ = evaluarZ(arbol.hijos[0],valorC)
    return valorZ

#<Z> ::= "**" <C> <Z> | "*/" <C> <Z> | ε
def evaluarZ(arbol,res):
    if arbol.hijos[0].dato == "epsilon":
        # Caso ε
        return res
    operador = arbol.hijos[-1].dato
    if operador in ["potencia", "raiz"]:
        valorC = evaluarC(arbol.hijos[1])
        if operador == "potencia":
            res1 = res ** valorC
        else:
            res1 = valorC ** (1/res)
        valorZ = evaluarZ(arbol.hijos[0],res1)
        return valorZ

#<C> ::= "(" <expArit> ")" | "real" | "id"
def evaluarC(arbol):
    if arbol.hijos[-1].dato == "parentesisAbre":
        return evaluarExpArit(arbol.hijos[1])
    elif arbol.hijos[0].dato[0] == "real":
        # Retornar el valor numérico real
        return float(arbol.hijos[0].dato[1])
    elif arbol.hijos[0].dato[0] == "id":
        # Obtiene el valor del identificador desde la ts
        return tsim.devolverIdDato(arbol.hijos[0].dato[1])

#<ciclo> ::= "mientras" <cond> <bloque>
def evaluarCiclo(arbol):
    while evaluarCond(arbol.hijos[1]):
        evaluarBloque(arbol.hijos[0])

#<cond> ::= <SigCond> <K>
def evaluarCond(arbol):
    valor_cond = evaluarSigCond(arbol.hijos[-1])
    return evaluarK(arbol.hijos[0], valor_cond)

#<K> ::= "+-" <SigCond> <K> | "++" <SigCond> <K> | ε
def evaluarK(arbol, valor_inicial):
    if arbol.hijos[0].dato != "epsilon":
        sig_cond_val = evaluarSigCond(arbol.hijos[1])
        if arbol.hijos[-1].dato == "opAnd": 
            valor_inicial = valor_inicial and sig_cond_val
        elif arbol.hijos[-1] == "opOr":  
            valor_inicial = valor_inicial or sig_cond_val
        return evaluarK(arbol.hijos[0], valor_inicial)
    return valor_inicial  # Caso ε

#<SigCond> ::= <expArit> "opRel" <expArit> | "--" <SigCond> | “{“ <cond> ”}”
def evaluarSigCond(arbol):
    if arbol.hijos[-1].dato == "opNeg":
        return not evaluarSigCond(arbol.hijos[0])
    elif arbol.hijos[-1] == "llaveAbre": 
        return evaluarCond(arbol.hijos[1])
    else:
        exp1 = evaluarExpArit(arbol.hijos[-1])
        op_rel = arbol.hijos[1].dato[1]
        exp2 = evaluarExpArit(arbol.hijos[0])
        return evaluarOpRel(exp1, op_rel, exp2)

#<condIf> ::= "si" <cond> <bloque> <F>
def evaluarCondIf(arbol):
    if evaluarCond(arbol.hijos[2]):
        evaluarBloque(arbol.hijos[1])
    else:
        evaluarF(arbol.hijos[0])

#<F> ::= "sino" <bloque> | ε
def evaluarF(arbol):
    if arbol.hijos[0].dato != "epsilon": 
        evaluarBloque(arbol.hijos[0])

#<bloque> ::= "[" <prog> "]"
def evaluarBloque(arbol):
    evaluarPrograma(arbol.hijos[1])  # Se evalúa el programa dentro del bloque

#<Lectura> ::= "leer" "(" "cadena" "," "id" ")"
def evaluarLect(arbol):
    print(arbol.hijos[3].dato[1])
    aux = float(input())
    tsim.actualizarTS(arbol.hijos[1].dato[1], aux)

#<Escritura> ::= "escribir" "(" "cadena" "," <ExpArit> ")"
def evaluarEscr(arbol):
    res = evaluarExpArit(arbol.hijos[1])
    print(arbol.hijos[3].dato[1],res)

def evaluarOpRel(exp1, op_rel, exp2):
    if op_rel == "=":
        return exp1 == exp2
    elif op_rel == "<>":
        return exp1 != exp2
    elif op_rel == "<":
        return exp1 < exp2
    elif op_rel == ">":
        return exp1 > exp2
    elif op_rel == "<=":
        return exp1 <= exp2
    elif op_rel == ">=":
        return exp1 >= exp2

archivoAEjecutar = "prueba.txt"
sint = p.AnalizadorSintactico(archivoAEjecutar) #crea el Analizador Sintactico
arb = sint.analizarSintactico() #Analiza sintacticamente obteniendo un arbol
if arb is not None:
    evaluarPrograma(arb)  # Evalúa la raíz con el árbol obtenido
    # print(arb.hijos[-1].hijos[0].hijos[0].hijos[0].hijos[0].hijos[0].dato)
else:
    print("No se puede ejecutar el programa debido a errores de sintaxis.")