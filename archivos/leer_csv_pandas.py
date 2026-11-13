import pandas as pd

print(type(pd))

df = pd.read_csv("archivos/datos.csv")
df2 = pd.read_csv("archivos/datos.csv")

print(df["nombre"])

cadena = "123456790"
print(cadena[3])

#Slicing
print(cadena[:])
print(cadena[:3])
print(cadena[1:3])

#dataframes
df_ordenado_asc = df.sort_values("edad")
df_ordenado_desc = df.sort_values("edad", ascending=False)
print(df_ordenado_asc)
print(df_ordenado_desc)

#concatenando dataframes
df_concatenado = pd.concat([df,df2])

print(df_concatenado)

# Accediendo a las primeras filas
primera_fila = df.head(2)
print (primera_fila)

#accedidendo de bottom-up
ultimas_filas = df.tail(2)
print (ultimas_filas)

filas, columnas = df.shape
print(f"filas {filas} y columnas {columnas}")

#estadisticas sobre la matriz
df_info = df.describe()
print(df_info)

#accediendo al df con loc

elemento_especifico_loc = df.loc[2,"edad"]
print(elemento_especifico_loc)
print("-----------")
elemento_especifico_iloc = df.iloc[2,2]
print(elemento_especifico_iloc)
print("-----------")
apellido_loc = df.loc[:,"apellido"]
print(apellido_loc)
print("-----------")
fila3_loc = df.loc[2,:]
print(fila3_loc)
print("-----------")

#mayor que 30
mayor_30 = df.loc[df["edad"] > 30, :]
print(mayor_30)