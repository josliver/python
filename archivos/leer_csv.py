import csv

with open("archivos/datos.csv") as archivo:
    contenido = csv.reader(archivo)
    print(f"tenemos {type(contenido)} y es {contenido}")
    for row in contenido:
        print(row)

#TODO: Aprender Pandas para análisis de datos