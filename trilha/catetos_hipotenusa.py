import math

def calcula_hipotenusa(adjacente, oposto):
    hipotenusa = math.sqrt(adjacente**2 + oposto**2)
    print(f'A hipotenusa vai medir {hipotenusa:.2f}')

if __name__ == '__main__':
    adjacente = float(input('Comprimento do cateto adjacente: '))
    oposto = float(input('Comprimento do cateto oposto: '))
    calcula_hipotenusa(adjacente, oposto)