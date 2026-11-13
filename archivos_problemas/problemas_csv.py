import pandas as pd

df = pd.read_csv("archivos_problemas/datos.csv")
print(df)
print("------------------")
#cambiar el tipo de dato de una columna
print(type(df["edad"][0]))
df["edad"] = df["edad"].astype(str)
print(type(df["edad"][0]))
print("------------------")
# sin el inplace no se reemplaza el original
df_modified = df["apellido"].replace("Sliver","Dolly", inplace=True)
print(df)
print("------------------")
#remover filas donde faltan datos
df = df.dropna()
print(df)
print("------------------")
#Eliminar repetidas
df = df.drop_duplicates()
print(df)

df.to_csv("archivos_problemas/datos_limpios.csv")