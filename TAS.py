import scanner as s
import pandas as pd

igual = s.igual
mayor = s.mayor
menor = s.menor
mayorIgual = s.mayorIgual
menorIgual = s.menorIgual
distinto = s.distinto
asignar = s.asignar
opAnd = s.opAnd
opNeg = s.opNeg
opOr = s.opOr
mas = s.mas
menos = s.menos
por = s.por
dividido = s.dividido
potencia = s.potencia
raiz = s.raiz
puntoycoma= s.puntoycoma
coma = s.coma
punto = s.punto
parentesisAbre = s.parentesisAbre
parentesisCierra = s.parentesisCierra
corcheteAbre = s.corcheteAbre
corcheteCierra = s.corcheteCierra
cadena = s.cadena
LEER = s.LEER
ESCRIBIR = s.ESCRIBIR
MIENTRAS = s.MIENTRAS
SI = s.SI
SINO = s.SINO
real = s.real
id = s.id
ErrorLexico = s.ErrorLexico
G = s.G
J = s.J
F = s.F
K = s.K
X = s.X
Y = s.Y
Z = s.Z
A = s.A
B = s.B
C = s.C
prog = s.prog
sent = s.sent
var = s.var
asig = s.asig
expArit = s.expArit
ciclo = s.ciclo
cond = s.cond
sigCond = s.sigCond
condIf = s.condIf
bloque = s.bloque
lect = s.lect
escr = s.escr
epsilon = s.epsilon
peso = s.peso


######################################################################################################
###########################################       TAS       ##########################################
######################################################################################################

