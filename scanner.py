import archivo as arc
import tablaDeSimbolos as tsim
import string

######################################################################################################
#################################     TIPOS COMPONENTES LEXICOS     ##################################
######################################################################################################

igual = "igual"
mayor = "mayor"
menor = "menor"
mayorIgual = "mayorIgual"
menorIgual = "menorIgual"
distinto = "distinto"
asignar = "asignar"
opAnd = "opAnd"
opNeg = "opNeg"
opOr = "opOr"
mas = "mas"
menos = "menos"
por = "por"
dividido = "dividido"
potencia = "potencia"
raiz = "raiz"
puntoycoma= "puntoycoma"
coma = "coma"
punto = "punto"
parentesisAbre = "parentesisAbre"
parentesisCierra = "parentesisCierra"
corcheteAbre = "corcheteAbre"
corcheteCierra = "corcheteCierra"
cadena = "cadena"
LEER = "leer"
ESCRIBIR = "escribir"
MIENTRAS = "mientras"
SI = "si"
SINO = "sino"
real = "real"
id = "id"
ErrorLexico = "ErrorLexico"
G = "G"
J = "J"
F = "F"
K = "K"
X = "X"
Y = "Y"
Z = "Z"
A = "A"
B = "B"
C = "C"
prog = "PROGRAMA"
sent = "SENTENCIA"
varia = "VAR"
asig = "ASIGNACION"
expArit = "EXPARIT"
ciclo = "CICLO"
cond = "CONDICION"
sigCond = "SIGCONDICION"
condIf = "CONDICIONALIF"
bloque = "BLOQUE"
lect = "LECTURA"
escr = "ESCRITURA"
epsilon = "epsilon"
peso = "peso"

Terminal = [ESCRIBIR, LEER, MIENTRAS, SI, SINO, parentesisAbre, parentesisCierra, corcheteAbre, corcheteCierra, mas, menos, por, dividido, potencia, raiz, cadena, coma, puntoycoma, id, punto, real, igual, mayor, menor, mayorIgual, menorIgual, distinto, opAnd, opNeg, opOr, asignar, ErrorLexico, epsilon, peso]
Variables = [G, F, K, A, B, C, X, Y, Z, prog, sent, varia, asig, expArit, ciclo, cond, sigCond, condIf, bloque, lect, escr]

def simbolo(linea: str, posicion: int) -> bool:
    simb = False
    aux = arc.leerCaracter(linea, posicion)
    if aux in {'=', '<', '>', ':', '+', '-', '*', '/', ';', ',', '.', '(', ')', '[', ']'}:
        simb = True
    return simb

def simbolo1(linea: str, posicion: int) -> bool:
    simb = False
    aux = arc.leerCaracter(linea, posicion)
    if aux in {'=', '+', '*', '/', ';', ',', '(', ')', '[', ']'}:
        simb = True
    return simb

def simboloID(aux: str) -> int:
    if aux in string.ascii_letters:
        return 0
    elif aux in string.digits:
        return 1
    elif aux == "_":
        return 2
    else:
        return 3

def simbCONS(Car: str) -> int:
    if Car in string.digits:
        return 0
    elif Car == '-':
        return 1
    elif Car == '.':
        return 2
    else:
        return 3

def simbCAD(car: str) -> int:
    if car == "'":
        return 0
    else:
        return 1

def esCADENA(linea: str, pos: int) -> str:
    q0 = 0
    F = [2]
    delta = [None] * 4
    for i in range(4):
        delta[i] = [None] * 2
    delta[0][0] = 1
    delta[0][1] = 3
    delta[1][0] = 2
    delta[1][1] = 1
    delta[2][0] = 3
    delta[2][1] = 3
    delta[3][0] = 3
    delta[3][1] = 3
    auxControl = pos
    estado = q0
    lexema = ''
    T = arc.leerCaracter(linea, auxControl)
    while estado != 3  and auxControl < len(linea)  and T!="\n" and (estado not in F):
        estado = delta[estado][simbCAD(T)]
        if estado != 3:
            lexema = lexema + T
            auxControl = auxControl + 1
            T = arc.leerCaracter(linea, auxControl)
    if estado in F:
        pos = auxControl
        return lexema
    else:
        return ""

