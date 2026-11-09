cadena1="Hola Mundo"
cadena2="Jony dize"

#dir devuelve una lista de los atributos y métodos de cualquier objeto (funciones, variables, etc.) que pertenezcan al objeto especificado.
print(dir(cadena1))

print(cadena1.upper()) # convierte la cadena a mayusculas
print(cadena1.lower()) # convierte la cadena a minusculas
print(cadena1.capitalize()) # convierte la primera letra de la cadena a mayuscula
print(cadena2.title()) # convierte la primera letra de cada palabra a mayuscula
print(cadena1.count("o")) # cuenta cuantas veces aparece la letra "o" en la cadena

print(cadena1.find("Mundo")) # devuelve la posicion de la primera letra de la palabra "Mundo", 
# si no la encuentra devuelve -1
print(cadena1.index("Mundo")) # devuelve la posicion de la primera letra de la palabra "Mundo",
# si no la encuentra devuelve un error
print(cadena1.startswith("Hola")) # devuelve True si la cadena empieza con "Hola"
print(cadena1.endswith("Mundo")) # devuelve True si la cadena termina con "Mundo"


print(cadena1.isalpha()) # devuelve True si la cadena solo contiene letras
print(cadena1.isdigit()) # devuelve True si la cadena solo contiene numeros
print(cadena1.isalnum()) # devuelve True si la cadena contiene solo letras y numeros
print(cadena1.isnumeric()) # devuelve True si la cadena contiene solo numeros

print(cadena1.strip()) # elimina los espacios en blanco al inicio y al final de la cadena
print(cadena1.count("o")) # cuenta cuantas veces aparece la letra "o" en la cadena
print(len(cadena1)) # devuelve la longitud de la cadena


print(cadena1.replace("Mundo", "Python")) # reemplaza la palabra "Mundo" por "Python"
print(cadena1.split(" ")) # divide la cadena en una lista  