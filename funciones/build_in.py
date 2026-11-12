numeros_aleatorios = [20, 1, 50, 45, 30, 10, 5, 15, 25, 35]

print("Números aleatorios:", numeros_aleatorios)
print("Números ordenados de menor a mayor:", sorted(numeros_aleatorios))
print("Números ordenados de mayor a menor:", sorted(numeros_aleatorios, reverse=True))

print("Números ordenados de menor a mayor (in-place):", numeros_aleatorios.sort())
print("El menor:", min(numeros_aleatorios))
print("El mayor:", max(numeros_aleatorios))

#bool(), all(), any(), chr(), ord(), divmod(), enumerate(), filter(), float(), format(), int(), len(), list(), map(), max(), min(), pow(), range(), 
#round(), set(), slice(), sorted(), str(), sum(), tuple()

print(sum(numeros_aleatorios))