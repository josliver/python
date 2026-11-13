import re

texto = "Hola bicho, este es mi número +5693459958"

#pattern = r"(\+56)+[2,9]+\d{7}"
pattern = r"(\+\d{2})*[29]+\d{7}"

reemplazo = re.sub(pattern,"(oculto)",texto)

print(reemplazo)