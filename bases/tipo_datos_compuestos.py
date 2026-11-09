arreglo = ["Jony", "Ing", True, 1.70]

print(arreglo)
#0 indexed
print(arreglo[0])

#tuplas no se pueden modificar, son inmutables
tupla = ("Jony", "Ing", True, 1.70)
print(tupla)    

#no se accede desde el indice, sino desde el valor, no permite duplicados, no es ordenado
# Solo se accede desde un bucle for
conjunto = {"Jony", "Ing", True, 1.70}
print(conjunto)

#diccionario de clave y valor, se accede desde la clave
diccionario = {
    "nombre": "Jony",
    "profesion": "Ing",
    "casado": True,
    "altura": 1.70
}
print(diccionario)  
print(diccionario["nombre"])    