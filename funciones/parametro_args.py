def suma(a,b):
    print("suma simple")
    return a + b

def suma(lista):
    print("suma lista")
    return sum(lista)

#Utilizando args args[]
def suma_total(*argumentos):
    print(argumentos)
    return suma(argumentos)

#print(suma(1,2))
print(suma([5,3,9]))
print (suma_total(1,2,3,4,5))