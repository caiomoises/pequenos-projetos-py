# implementando codigo para calculo de fatorial

def fat(n):
    fatorial = 1
    if n == 0:
        return fatorial == 0
    else:
        for index in range(1, n+1):
            fatorial *= index
        return fatorial
print(fat(4))