def esSimbolo(linea: str, posicion: int) -> str:
    aux = linea[posicion]
    if aux == '=':
        return igual
    elif aux == '<':
        if posicion + 1 < len(linea) and linea[posicion + 1] == '=':
            return menorIgual   
        elif posicion + 1 < len(linea) and linea[posicion + 1] == '>':
            return distinto     
        return menor
    elif aux == '>':
        if posicion + 1 < len(linea) and linea[posicion + 1] == '=':
            return mayorIgual
        return mayor
    elif aux == '+':
        if posicion + 1 < len(linea) and linea[posicion + 1] == '-':
            return opOr
        elif posicion + 1 < len(linea) and linea[posicion + 1] == '+':
            return opAnd
        return mas
    elif aux == ':':
        return asignar
    elif aux == '-':
        if posicion + 1 < len(linea) and linea[posicion + 1] == '-':
            return opNeg
        return menos
    elif aux == '*': 
        if posicion  + 1 < len(linea) and linea[posicion + 1] == '*':
            return potencia       
        elif posicion + 1 < len(linea) and linea[posicion + 1] == '/':
            return raiz
        return por
    elif aux == '/':
        return dividido
    elif aux == ";":
        return puntoycoma
    elif aux == ",":
        return coma
    elif aux == '.':
        return punto
    elif aux == "(":
        return parentesisAbre
    elif aux == ")":
        return parentesisCierra
    elif aux == "[":
        return corcheteAbre
    elif aux == "]":
        return corcheteCierra
    else:
        return ""

