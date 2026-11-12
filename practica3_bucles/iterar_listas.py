animales = ["perro", "gato", "conejo", "hamster", "pez"]
numeros = [1, 2, 3, 4, 5]

# Estas iteraciones funcionan con cualquier tipo de lista, tupla, diccionario o conjunto
# basicamente cualquier objeto iterable
print("----------------------------------")
for animal in animales:
    print(animal)
print("----------------------------------")
#Si tenemos 2 listas, podemos iterar sobre ambas al mismo tiempo con la función zip()
#siempre y cuando tengan la misma longitud, si no, se detendrá en la lista más corta
for animal, numero in zip(animales, numeros):   
    print(f"El animal {animal} tiene el número {numero}")
print("----------------------------------")
#Con range() podemos iterar sobre un rango de números, por ejemplo, del 0 al 9
for num in range(10):
    print(num)
print("----------------------------------")
for num in range(len(numeros)):
    print(numeros[num] )

}#Forma optimizada con enumerate() para obtener el índice y el valor al mismo tiempo
for index, num in enumerate(numeros):
    print(f"El número en la posición {index} es {num}") 
print("----------------------------------")
#TODO: Trabajo con matrices, listas de listas, diccionarios y conjuntos