# cTAS = [None] * 23
# for i in range(23):
#     cTAS[i] = [None] * 31
# cTAS[0][0] =[]
# cTAS[0][1] = []
# cTAS[0][2] = []
# cTAS[0][3] = [sent, G]
# cTAS[0][4] = []
# cTAS[0][5] = [sent, G]
# cTAS[0][6] = [sent, G]
# cTAS[0][7] = []
# cTAS[0][8] = [sent, G]
# cTAS[0][9] = [sent, G]
# cTAS[0][10] = []
# cTAS[0][11] = []
# cTAS[0][12] = []
# cTAS[0][13] = []
# cTAS[0][14] = []
# cTAS[0][15] = []
# cTAS[0][16] = []
# cTAS[0][17] = []
# cTAS[0][18] = []
# cTAS[0][19] = []
# cTAS[0][20] = []
# cTAS[0][21] = []
# cTAS[0][22] = []
# cTAS[0][23] = []
# cTAS[0][24] = []
# cTAS[0][25] = []
# cTAS[0][26] = []
# cTAS[0][27] = []
# cTAS[0][28] = []
# cTAS[0][29] = []
# cTAS[0][30] = []
# cTAS[1][0] = [puntoycoma, sent, G]
# cTAS[1][1] = []
# cTAS[1][2] = []
# cTAS[1][3] = [sent, G]
# cTAS[1][4] = []
# cTAS[1][5] = [sent, G]
# cTAS[1][6] = [sent, G]
# cTAS[1][7] = []
# cTAS[1][8] = [sent, G]
# cTAS[1][9] = [sent, G]
# cTAS[1][10] = []
# cTAS[1][11] = []  
# cTAS[1][12] = []
# cTAS[1][13] = []
# cTAS[1][14] = []
# cTAS[1][15] = []
# cTAS[1][16] = []
# cTAS[1][17] = []
# cTAS[1][18] = []
# cTAS[1][19] = []
# cTAS[1][20] = [epsilon] #no sale este epsilon
# cTAS[1][21] = []
# cTAS[1][22] = []
# cTAS[1][23] = []
# cTAS[1][24] = []
# cTAS[1][25] = []
# cTAS[1][26] = []
# cTAS[1][27] = []
# cTAS[1][28] = []
# cTAS[1][29] = []
# cTAS[1][30] = [epsilon]
# cTAS[2][0] = []
# cTAS[2][1] = []
# cTAS[2][2] = []
# cTAS[2][3] = [var]
# cTAS[2][4] = []
# cTAS[2][5] = [ciclo]
# cTAS[2][6] = [condIf]
# cTAS[2][7] = []
# cTAS[2][8] = [lect]
# cTAS[2][9] = [escr]
# cTAS[2][10] = []
# cTAS[2][11] = []
# cTAS[2][12] = []
# cTAS[2][13] = []
# cTAS[2][14] = []
# cTAS[2][15] = []
# cTAS[2][16] = []
# cTAS[2][17] = []
# cTAS[2][18] = []
# cTAS[2][19] = []
# cTAS[2][20] = []
# cTAS[2][21] = []
# cTAS[2][22] = []
# cTAS[2][23] = []
# cTAS[2][24] = []
# cTAS[2][25] = []
# cTAS[2][26] = []
# cTAS[2][27] = []
# cTAS[2][28] = []
# cTAS[2][29] = []
# cTAS[2][30] = []
# cTAS[3][0] = []
# cTAS[3][1] = []
# cTAS[3][2] = []
# cTAS[3][3] = [id, asig]
# cTAS[3][4] = []
# cTAS[3][5] = []
# cTAS[3][6] = []
# cTAS[3][7] = []
# cTAS[3][8] = []
# cTAS[3][9] = []
# cTAS[3][10] = []
# cTAS[3][11] = []
# cTAS[3][12] = []
# cTAS[3][13] = []
# cTAS[3][14] = []
# cTAS[3][15] = []
# cTAS[3][16] = []
# cTAS[3][17] = []
# cTAS[3][18] = []
# cTAS[3][19] = []
# cTAS[3][20] = []
# cTAS[3][21] = []
# cTAS[3][22] = []
# cTAS[3][23] = []
# cTAS[3][24] = []
# cTAS[3][25] = []
# cTAS[3][26] = []
# cTAS[3][27] = []
# cTAS[3][28] = []
# cTAS[3][29] = []
# cTAS[3][30] = []
# cTAS[4][0] = []
# cTAS[4][1] = [asignar, expArit]
# cTAS[4][2] = [coma, id, asig]
# cTAS[4][3] = [id, asignar, expArit]
# cTAS[4][4] = []
# cTAS[4][5] = []
# cTAS[4][6] = []
# cTAS[4][7] = []
# cTAS[4][8] = []
# cTAS[4][9] = []
# cTAS[4][10] = []
# cTAS[4][11] = []
# cTAS[4][12] = []
# cTAS[4][13] = []
# cTAS[4][14] = []
# cTAS[4][15] = []
# cTAS[4][16] = []
# cTAS[4][17] = []
# cTAS[4][18] = []
# cTAS[4][19] = []
# cTAS[4][20] = []
# cTAS[4][21] = []
# cTAS[4][22] = []
# cTAS[4][23] = []
# cTAS[4][24] = []
# cTAS[4][25] = []
# cTAS[4][26] = []
# cTAS[4][27] = []
# cTAS[4][28] = []
# cTAS[4][29] = []
# cTAS[4][30] = []
# cTAS[5][0] = []
# cTAS[5][1] = []
# cTAS[5][2] = []
# cTAS[5][3] = [A, X]
# cTAS[5][4] = [A, X]
# cTAS[5][5] = []
# cTAS[5][6] = []
# cTAS[5][7] = []
# cTAS[5][8] = []
# cTAS[5][9] = []
# cTAS[5][10] = []
# cTAS[5][11] = []
# cTAS[5][12] = []
# cTAS[5][13] = []
# cTAS[5][14] = []
# cTAS[5][15] = []
# cTAS[5][16] = []
# cTAS[5][17] = [A, X]
# cTAS[5][18] = []
# cTAS[5][19] = []
# cTAS[5][20] = []
# cTAS[5][21] = []
# cTAS[5][22] = []
# cTAS[5][23] = []
# cTAS[5][24] = []
# cTAS[5][25] = []
# cTAS[5][26] = []
# cTAS[5][27] = []
# cTAS[5][28] = []
# cTAS[5][29] = []
# cTAS[5][30] = []
# cTAS[6][0] = []
# cTAS[6][1] = []
# cTAS[6][2] = []
# cTAS[6][3] = [B, Y]
# cTAS[6][4] = [B, Y]
# cTAS[6][5] = []
# cTAS[6][6] = []
# cTAS[6][7] = []
# cTAS[6][8] = []
# cTAS[6][9] = []
# cTAS[6][10] = []
# cTAS[6][11] = []
# cTAS[6][12] = []
# cTAS[6][13] = []
# cTAS[6][14] = []
# cTAS[6][15] = []
# cTAS[6][16] = []
# cTAS[6][17] = [B, Y]
# cTAS[6][18] = []
# cTAS[6][19] = []
# cTAS[6][20] = []
# cTAS[6][21] = []
# cTAS[6][22] = []
# cTAS[6][23] = []
# cTAS[6][24] = []
# cTAS[6][25] = []
# cTAS[6][26] = []
# cTAS[6][27] = []
# cTAS[6][28] = []
# cTAS[6][29] = []
# cTAS[6][30] = []
# cTAS[7][0] = [epsilon]
# cTAS[7][1] = []
# cTAS[7][2] = []
# cTAS[7][3] = []
# cTAS[7][4] = []
# cTAS[7][5] = []
# cTAS[7][6] = []
# cTAS[7][7] = []
# cTAS[7][8] = []
# cTAS[7][9] = []
# cTAS[7][10] = []
# cTAS[7][11] = [mas, A, X]
# cTAS[7][12] = [menos, A, X]
# cTAS[7][13] = []
# cTAS[7][14] = []
# cTAS[7][15] = []
# cTAS[7][16] = []
# cTAS[7][17] = []
# cTAS[7][18] = [epsilon]
# cTAS[7][19] = [epsilon]
# cTAS[7][20] = []
# cTAS[7][21] = [epsilon]
# cTAS[7][22] = [epsilon]
# cTAS[7][23] = []
# cTAS[7][24] = [epsilon]
# cTAS[7][25] = [epsilon]
# cTAS[7][26] = [epsilon]
# cTAS[7][27] = [epsilon]
# cTAS[7][28] = [epsilon]
# cTAS[7][29] = [epsilon]
# cTAS[7][30] = []
# cTAS[8][0] = []
# cTAS[8][1] = []
# cTAS[8][2] = []
# cTAS[8][3] = [C, Z]
# cTAS[8][4] = [C, Z]
# cTAS[8][5] = []
# cTAS[8][6] = []
# cTAS[8][7] = []
# cTAS[8][8] = []
# cTAS[8][9] = []
# cTAS[8][10] = []
# cTAS[8][11] = []
# cTAS[8][12] = []
# cTAS[8][13] = []
# cTAS[8][14] = []
# cTAS[8][15] = []
# cTAS[8][16] = []
# cTAS[8][17] = [C, Z]
# cTAS[8][18] = []
# cTAS[8][19] = []
# cTAS[8][20] = []
# cTAS[8][21] = []
# cTAS[8][22] = []
# cTAS[8][23] = []
# cTAS[8][24] = []
# cTAS[8][25] = []
# cTAS[8][26] = []
# cTAS[8][27] = []
# cTAS[8][28] = []
# cTAS[8][29] = []
# cTAS[8][30] = []
# cTAS[9][0] = [epsilon]
# cTAS[9][1] = []
# cTAS[9][2] = []
# cTAS[9][3] = []
# cTAS[9][4] = []
# cTAS[9][5] = []
# cTAS[9][6] = []
# cTAS[9][7] = []
# cTAS[9][8] = []
# cTAS[9][9] = []
# cTAS[9][10] = []
# cTAS[9][11] = [epsilon]
# cTAS[9][12] = [epsilon]
# cTAS[9][13] = [por, B, Y]
# cTAS[9][14] = [dividido, B, Y]
# cTAS[9][15] = []
# cTAS[9][16] = []
# cTAS[9][17] = []
# cTAS[9][18] = [epsilon]
# cTAS[9][19] = [epsilon]
# cTAS[9][20] = []
# cTAS[9][21] = [epsilon]
# cTAS[9][22] = [epsilon]
# cTAS[9][23] = []
# cTAS[9][24] = [epsilon]
# cTAS[9][25] = [epsilon]
# cTAS[9][26] = [epsilon]
# cTAS[9][27] = [epsilon]
# cTAS[9][28] = [epsilon]
# cTAS[9][29] = [epsilon]
# cTAS[9][30] = []
# cTAS[10][0] = []
# cTAS[10][1] = []
# cTAS[10][2] = []
# cTAS[10][3] = [id]
# cTAS[10][4] = [real]
# cTAS[10][5] = []
# cTAS[10][6] = []
# cTAS[10][7] = []
# cTAS[10][8] = []
# cTAS[10][9] = []
# cTAS[10][10] = []
# cTAS[10][11] = []
# cTAS[10][12] = []
# cTAS[10][13] = []
# cTAS[10][14] = []
# cTAS[10][15] = []
# cTAS[10][16] = []
# cTAS[10][17] = [parentesisAbre, expArit, parentesisCierra]
# cTAS[10][18] = []
# cTAS[10][19] = []
# cTAS[10][20] = []
# cTAS[10][21] = []
# cTAS[10][22] = []
# cTAS[10][23] = []
# cTAS[10][24] = []
# cTAS[10][25] = []
# cTAS[10][26] = []
# cTAS[10][27] = []
# cTAS[10][28] = []
# cTAS[10][29] = []
# cTAS[10][30] = []
# cTAS[11][0] = [epsilon]
# cTAS[11][1] = []
# cTAS[11][2] = []
# cTAS[11][3] = []
# cTAS[11][4] = []
# cTAS[11][5] = []
# cTAS[11][6] = []
# cTAS[11][7] = []
# cTAS[11][8] = []
# cTAS[11][9] = []
# cTAS[11][10] = []
# cTAS[11][11] = [epsilon]
# cTAS[11][12] = [epsilon]
# cTAS[11][13] = [epsilon]
# cTAS[11][14] = [epsilon]
# cTAS[11][15] = [potencia, C, Z]
# cTAS[11][16] = [raiz, C, Z]
# cTAS[11][17] = []
# cTAS[11][18] = [epsilon]
# cTAS[11][19] = [epsilon]
# cTAS[11][20] = []
# cTAS[11][21] = [epsilon]
# cTAS[11][22] = [epsilon]
# cTAS[11][23] = []
# cTAS[11][24] = [epsilon]
# cTAS[11][25] = [epsilon]
# cTAS[11][26] = [epsilon]
# cTAS[11][27] = [epsilon]
# cTAS[11][28] = [epsilon]
# cTAS[11][29] = [epsilon]
# cTAS[11][30] = []
# cTAS[12][0] = []
# cTAS[12][1] = []
# cTAS[12][2] = []
# cTAS[12][3] = []
# cTAS[12][4] = []
# cTAS[12][5] = [MIENTRAS, cond, bloque]
# cTAS[12][6] = []
# cTAS[12][7] = []
# cTAS[12][8] = []
# cTAS[12][9] = []
# cTAS[12][10] = []
# cTAS[12][11] = []
# cTAS[12][12] = []
# cTAS[12][13] = []
# cTAS[12][14] = []
# cTAS[12][15] = []
# cTAS[12][16] = []
# cTAS[12][17] = []
# cTAS[12][18] = []
# cTAS[12][19] = []
# cTAS[12][20] = []
# cTAS[12][21] = []
# cTAS[12][22] = []
# cTAS[12][23] = []
# cTAS[12][24] = []
# cTAS[12][25] = []
# cTAS[12][26] = []
# cTAS[12][27] = []
# cTAS[12][28] = []
# cTAS[12][29] = []
# cTAS[12][30] = []
# cTAS[13][0] = []
# cTAS[13][1] = []
# cTAS[13][2] = []
# cTAS[13][3] = [expArit, K]
# cTAS[13][4] = [expArit, K]
# cTAS[13][5] = []
# cTAS[13][6] = []
# cTAS[13][7] = []
# cTAS[13][8] = []
# cTAS[13][9] = []
# cTAS[13][10] = []
# cTAS[13][11] = []
# cTAS[13][12] = []
# cTAS[13][13] = []
# cTAS[13][14] = []
# cTAS[13][15] = []
# cTAS[13][16] = []
# cTAS[13][17] = [expArit, K]
# cTAS[13][18] = []
# cTAS[13][19] = []
# cTAS[13][20] = []
# cTAS[13][21] = []
# cTAS[13][22] = []
# cTAS[13][23] = [sigCond, K]
# cTAS[13][24] = []
# cTAS[13][25] = []
# cTAS[13][26] = []
# cTAS[13][27] = []
# cTAS[13][28] = []
# cTAS[13][29] = []
# cTAS[13][30] = []
# cTAS[14][0] = []
# cTAS[14][1] = []
# cTAS[14][2] = []
# cTAS[14][3] = [expArit, J]
# cTAS[14][4] = [expArit, J]
# cTAS[14][5] = []
# cTAS[14][6] = []
# cTAS[14][7] = []
# cTAS[14][8] = []
# cTAS[14][9] = []
# cTAS[14][10] = []
# cTAS[14][11] = []
# cTAS[14][12] = []
# cTAS[14][13] = []
# cTAS[14][14] = []
# cTAS[14][15] = []
# cTAS[14][16] = []
# cTAS[14][17] = [expArit, J]
# cTAS[14][18] = []
# cTAS[14][19] = []
# cTAS[14][20] = []
# cTAS[14][21] = []
# cTAS[14][22] = []
# cTAS[14][23] = [opNeg, sigCond]
# cTAS[14][24] = []
# cTAS[14][25] = []
# cTAS[14][26] = []
# cTAS[14][27] = []
# cTAS[14][28] = []
# cTAS[14][29] = []
# cTAS[14][30] = []
# cTAS[15][0] = []
# cTAS[15][1] = []
# cTAS[15][2] = []
# cTAS[15][3] = []
# cTAS[15][4] = []
# cTAS[15][5] = []
# cTAS[15][6] = []
# cTAS[15][7] = []
# cTAS[15][8] = []
# cTAS[15][9] = []
# cTAS[15][10] = []
# cTAS[15][11] = []
# cTAS[15][12] = []
# cTAS[15][13] = []
# cTAS[15][14] = []
# cTAS[15][15] = []
# cTAS[15][16] = []
# cTAS[15][17] = []
# cTAS[15][18] = []
# cTAS[15][19] = [epsilon]
# cTAS[15][20] = []
# cTAS[15][21] = [opOr, sigCond, K]
# cTAS[15][22] = [opAnd, sigCond, K]
# cTAS[15][23] = []
# cTAS[15][24] = []
# cTAS[15][25] = []
# cTAS[15][26] = []
# cTAS[15][27] = []
# cTAS[15][28] = []
# cTAS[15][29] = []
# cTAS[15][30] = []
# cTAS[16][0] = []
# cTAS[16][1] = []
# cTAS[16][2] = []
# cTAS[16][3] = []
# cTAS[16][4] = []
# cTAS[16][5] = []
# cTAS[16][6] = []
# cTAS[16][7] = []
# cTAS[16][8] = []
# cTAS[16][9] = []
# cTAS[16][10] = []
# cTAS[16][11] = []
# cTAS[16][12] = []
# cTAS[16][13] = []
# cTAS[16][14] = []
# cTAS[16][15] = []
# cTAS[16][16] = []
# cTAS[16][17] = []
# cTAS[16][18] = []
# cTAS[16][19] = []
# cTAS[16][20] = []
# cTAS[16][21] = []
# cTAS[16][22] = []
# cTAS[16][23] = []
# cTAS[16][24] = [menor, expArit]
# cTAS[16][25] = [mayor, expArit]
# cTAS[16][26] = [distinto, expArit]
# cTAS[16][27] = [igual, expArit]
# cTAS[16][28] = [menorIgual, expArit]
# cTAS[16][29] = [mayorIgual, expArit]
# cTAS[16][30] = []
# cTAS[17][0] = []
# cTAS[17][1] = []
# cTAS[17][2] = []
# cTAS[17][3] = []
# cTAS[17][4] = []
# cTAS[17][5] = []
# cTAS[17][6] = [SI, cond, bloque, F]
# cTAS[17][7] = []
# cTAS[17][8] = []
# cTAS[17][9] = []
# cTAS[17][10] = []
# cTAS[17][11] = []
# cTAS[17][12] = []
# cTAS[17][13] = []
# cTAS[17][14] = []
# cTAS[17][15] = []
# cTAS[17][16] = []
# cTAS[17][17] = []
# cTAS[17][18] = []
# cTAS[17][19] = []
# cTAS[17][20] = []
# cTAS[17][21] = []
# cTAS[17][22] = []
# cTAS[17][23] = []
# cTAS[17][24] = []
# cTAS[17][25] = []
# cTAS[17][26] = []
# cTAS[17][27] = []
# cTAS[17][28] = []
# cTAS[17][29] = []
# cTAS[17][30] = []
# cTAS[18][0] = [epsilon]
# cTAS[18][1] = []
# cTAS[18][2] = []
# cTAS[18][3] = []
# cTAS[18][4] = []
# cTAS[18][5] = []
# cTAS[18][6] = []
# cTAS[18][7] = [SINO, bloque]
# cTAS[18][8] = []
# cTAS[18][9] = []
# cTAS[18][10] = []
# cTAS[18][11] = []
# cTAS[18][12] = []
# cTAS[18][13] = []
# cTAS[18][14] = []
# cTAS[18][15] = []
# cTAS[18][16] = []
# cTAS[18][17] = []
# cTAS[18][18] = []
# cTAS[18][19] = []
# cTAS[18][20] = []
# cTAS[18][21] = []
# cTAS[18][22] = []
# cTAS[18][23] = []
# cTAS[18][24] = []
# cTAS[18][25] = []
# cTAS[18][26] = []
# cTAS[18][27] = []
# cTAS[18][28] = []
# cTAS[18][29] = []
# cTAS[18][30] = []
# cTAS[19][0] = []
# cTAS[19][1] = []
# cTAS[19][2] = []
# cTAS[19][3] = []
# cTAS[19][4] = []
# cTAS[19][5] = []
# cTAS[19][6] = []
# cTAS[19][7] = []
# cTAS[19][8] = []
# cTAS[19][9] = []
# cTAS[19][10] = []
# cTAS[19][11] = []
# cTAS[19][12] = []
# cTAS[19][13] = []
# cTAS[19][14] = []
# cTAS[19][15] = []
# cTAS[19][16] = []
# cTAS[19][17] = []
# cTAS[19][18] = []
# cTAS[19][19] = [corcheteAbre, prog, corcheteCierra]
# cTAS[19][20] = []
# cTAS[19][21] = []
# cTAS[19][22] = []
# cTAS[19][23] = []
# cTAS[19][24] = []
# cTAS[19][25] = []
# cTAS[19][26] = []
# cTAS[19][27] = []
# cTAS[19][28] = []
# cTAS[19][29] = []
# cTAS[19][30] = []
# cTAS[20][0] = []
# cTAS[20][1] = []
# cTAS[20][2] = []
# cTAS[20][3] = []
# cTAS[20][4] = []
# cTAS[20][5] = []
# cTAS[20][6] = []
# cTAS[20][7] = []
# cTAS[20][8] = [LEER, parentesisAbre, cadena, coma, id, parentesisCierra]
# cTAS[20][9] = []
# cTAS[20][10] = []
# cTAS[20][11] = []
# cTAS[20][12] = []
# cTAS[20][13] = []
# cTAS[20][14] = []
# cTAS[20][15] = []
# cTAS[20][16] = []
# cTAS[20][17] = []
# cTAS[20][18] = []
# cTAS[20][19] = []
# cTAS[20][20] = []
# cTAS[20][21] = []
# cTAS[20][22] = []
# cTAS[20][23] = []
# cTAS[20][24] = []
# cTAS[20][25] = []
# cTAS[20][26] = []
# cTAS[20][27] = []
# cTAS[20][28] = []
# cTAS[20][29] = []
# cTAS[20][30] = []
# cTAS[21][0] = []
# cTAS[21][1] = []
# cTAS[21][2] = []
# cTAS[21][3] = []
# cTAS[21][4] = []
# cTAS[21][5] = []
# cTAS[21][6] = []
# cTAS[21][7] = []
# cTAS[21][8] = []
# cTAS[21][9] = [ESCRIBIR, parentesisAbre, cadena, coma, expArit, parentesisCierra]
# cTAS[21][10] = []
# cTAS[21][11] = []
# cTAS[21][12] = []
# cTAS[21][13] = []
# cTAS[21][14] = []
# cTAS[21][15] = []
# cTAS[21][16] = []
# cTAS[21][17] = []
# cTAS[21][18] = []
# cTAS[21][19] = []
# cTAS[21][20] = []
# cTAS[21][21] = []
# cTAS[21][22] = []
# cTAS[21][23] = []
# cTAS[21][24] = []
# cTAS[21][25] = []
# cTAS[21][26] = []
# cTAS[21][27] = []
# cTAS[21][28] = []
# cTAS[21][29] = []
# cTAS[21][30] = []




