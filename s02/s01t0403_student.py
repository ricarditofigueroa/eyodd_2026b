'''
NOTAS:
1: identifico el tamaño de la entrada "n"
el tamaño de la entrada es el numero
de estudiantes.
2: es ver cuanto crece el numero de
operaciones en mi algpritmo conforme
creece el tamaño
agrego las bigO identificadas
teniendo en cuenta la cota superior asimetrica
O(n) + 4*O(1) = O(n+4) = O(n)
'''

# creando una lista de estudoantes 
student_list_01 = ['Jordan', 'Pipen', 'curry', 'shack']
student_list_02 = ['mike', 'saul', 'walter', 'jessy']

# verificando presencia de un estudiante 
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student:
            print("Estudiante encontralo")
            return student
    # pero si no encuntro al estudiante 
    print("Estudiante no encontrado")
    return None

# probando algoritmo 
check_student("walter", student_list_02)        