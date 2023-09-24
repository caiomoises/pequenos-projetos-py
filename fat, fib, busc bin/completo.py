# implementando codigo para calculo de fatorial, sequencia de fibonacci e busca binaria
def fat(n):
    fatorial = 1
    if n == 0:
        return fatorial == 0
    else:
        for index in range(1, n+1):
            fatorial *= index
        return fatorial
def fibonacci(n):
    a = 0
    b = 1
    result = [a, b]
    for i in range(n):
        c = a + b
        a = b
        b = c
        result.append(c)
    return ', '.join(map(str, result))
      