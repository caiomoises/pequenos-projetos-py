import random

primeiro_aluno = input('Nome do primeiro aluno: ')
segundo_aluno = input('Nome do segundo aluno: ')
terceiro_aluno = input('Nome do terceiro aluno: ')
quarto_aluno = input('Nome do quarto aluno: ')

lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]

numero_aleatorio = random.randint(0, 3)
print(lista_alunos[numero_aleatorio])