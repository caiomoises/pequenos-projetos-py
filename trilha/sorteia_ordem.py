import random

primeiro_aluno = input('Nome do primeiro aluno: ')
segundo_aluno = input('Nome do segundo aluno: ')
terceiro_aluno = input('Nome do terceiro aluno: ')
quarto_aluno = input('Nome do quarto aluno: ')

lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
random.shuffle(lista)
print(lista)