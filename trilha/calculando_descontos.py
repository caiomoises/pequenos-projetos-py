def descontos(total, porcentagem):
    desconto = (total * porcentagem)/100
    print(f'\nO valor total da compra é {total}, com o desconto de {porcentagem}%, fica: R${total - desconto}')

if __name__ == '__main__':
    total = float(input('Qual o valor do produto? R$'))
    porcentagem = float(input('\nDe quanto será o desconto: '))

    descontos(total, porcentagem)