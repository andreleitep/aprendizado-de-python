N = int(input('Digite a quantidade de números de Fibonacci que você quer saber: '))
i=0
a=0
b=1
termo = 0
if N > 0:
    if N == 1:
        print(a)
    elif N == 2:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        while i < N - 2:
            termo = b + a
            a = b
            b = termo
            print(termo)
            i+=1


else:
    print('Erro: O número precisa ser maior que zero.')

print(f'\n\nFim do programa')
