import os

def conversor(valor, opcao):
    dolar_americano = valor/5.03
    dolar_canadense = valor/3.73
    euro = valor/5.32
    coroa_sueca = valor/0.46

    if opcao == 1:
        return dolar_americano
    if opcao == 2:
        return dolar_canadense
    if opcao == 3:
        return euro
    if opcao == 4:
        return coroa_sueca
    
if __name__ == '__main__':
    os.system('cls')
    while True:
        valor = float(input('\n\tConversor de moedas\nValor? R$'))
        opcao = int(input('\nID\tMoeda\n1 - Dolar americano\n2 - Dolar canadense\n3 - Euro\n4 - Coroa sueca\n5- Sair\nEscolha o ID para qual moeda deseja converter:'))

        if opcao == 1:
            os.system('cls')
            print('\nA cotação do Dolar americano está 5.03 real por dolar\n')
            result = conversor(valor, opcao)
            print(f'R${valor} em Dolar americano é {result}')
        if opcao == 2:
            os.system('cls')
            print('\nA cotação do Dolar canadense está 3.73 real por dolar\n')
            result = conversor(valor, opcao)
            print(f'R${valor} em Dolar canadense é {result}')
        if opcao == 3:
            os.system('cls')
            print('\nA cotação do Euro está 5.32 real por euro\n')
            result = conversor(valor, opcao)
            print(f'R${valor} em Euro é {result}')
        if opcao == 4:
            os.system('cls')
            print('\nA cotação da Coroa sueca está 0.46 real por coroa sueca\n')
            result = conversor(valor, opcao)
            print(f'R${valor} em Coroa sueca é {result}')
        if opcao == 5:
            os.system('cls')
            print('Obrigado por usar o conversor de moedas!')
            break