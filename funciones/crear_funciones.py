#creando una funcion simple
def saludar():
    print("Maestro, ¿cómo estás?")

saludar()

#función con parámetros y uno con valor por defecto
def saludo_personalizado(nombre, sexo="masculino"):
    if sexo == "masculino":
        adjetivo = "crack"
    else:
        adjetivo = "amor"

    print(f"Hola {nombre} {adjetivo}, ¿cómo estás?")

nombre_usuario = input("Ingresa tu nombre: ")
saludo_personalizado(nombre_usuario)
#saludo_personalizado("Juan")

#funcion con return
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("El resultado de la suma es:", resultado)

def crear_contrasena(semilla):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    num_entero = str(semilla)
    num = int(num_entero[-1])  # Tomar el último dígito de la semilla como número
    c1 = num - 2
    c2 = num
    c3 = num - 5
    c4 = num

    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{semilla*2}"

    return contrasena

print(crear_contrasena(27))
    
 #   import random
 #   import string
 #   caracteres = string.ascii_letters + string.digits + string.punctuation
 #   contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
 #   return contraseña

#función recursiva
def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)

entero = int(input("dame un número: "))
print(f"factorial normal {factorial(entero)}")

#recursiva con if inline
def factorial_inline(numero):
    return 1 if numero == 0 else numero * factorial(numero-1)

print (f"factorial con if inline {factorial_inline(entero)}")