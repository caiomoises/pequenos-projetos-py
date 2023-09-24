# implementando codigo da sequencia de fibonacci

def fibonacci(n):
    a = 0
    b = 1
    print(b)
    for i in range(n):
        c = a + b
        a = b
        b = c
        print(c)
    
fibonacci(10)