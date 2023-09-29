def aluguel(dias, km):
    preco_dias = dias * 60
    preco_km = km * 0.15
    preco_final = preco_dias + preco_km
    print(f'O total a ser pago é R${preco_final}')

if __name__ == '__main__':
    dias = int(input('Por quantos dias o carro foi alugado? '))
    km = float(input('Quantos km o carro rodou? '))
    aluguel(dias, km)