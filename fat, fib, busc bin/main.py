from completo import *

if __name__ == '__main__':
    
    while True:
        print('1 - Verificar fatorial\n'
               '2 - Sequencia de fibonacci\n'
               '3 - Busca binaria\n'
               '4 - Sair\n\n')
        op = int(input('Escolha uma opção:'))
        if op == 1:
            x = int(input('Qual fatorial deseja calcular: '))
            print(f'O fatorial de {x} é {fat(x)}\n')
        if op == 2:
            x = int(input('Quantos valores da sequencia de fibonacci deseja ver: '))
            fibonacci(x-1)
            print(f'\n')
        if op == 3:
            ...
        if op == 4:
            print('Obrigado por usar este programa!')
            break