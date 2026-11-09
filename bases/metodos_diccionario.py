diccionario = dict({"nombre": "Jony", "profesion": "Ing", "casado": True, "altura": 1.70})
print(diccionario)

print(diccionario.keys()) # devuelve las claves del diccionario
print(diccionario.values()) # devuelve los valores del diccionario
print(diccionario.items()) # devuelve los pares clave-valor del diccionario

print(diccionario.get("nombre")) # devuelve el valor de la clave "nombre"
print(diccionario["profesion"]) # devuelve el valor de la clave "profesion"
diccionario["edad"] = 30 # agrega una nueva clave-valor al diccionario
print(diccionario)