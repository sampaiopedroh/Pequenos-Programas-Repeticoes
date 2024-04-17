# Quais dos n primeiros números da sequência de fibo são primos:
qtd = int(input('Diga o tamanho da sequência a ser testada: '))
a = 1
b = 1
j = 0
k=2
print(a)
print(b)
while j < qtd:
    c = a + b

    a = b
    b = c
    i = 2
    num = c
    k += 1
    while True:

        if num % i == 0:
            break
        elif i >= num ** 0.5:
            print(f"{num} É primo: {j + 1}º primo e {k}º fibo")
            j += 1
            break
        i += 1