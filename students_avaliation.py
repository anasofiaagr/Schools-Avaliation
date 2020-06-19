
#listas e a repetição
classtudent = []
while True:
    student = (input("Type the student's name:"))
    classtudent.append(student)
    absences =int(input("Type the student's absences:"))
    classtudent.append(absences)
    grade = int(input("Type the student's grade:"))
    classtudent.append(grade)

    #condições usando as variáveis
    if grade >= 6 and absences < 10:
        print("The student pass")
    if grade >= 6 and absences > 10:
        print("The student has failed due absence")
    if 4 < grade < 6 and absences < 10:
        print("The student has failed due to grades")
    if grade < 4:
        print("The student straightly repeats the year")
    if 4 < grade < 6 and absences > 10:
        print("The student repeats the year due to grades and absences")

    #continuar caso tenha outros alunos, e se não, o código para e mostra a lista da turma.
    continueprocess = input("Do you wish to continue? [Y/N]: ").upper()[0]
    if continueprocess == "N":
        break

print(classtudent)
