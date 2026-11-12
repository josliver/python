with open("archivos/text.txt", "+a") as archivo:
    # archivo.write("esto puede ser que re-escriba el archivo de gestión")
    archivo.writelines(["lorem ipsum\n", "piazo e loco "])
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Esta es la linea {i+1} del código\n")