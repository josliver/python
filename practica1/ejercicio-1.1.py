#Promedios de duración de otros cursos
otros_cursos_min = 2.5
otros_cursos_max = 7.0
otros_cursos_promedio = 4.0
dalto_curso = 1.5

#duración de crudos
crudo_promedio = 5.0
crudo_dalto = 3.5

#diferencias de duración entre el curso de Dalto y otros cursos
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso / otros_cursos_max * 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calulo de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_vacio_dalto = 100 - dalto_curso / crudo_dalto * 100

print("El curso de Dalto dura un " + str(round(diferencia_con_min, 2)) + "% menos del curso más corto de otros cursos.")
print("El curso de Dalto dura un " + str(round(diferencia_con_max, 2)) + "% menos del curso más largo de otros cursos.")
print("El curso de Dalto dura un " + str(round(diferencia_con_promedio, 2)) + "% menos  del curso promedio de otros cursos.")
print("-------------------------------- --------------------------------")
print("El tiempo vacío removido en el curso promedio es del " + str(round(tiempo_vacio_promedio, 2)) + "%.")
print("El tiempo vacío removido en el curso de Dalto es del " + str(round(tiempo_vacio_dalto, 2)) + "%.")
print("-------------------------------- --------------------------------")
#mostrando diferencia si el curso dura 10 hrs
print(f"Ver 10hrs de Dalto equivale a {round(otros_cursos_promedio / dalto_curso * 10, 2)} hrs de otros cursos.")
print(f"Ver 10hrs de Otros cursos equivale a {round(dalto_curso / otros_cursos_promedio * 10, 2)} hrs de Dalto.")
print("-------------------------------- --------------------------------")