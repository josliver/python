#creando un conjunto con set
conjunto = set(["dato1", "dato2", "dato3"])
print(conjunto)

#conjunto.add({"dato4","dato5"})

conjunto1 = frozenset({"dato1", "dato2", "dato3"})
conjunto2 = {"dato4", conjunto1}

print(conjunto2)

#teoria de conjuntos
conjuntoA = {1, 2, 3, 5, 7}
conjuntoB = {1, 3, 7}

print(conjuntoA.issubset(conjuntoB))
print(conjuntoB.issubset(conjuntoA))
# esto es lo mismo
print(conjuntoB <= conjuntoA)
print("----------------------")

print(conjuntoA.issuperset(conjuntoB))
print(conjuntoB.issuperset(conjuntoA))
# esto es lo mismo
print(conjuntoB >= conjuntoA)
print("----------------------")

#Verificando si al menos hay 1 elementos en comun
print(not conjuntoA.isdisjoint(conjuntoB))
