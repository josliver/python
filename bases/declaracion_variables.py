# las variables son case sensitive
a = 5
b = 6
c = a + b
c += 10
print(c)

#Camel Case definido por la primera letra de cada palabra en mayuscula
myVariableName = "Hola"

#Snake Case definido por guiones bajos, sugerido por pyhton
my_variable_name = "Hola"



nombre = "Juan"
welcome = "Hola " + nombre + " ¿como estas?"
print(welcome)

#fstrings -> todo lo convierte a texto
welcome_fstring = f"Hola {nombre} ¿como estas?"
print(welcome_fstring)

#Puede ser in / not in
print ("ola" in welcome_fstring)

#Borra variables
del a