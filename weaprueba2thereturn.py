import pandas as pd
import scanner as sc

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('CSVTAS.csv', header=None)

componente_lexico = df.iloc[0, 1:].tolist()
variable = df.iloc[1:, 0].tolist()

# if set(componente_lexico) == set(sc.Terminal) and set(variable) == set(sc.Variables):
#     print("Componente Léxico:", componente_lexico)
#     print("Variable:", variable)



# # Busca e imprime la celda de intersección
# try:
#     indice_componente = componente_lexico.index(componente_lexico_buscar) + 1
#     indice_variable = variable.index(variable_buscar) + 1
#     regla = df.iloc[indice_variable, indice_componente]
#     print("Celda de intersección:", regla)
# except IndexError:
#     print("No se encontró la celda de intersección para el componente léxico '{}' y la variable '{}'.".format(componente_lexico_buscar, variable_buscar))


# Crear el diccionario tas_dict
tas_dict = {}

# Iterar sobre las intersecciones de índices y guardar los valores en el diccionario
for var in range(len(variable)):
    for lex in range(1, len(componente_lexico) + 1):
        regla = df.iloc[var + 1, lex]
        tas_dict[(variable[var], componente_lexico[lex - 1])] = regla

# Componente léxico y variable específicos para buscar
componente_lexico_buscar = 'id'
variable_buscar = 'A'
if (variable_buscar, componente_lexico_buscar) in tas_dict:
    regla1= tas_dict[(variable_buscar, componente_lexico_buscar)]
    if pd.isna(regla1):
        print('Es vacio')
    else:
        prim_letra= regla1[0]
        print(prim_letra)

# if any('prog' in key for key in tas_dict.keys()):
#     print('Asi es')
# else:
#     print('Asi no es')