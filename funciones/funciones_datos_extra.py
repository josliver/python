def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, sos un {adjetivo}"

print(frase("Jony","Sliver","Crack"))
print(frase(adjetivo="Capo",nombre= "Jony",apellido="Sliver"))
# Error: print(frase({"nombre":"Jony", "Apellido":"Sliver","Adjetivo": "lindo"}))