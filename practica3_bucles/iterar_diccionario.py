diccionario = {
    "nombre": "Jony",
    "profesion": "Ing",
    "casado": True,
    "altura": 1.70
}

for datos in diccionario:
    print(f"{type(datos)} - {datos}") #imprime las claves del diccionario

for datos in diccionario.values():
    print(f"{type(datos)} - {datos}") #imprime los valores del diccionario

for datos in diccionario.items():
    print(f"{type(datos)} - {datos}") #imprime las claves y valores del diccionario como tuplas