import Parser as p
import scanner as s
import TabladeSimbolos as tsim
#Semantica

#< S >::= < sentencia > < A >
def evaluarS(arbol, ts):
    evaluarSentencia(arbol.hijos[0], ts)
    evaluarA(arbol.hijos[1], ts)

#< A >::= 	 ; < sentencia> <A> | ε
def evaluarA(arbol ,ts):
    if len(arbol.hijos)>=1 and  arbol.hijos[0].getDato()==s.puntoycoma:
        evaluarSentencia(arbol.hijos[1] ,ts)
        evaluarA(arbol.hijos[2] ,ts)

#<sentencia> ::=        leer(cadena, id) | escribir(texto, < expr_arit_c > < H > < N > ) | id = < expr_arit_c > < H > < N >
def evaluarSentencia(arbol, ts):
    if len(arbol.hijos)>=1 and  arbol.hijos[0].getDato()== s.LEER:
        if len(arbol.hijos[2].hijos) == 1:
            print(arbol.hijos[2].hijos[0].getDato())
        aux = input()
        tsim.actualizarTS(ts,arbol.hijos[4].hijos[0].getDato(), aux)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.ESCRIBIR:
        if len(arbol.hijos[2].hijos) == 1:
            print(arbol.hijos[2].hijos[0].getDato())
        res = evaluarExprArit(arbol.hijos[4], ts)
        res = evaluarH(arbol.hijos[5], ts, res)
        res = evaluarN(arbol.hijos[6], ts, res)
        print(res)
    else:
        res = evaluarExprArit(arbol.hijos[2], ts)
        res = evaluarH(arbol.hijos[3], ts, res)
        res = evaluarN(arbol.hijos[4], ts, res)
        tsim.actualizarTS(ts,arbol.hijos[0].hijos[0].getDato(), str(res))

#< N >::=        + < expr_arit_c > < H > < N > | - < expr_arit_c > < H > < N > | ε

def evaluarN(arbol, ts, res):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.mas:
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res2 = evaluarH(arbol.hijos[2], ts, res1)
        res = res + evaluarN(arbol.hijos[3], ts, res2)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.menos:
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res2 = evaluarH(arbol.hijos[2], ts, res1)
        res = res - evaluarN(arbol.hijos[3], ts, res2)
    return res

#< H >::= * < expr_arit_c > < H > | / < expr_ar1it_c > < H > | ε
def evaluarH(arbol, ts, res: int):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.por:
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res = res * evaluarH(arbol.hijos[2], ts, res1)
    elif len(arbol.hijos)>=1  and arbol.hijos[0].getDato() == s.dividido:
        res2 = evaluarExprArit(arbol.hijos[1], ts)
        res = res /evaluarH(arbol.hijos[2], ts, res2)
    return res

#< expr_arit_c >::=    id | const | ( < expr_arit_c > < H > < N >)
def evaluarExprArit(arbol, ts):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.id:
        return float(tsim.devolverIdDato(ts, arbol.hijos[0].hijos[0].getDato()))
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.real:
        return float(arbol.hijos[0].hijos[0].getDato())
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.parentesisAbre:
        res = evaluarExprArit(arbol.hijos[1], ts)
        res = evaluarH(arbol.hijos[2], ts, res)
        res = evaluarN(arbol.hijos[3], ts, res)
        return res


archivoAEjecutar = str(input("Ingrese direccion del archivo a ejecutar: \n"))
sint = p.AnalizadorSintactico(archivoAEjecutar) #crea el Analizador Sintactico
arb = sint.analizarSintactico() #Analiza sintacticamente obteniendo un arbol
evaluarS(arb,sint.tablaSimbolos)  #evalua la raiz con el arbol obtenido y la tabla de simbolos del Analizador Sintactico