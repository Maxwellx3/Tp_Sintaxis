import Parser as p
import scanner as s
import TabladeSimbolos as tsim
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
def evaluarN(arbol, ts, res):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.mas:
        res1 = evaluarA(arbol.hijos[1], ts)
        res2 = evaluarH(arbol.hijos[2], ts, res1)
        res = res + evaluarN(arbol.hijos[3], ts, res2)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.menos:
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res2 = evaluarH(arbol.hijos[2], ts, res1)
        res = res - evaluarN(arbol.hijos[3], ts, res2)
    return res

#<A> ::= <B> <Y>
def evaluarA(arbol, ts):
    res = evaluarB(arbol.hijos[0], ts)
    res = evaluarY(arbol.hijos[1], ts, res)
    return res

#<Y> ::= "*" <B> <Y> | "/" <B> <Y> | ε

#<B> ::= <C> <Z>
def evaluarB(arbol, ts):
    res = evaluarC(arbol.hijos[0], ts)
    res = evaluarZ(arbol.hijos[1], ts, res)
    return res

#<Z> ::= "**" <C> <Z> | "*/" <C> <Z> | ε

#<C> ::= "(" <ExpArit> ")" | "real" | "id"

#<Ciclo> ::= "mientras" <Condición> <Bloque>

#<Condición> ::= <SigCondición> <K>

#<SigCondición> ::= <ExpArit> <J> | "--" <SigCondición>

#<K> ::= "+-" <SigCondición> <K> | "++" <SigCondición> <K> | ε

#<J> ::= "<>" <ExpArit> | "=" <ExpArit> | "<" <ExpArit> | ">" <ExpArit> | "<=" <ExpArit> | ">=" <ExpArit>

#<CondicionalIf> ::= "si" <Condición> <Bloque> <F>

#<F> ::= "sino" <Bloque> | ε

#<Bloque> ::= "[" <Programa> "]"

#<Lectura> ::= "leer" "(" "cadena" "," "id" ")"

#<Escritura> ::= "escribir" "(" "cadena" "," <ExpArit> ")"

archivoAEjecutar = str(input("Ingrese direccion del archivo a ejecutar: \n"))
sint = p.AnalizadorSintactico(archivoAEjecutar) #crea el Analizador Sintactico
arb = sint.analizarSintactico() #Analiza sintacticamente obteniendo un arbol
evaluarS(arb,sint.tablaSimbolos)  #evalua la raiz con el arbol obtenido y la tabla de simbolos del Analizador Sintactico 