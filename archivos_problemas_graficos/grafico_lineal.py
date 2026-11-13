import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos/pedos.csv")

print(df)
# Levanta una ventana con la gráfica pero no funciona en la pi
# sns.lineplot(x="fecha",y="pedos", data=df)

max = df["pedos"].max()
maximo_pedo = df.loc[df["pedos"].idxmax()]
#print(type(maximo_pedo))
#print(maximo_pedo)
fecha = maximo_pedo["fecha"]
pedos = int(maximo_pedo["pedos"])

#print(maximo_pedo["pedos"].)
print(f"__ {fecha} __ {pedos} ")
# plt.plot("01-09",17,"o")
# plt.plot(fecha, pedos,"o")
#print(f"Lo máximo en _ fueron {maximo_pedo["pedos"]} pedos")
#plt.plot(maximo_pedo["fecha"],maximo_pedo["pedos"],"o")
# plt.show()

