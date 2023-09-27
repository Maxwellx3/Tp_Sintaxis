import parser_1 as p
import scanner as s
import tablaDeSimbolos as tsim
#Semantica

#<Programa> ::= <Sentencia> <G>
def evaluarPrograma(arbol, ts):
    evaluarSentencia(arbol.hijos[0], ts)
    evaluarG(arbol.hijos[1], ts)

#<G> ::= ";" <Sentencia> <G> | ε
def evaluarG(arbol, ts):
    if len(arbol.hijos)>=1 and  arbol.hijos[0].getDato()==s.puntoycoma:
        evaluarSentencia(arbol.hijos[1], ts)
        evaluarG(arbol.hijos[2], ts)

#<Sentencia> ::= <Var> | <Ciclo> | <CondicionalIf> | <Lectura> | <Escritura>
def evaluarSentencia(arbol, ts):
    if len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.var:
        evaluarVar(arbol.hijos[0],ts)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.ciclo:
        evaluarCiclo(arbol.hijos[0],ts)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.condIf:
        evaluarCondIf(arbol.hijos[0],ts)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.lect:
        evaluarLect(arbol.hijos[0],ts)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.escr:
        evaluarEscr(arbol.hijos[0],ts)

#<Var> ::= "id" <Asignación>
def evaluarVar(arbol, ts):
    res = evaluarAsig(arbol.hijos[1], ts)
    tsim.actualizarTS(ts,arbol.hijos[0].hijos[0].getDato(), str(res))

#<Asignación> ::= ":" <ExpArit> | "," "id" <Asignación>
def evaluarAsig(arbol, ts):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.asignar:
        res = evaluarExprArit(arbol.hijos[1], ts)
        return res
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.coma:
        res = evaluarAsig(arbol.hijos[2], ts)
        tsim.actualizarTS(ts,arbol.hijos[1].hijos[0].getDato(), str(res))

#<ExpArit> ::= <A> <X>
def evaluarExprArit(arbol, ts):
    res = evaluarA(arbol.hijos[0], ts)
    res = evaluarX(arbol.hijos[1], ts, res)
    return res

#<X> ::= "+" <A> <X> | "-" <A> <X> | ε *falta
def evaluarX(arbol, ts, res):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.mas:
        res1 = evaluarA(arbol.hijos[1], ts)
        res = res + evaluarX(arbol.hijos[2], ts, res1)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.menos:
        res1 = evaluarA(arbol.hijos[1], ts)
        res = res - evaluarX(arbol.hijos[2], ts, res1)
    return res

#<A> ::= <B> <Y>
def evaluarA(arbol, ts):
    res = evaluarB(arbol.hijos[0], ts)
    res = evaluarY(arbol.hijos[1], ts, res)
    return res

#<Y> ::= "*" <B> <Y> | "/" <B> <Y> | ε
def evaluarY(arbol, ts, res):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.por:
        res1 = evaluarB(arbol.hijos[1], ts)
        res = res * evaluarY(arbol.hijos[2], ts, res1)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.dividido:
        res1 = evaluarB(arbol.hijos[1], ts)
        res = res / evaluarY(arbol.hijos[2], ts, res1)
    return res

#<B> ::= <C> <Z>
def evaluarB(arbol, ts):
    res = evaluarC(arbol.hijos[0], ts)
    res = evaluarZ(arbol.hijos[1], ts, res)
    return res

#<Z> ::= "**" <C> <Z> | "*/" <C> <Z> | ε
def evaluarZ(arbol, ts, res):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.potencia:
        res1 = evaluarC(arbol.hijos[1], ts)
        res = res ** evaluarZ(arbol.hijos[2], ts, res1)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.raiz:
        res1 = evaluarC(arbol.hijos[1], ts)
        res =  math.sqrt(evaluarZ(arbol.hijos[2], ts, res1))
    return res

#<C> ::= "(" <ExpArit> ")" | "real" | "id"
def evaluarC(arbol, ts):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.id:
        return float(tsim.devolverIdDato(ts, arbol.hijos[0].hijos[0].getDato()))
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.real:
        return float(arbol.hijos[0].hijos[0].getDato())
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.parentesisAbre:
        res = evaluarExprArit(arbol.hijos[1], ts)
        return res

#<Ciclo> ::= "mientras" <Condición> <Bloque>

#<Condición> ::= <SigCondición> <K>

#<SigCondición> ::= <ExpArit> <J> | "--" <SigCondición>

#<K> ::= "+-" <SigCondición> <K> | "++" <SigCondición> <K> | ε

#<J> ::= "<>" <ExpArit> | "=" <ExpArit> | "<" <ExpArit> | ">" <ExpArit> | "<=" <ExpArit> | ">=" <ExpArit>

#<CondicionalIf> ::= "si" <Condición> <Bloque> <F>

#<F> ::= "sino" <Bloque> | ε

#<Bloque> ::= "[" <Programa> "]"

#<Lectura> ::= "leer" "(" "cadena" "," "id" ")"
def evaluarLect(arbol, ts):
    if len(arbol.hijos[2].hijos) == 1:
        print(arbol.hijos[2].hijos[0].getDato())
    aux = input()
    tsim.actualizarTS(ts,arbol.hijos[4].hijos[0].getDato(), aux)

#<Escritura> ::= "escribir" "(" "cadena" "," <ExpArit> ")"
def evaluarEscr(arbol, ts):
    if len(arbol.hijos[2].hijos) == 1:
        print(arbol.hijos[2].hijos[0].getDato())
    res = evaluarExprArit(arbol.hijos[4], ts)
    print(res)

archivoAEjecutar = str(input("Ingrese direccion del archivo a ejecutar: \n"))
sint = p.AnalizadorSintactico(archivoAEjecutar) #crea el Analizador Sintactico
arb = sint.analizarSintactico() #Analiza sintacticamente obteniendo un arbol
evaluarPrograma(arb,sint.tablaSimbolos)  #evalua la raiz con el arbol obtenido y la tabla de simbolos del Analizador Sintactico 