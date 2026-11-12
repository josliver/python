frutas = ["manzana", "banana", "cereza", "durazno", "kiwi", "limón", "mango", "naranja", "papaya", "pera"]

for fruta in frutas:
    if fruta == "kiwi":
        continue
    print(f"Voy a comer{fruta}")

for fruta in frutas:
    if fruta == "limón":
        break
    print(f"Voy a comer {fruta}")

#recorriendo cadenas de texto
cadena = "Hola mundo"
for letra in cadena:
    print(f"Voy a imprimir la letra {letra}")

#inline for
numeros = [1, 2, 3, 4, 5]
print([numero * 2 for numero in numeros])

print("Fin del programa")