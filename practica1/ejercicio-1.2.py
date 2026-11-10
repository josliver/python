# calula el tiempo que una persona dice esa frase 
frase = input("Dime una frase: ")
palabras_separadas = frase.split(" ")
cantidad_palabras = len(palabras_separadas)

print(f"Dijiste {cantidad_palabras} y tardarías {cantidad_palabras / 2} segundos en decirla.")