class Lexico():
    def __init__(self, archivo):   #se ejecuta solo al crear el Lexico (constructor)
        self.posNueva = 0 #guarda la posicion actual en la linea
        self.lineas = arc.leerLineas(archivo) #lee todas las lineas poniendo cada linea en un vector
        self.l = 0 #guarda la linea actual
        self.compLexico = None

    def siguienteComponenteLexico(self, ts): 
        compLexico = ErrorLexico
        lexema = ""
        linea = self.lineas[self.l]
        
        # Avanzar hasta el próximo componente léxico válido
        while self.l < len(self.lineas) and self.posNueva < len(self.lineas[self.l]) and self.lineas[self.l][self.posNueva] == " "  and self.lineas[self.l][self.posNueva] != "\n": #mientras sea espacio o salto de pagina avanza uno, sin salirse del rang
            self.posNueva += 1
       
        
        # Avanzar a la siguiente línea si es necesario (tienen que estar anidados)
        while self.l < (len(self.lineas) - 1) and linea[self.posNueva] == "\n": #avanza de linea cuando el control se encuentra un ";" para que salte al encontrar ;
            self.l += 1
            linea = self.lineas[self.l]
            self.posNueva = 0

        # Si estamos al final del archivo, devolver el token de peso
        if not (self.l < (len(self.lineas) - 1)) and not(self.posNueva < len(self.lineas[self.l])):
            vector = [peso, "$"]
            return vector

        # Intentar reconocer un número real
        lexema = self.esConstReal(linea, self.posNueva)
        if lexema != "":
            self.posNueva += len(lexema) 
            compLexico = real
        else:
            # Intentar reconocer un símbolo
            if simbolo(linea, self.posNueva):
                compLexico = esSimbolo(linea, self.posNueva)
                if compLexico in {menorIgual, mayorIgual, potencia, raiz}:  
                    self.posNueva += 2  
                    if compLexico == menorIgual:
                        lexema = "<="
                    elif compLexico == mayorIgual:
                        lexema = ">="
                    elif compLexico == distinto:
                        lexema = "<>"
                    elif compLexico == potencia:
                        lexema = "**"
                    elif compLexico == raiz:
                        lexema = "*/"
                    elif compLexico == opAnd:
                        lexema = "++"
                    elif compLexico == opNeg:
                        lexema = "--"
                    elif compLexico == opOr:
                        lexema = "+-"
                else:
                    lexema = linea[self.posNueva]
                    self.posNueva += 1
            else:
                # Intentar reconocer un identificador
                lexema = self.esID(linea, self.posNueva)
                if lexema != "":
                    ts = tsim.actualizarTS(ts, lexema, "0")
                    self.posNueva += len(lexema)
                    compLexico = id 
                else:
                    # Intentar reconocer una cadena
                    lexema = esCADENA(linea, self.posNueva)
                    if lexema != "":
                        self.posNueva += len(lexema)
                        compLexico = cadena
                        
                    if compLexico == ErrorLexico:
                        print("En la linea:", self.l, " Posición:", self.posNueva, "se encuentra un error lexico.")
        vector = [compLexico, lexema]
        return vector
    def esConstReal(self, linea: str, pos: int) -> str:
        q0 = 0
        F = {1, 4}
        # Q=range(1,6)
        # sigma=(D, menos, punto, O)
        delta = [None] * 6
        for i in range(6):
            delta[i] = [None] * 4
        estado = q0
        auxControl = pos
        delta[0][0] = 1
        delta[0][1] = 3
        delta[0][2] = 5  # 5=muerto
        delta[0][3] = 5
        delta[1][0] = 1
        delta[1][1] = 5
        delta[1][2] = 2
        delta[1][3] = 5
        delta[2][0] = 4
        delta[2][1] = 5
        delta[2][2] = 5
        delta[2][3] = 5
        delta[3][0] = 1
        delta[3][1] = 5
        delta[3][2] = 5
        delta[3][3] = 5
        delta[4][0] = 4
        delta[4][1] = 5
        delta[4][2] = 5
        delta[4][3] = 5
        delta[5][0] = 5
        delta[5][1] = 5
        delta[5][2] = 5
        delta[5][3] = 5
        lexema = ""
        T = arc.leerCaracter(linea, auxControl)
        while estado != 5 and auxControl < len(linea) and T != " " and T != "\n" and (not simbolo1(linea, auxControl)):
            estado = delta[estado][simbCONS(T)]
            if estado != 5:
                lexema = lexema + T
                auxControl = auxControl + 1
                T = arc.leerCaracter(linea, auxControl)
        if estado in F:
            return lexema
        else:
            return ""
    def esID (self, linea: str, posicion: int)-> str:
        q0 = 0
        F = {0, 1}
        # Q = (0,1,2)
        # sigma=[(letra, digito, guionBajo, otro)]   #letra = 0ra columna, digito = 1da columna, guionBajo = 2ra columna, otro= 3ta columna)
        delta = [None] * 3
        for i in range(3):
            delta[i] = [None] * 4
        delta[0][0] = 1
        delta[0][1] = 2
        delta[0][2] = 2
        delta[0][3] = 2
        delta[1][0] = 1
        delta[1][1] = 1
        delta[1][2] = 1
        delta[1][3] = 2
        delta[2][0] = 2
        delta[2][1] = 2
        delta[2][2] = 2
        delta[2][3] = 2
        lexema = ""
        auxControl = posicion
        T = arc.leerCaracter(linea, auxControl)
        estado = q0
        while (estado != 2) and auxControl < len(linea) and (T != " ") and (T != "\n") and not simbolo(linea, auxControl):
            estado = delta[estado][simboloID(T)]
            lexema = lexema + T
            auxControl = auxControl + 1
            T = arc.leerCaracter(linea, auxControl)
        if estado in F:
            return lexema
        else:
            return ""
    def simbolo (linea: str, posicion: int)-> bool:
                simb = False
                aux = arc.leerCaracter(linea,posicion)
                if aux in {'=', '<', '>', ':', '+', '-', '*', '/', ';', ',', '.', '(', ')', '[', ']'}:
                    simb = True
                return simb
    def simbolo1(linea: str, posicion: int) -> bool:
                simb = False
                aux = arc.leerCaracter(linea, posicion)
                if aux in {'=', '+', '*', '/', ';', ',', '(', ')', '[', ']'}:
                     simb = True