diccionario_no_formal = {
    "nombre": "Jony",
    "profesion": "Ing",
    "casado": True,
    "altura": 1.70
}  

diccionario_formal = dict(nombre="Jhon", profesion="Pilot", casado=True, altura=1.70)

#diccionario con tupla como clave
diccionario_tupla = {
    ("nombre", "apellido"): "Jony Dalto",
    ("profesion", "edad"): "Ing 30"
}

#diccionario solo con claves y valores nulos
diccionario_claves = dict.fromkeys(["nombre", "profesion", "casado", "altura"])