# Crea un DataFrame a partir de las reglas
df = pd.read_csv (r"C:\Users\mache\OneDrive\Documentos\sintaxisTAS\TAS.csv")



# Transpone el DataFrame para que las reglas estén en filas y los símbolos en columnas
df = df.T

# Agrega nombres de columnas a las filas y coloca NaN donde sea necesario
df.columns = df.iloc[0]
df = df.iloc[1:]
df = df.fillna("")

# Imprime el DataFrame resultante
print(df)



def tVecTASVacio(x): #controla si el vector que devuelve la tas esta vacio
    if x != []:
        return False
    else:
        return True

def tas(produccion, simbolo): # devuelve el vector que se encuentra en la posicion de la tas, produccion son variables y simbolo son tipos de componentes lexicos
  i = 0
  j = 0
  if simbolo == puntoycoma:
      j = 0
  elif simbolo == asignar:
      j = 1
  elif simbolo == coma:
      j = 2
  elif simbolo == id:
      j = 3
  elif simbolo == real:
      j = 4
  elif simbolo == MIENTRAS:
      j = 5
  elif simbolo == SI:
      j = 6
  elif simbolo == SINO:
      j = 7
  elif simbolo == LEER:
      j = 8
  elif simbolo == ESCRIBIR:
      j = 9
  elif simbolo == cadena:
      j = 10
  elif simbolo == mas:
      j = 11
  elif simbolo == menos:
      j = 12
  elif simbolo == por:
      j = 13
  elif simbolo == dividido:
      j = 14
  elif simbolo == potencia:
      j = 15
  elif simbolo == raiz:
      j = 16
  elif simbolo == parentesisAbre:
      j = 17
  elif simbolo == parentesisCierra:
      j = 18
  elif simbolo == corcheteAbre:
      j = 19
  elif simbolo == corcheteCierra:
      j = 20
  elif simbolo == opOr:
      j = 21
  elif simbolo == opAnd:
      j = 22
  elif simbolo == opNeg:
      j = 23
  elif simbolo == menor:
      j = 24
  elif simbolo == mayor:
      j = 25
  elif simbolo == distinto:
      j = 26
  elif simbolo == igual:
      j = 27
  elif simbolo == menorIgual:
      j = 28
  elif simbolo == mayorIgual:
      j = 29
  elif simbolo == peso:
      j = 30
  if produccion == prog:
      i = 0
  elif produccion == G:
      i = 1
  elif produccion == sent:
      i = 2
  elif produccion == var:
      i = 3
  elif produccion == asig:
      i = 4
  elif produccion == expArit:
      i = 5
  elif produccion == A:
      i = 6
  elif produccion == X:
      i = 7
  elif produccion == B:
      i = 8
  elif produccion == Y:
      i = 9
  elif produccion == C:
      i = 10
  elif produccion == Z:
      i = 11
  elif produccion == ciclo:
      i = 12
  elif produccion == cond:
      i = 13
  elif produccion == sigCond:
      i = 14
  elif produccion == K:
      i = 15
  elif produccion == J:
      i = 16
  elif produccion == condIf:
      i = 17
  elif produccion == F:
      i = 18
  elif produccion == bloque:
      i = 19
  elif produccion == lect:
      i = 20
  elif produccion == escr:
      i = 21
  resul = cTAS[i][j]
  return resul

#######