#cabeçalho
print("****************** FACULDADE CESUSC ******************\n"
      "*  CURSO: Análise e Desenvolvimento de Sistemas      *\n"
      "*  Disciplina: Lógica Computacional e Algoritmos     *\n"
      "*  Aluna: Ana Sofia Aguiar Azambuja                  *\n"
      "*  Professor: Roberto Fabiano Fernandes              *\n"
      "******************************************************")

#listas e a repetição
turma = []
while True:
    aluno = (input("Digite o nome do aluno:"))
    turma.append(aluno)
    faltas =int(input("Digite as faltas do aluno:"))
    turma.append(faltas)
    nota = int(input("Digite a nota do aluno:"))
    turma.append(nota)

    #condições usando as variáveis
    if nota >= 6 and faltas < 10:
        print("O aluno passa direto")
    if nota >= 6 and faltas > 10:
        print("O aluno está de recuperação por falta")
    if 4 < nota < 6 and faltas < 10:
        print("O aluno está de recuperação por nota")
    if nota < 4:
        print("O aluno repete direto")
    if 4 < nota < 6 and faltas > 10:
        print("O aluno repete por não obter nota e excesso de faltas")

    #continuar caso tenha outros alunos, e se não, o código para e mostra a lista da turma.
    continuar = input("Deseja continuar? [S/N]: ").upper()[0]
    if continuar == "N":
        break

print(turma)

#Lucas Aguiar me ajudou a fazer o break