def Reajuste(salario_inicial, reajuste):
    acrescimo = (salario_inicial * reajuste) / 100
    salario_final = salario_inicial + acrescimo
    print(f'O funcionario ganhava {salario_inicial}, com o reajuste de {reajuste}% de aumento, passa a receber {salario_final:.2f}')

if __name__ == '__main__':
    salario = float(input('Qual o salario do funcionario: '))
    reajuste = int(input('De quanto será o reajuste salarial: '))
    Reajuste(salario, reajuste)