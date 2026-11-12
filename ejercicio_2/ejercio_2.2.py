#Validar si un número es primo
def es_primo(num):
    if num == 0 or num == 1: return False
    if num == 2 : return True
    for i in (2,(num-1)):
        if num%i == 0: return False
    else:
        return True

def numeros_primos_en_rango(num):
    primos = []
    for i in range(2,num+1):
        #print(i)
        if es_primo(i):
            primos.append(i)
    return primos

#print (es_primo(4))
print (numeros_primos_en_rango(5))

primos_hasta = lambda num: list(filter(lambda x: all(x%i != 0 for i in range(2, int(x**0.5)+1)), range(2,num)))
print(primos_hasta(13))

test = 13
rango = range(2,test)
print(range(2,test))
print(list(filter(None, rango)))