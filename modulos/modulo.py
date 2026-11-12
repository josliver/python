# Importar modulo y asignar alias
# import modulo_saludar as m

# Importar solo la función
from modulo_saludar import saludar
# renombrando la función: from modulo_saludar import saludar as hello_word


saludo = saludar("Tom")

print(saludo)