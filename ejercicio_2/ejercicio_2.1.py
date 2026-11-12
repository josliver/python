
def clase(cantidad_alumnos):
    alumnos = []
    for i in range(cantidad_alumnos):
        nombre = input("Nombre: ")
        edad   = int(input("Edad: "))
        alumno = (nombre, edad)
        alumnos.append(alumno)
    alumnos.sort(key=lambda n:n[1])
    return alumnos

def responsables(alumnos):
    asistente = alumnos[0][0]
    profesor  = alumnos[-1][0]
    return profesor,asistente

salon = clase(3)
profesor, asistente = responsables(salon)

print(salon)
print(f"El profe es {profesor} y su asistente {asistente}")