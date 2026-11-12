#funciones lambda o anonimas
multiplicar_por_dos = lambda x: x*2

print(multiplicar_por_dos(5))

# Ejemplo largo de filter sin lambda

def es_par(n):
    return True if n%2==0 else False

numeros = [10, 2, 5, 7,3,15, 18]

numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))

#Ahora lo mismo con lambda
numeros_pares_lambda = filter(lambda n: n%2==0, numeros)

print(list(numeros_pares_lambda))