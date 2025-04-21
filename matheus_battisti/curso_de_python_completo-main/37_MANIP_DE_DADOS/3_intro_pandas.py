# aula 1 - intro padas
import pandas as pd

series = pd.Series([10, 20 ,30, 40])

print(series)

data = {'Nome': ['Ana', "João", 'Maria'], 'Idade': [20, 32, 44]}

df = pd.DataFrame(data)

print(df)

print(df.info())

print(df.describe())

# aula 2 - criacao de dataframes

df = pd.DataFrame([[1, 'A'], [2, 'B'], [3, 'C']], columns=['ID', 'Letra'])

print(df)

import numpy as np

array = np.array([[10, 20], [30, 40]])

df = pd.DataFrame(array, columns=['Col1', 'Col2'])

print(df)

df = pd.read_csv('dados.csv')

print(df)

df = pd.read_csv('teste.csv')

df = df.fillna(1).infer_objects(copy=False)

print(df)


# aula 3 - manipulacao com pandas


df['Está Empregado'] = [False, False, True, True, False]

print(df)

df = df.drop(columns=["Idade"])

print(df)

df['Salário'] = df['Salário'] + 100

print(df)

df['Categoria'] = df['Salário'].apply(lambda x: 'Ganha bem' if x > 4000 else 'Ganha mal')

print(df)

# aula 4 - valores ausentes

df = pd.DataFrame({'A': [1, None, 3], 'B': [1, 5, None] ,'C': [6, None, None]})

print(df.isnull())

df_sem_nulos = df.dropna()

print(df_sem_nulos)

df_preenchido = df.fillna(0).infer_objects(copy=False)

print(df_preenchido)

df_ffill = df.ffill().infer_objects(copy=False)

print(df_ffill)