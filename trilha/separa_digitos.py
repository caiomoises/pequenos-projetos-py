num = int(input('Informe um número: '))
unidade = num % 10
por_cem = num % 100
dezena = int(por_cem/10)
por_mil = num % 1000
centena = int(por_mil/100)
milhar = int(num / 1000)

print(f'Analisando o número: {num}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')