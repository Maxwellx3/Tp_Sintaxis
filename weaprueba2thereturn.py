import pandas as pd
import scanner as sc

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('CSVTAS.csv', header=None)

componente_lexico = df.iloc[0, 1:].tolist()
variable = df.iloc[1:, 0].tolist()

# Crear el diccionario tas_dict
tas_dict = {}

# Iterar sobre las intersecciones de índices y guardar los valores en el diccionario
for var in range(len(variable)):
    for lex in range(1, len(componente_lexico) + 1):
        regla = df.iloc[var + 1, lex]
        if pd.notna(regla):
            regla_componentes = regla.split(',')  # Dividir la regla en componentes
        else:
            regla_componentes = []
        tas_dict[(variable[var], componente_lexico[lex - 1])] = regla_componentes

# Componente léxico y variable específicos para buscar
componente_lexico_buscar = 'id'
variable_buscar = 'prog'
if (variable_buscar, componente_lexico_buscar) in tas_dict:
    regla1= tas_dict[(variable_buscar, componente_lexico_buscar)]
    if not regla1:
        print('Es vacio')
    else:
        prim_letra= regla1[0]
        print(prim_letra)
