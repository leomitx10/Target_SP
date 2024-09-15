def is_fibonacci(num):
    if num < 0:
        return False

    a, b = 0, 1
    if num == a or num == b:
        return True

    fib = a + b
    while fib <= num:
        if fib == num:
            return True
        a, b = b, fib
        fib = a + b

    return False


n = int(input("Digite um numero: "))
if is_fibonacci(n):
    print(f"{n} Pertence a sequencia de Fibonacci.")
else:
    print(f"{n} Nao pertence a sequencia de Fibonacci.")




