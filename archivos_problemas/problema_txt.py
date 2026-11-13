#2 listas, una con nombres y otra con apellidos

nombres = ["Jon", "Ana", "Mario", "Lisa"]
apellidos = ["Doe", "Minelli", "Bros", "Simpson"]

with open("archivos_problemas/nombres_apellidos.txt","w") as archivo:
    archivo.writelines("Los datos son: \n")
    archivo.writelines(f"Nombre: {nombre}, Apellido: {apellido} \n" for nombre,apellido in zip(nombres, apellidos))