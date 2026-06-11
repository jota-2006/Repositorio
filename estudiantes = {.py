
for i in range(5):
    
    
    estudiante = input("ingrese un nombre: ")
    nota = float(input("ingrese nota del estudiante: "))





estudiantes = {
    
}

promedio = sum(estudiantes.values()) / len(estudiantes)

mejor_estudiante = ""

nota_mas_alta = -1.0

for estudiante in estudiantes:
    
    if estudiantes[estudiante] > nota_mas_alta:
        nota_mas_alta = estudiantes[estudiante]
        mejor_estudiante = estudiante
    
print(f"promedio del curso: {promedio} ")
print(f"estudiante destacado con mejor nota es = {mejor_estudiante} : {nota_mas_alta}")