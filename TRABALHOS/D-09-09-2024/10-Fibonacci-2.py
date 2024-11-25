N = int(input('Digite a quantidade de números de Fibonacci que você quer saber: '))
Prim = int(input('À partir de que número você quer começar a sequência: '))
i=0
a=0
b=1
termo = 0
PrimeiroJaFoi = False
SegundoJaFoi = False
if N > 0 and Prim >= 0:
    while i < N:
        if a >= Prim:
            print(a)
            i += 1
        temp = a
        a = b
        b = temp + b
        
else:
    print('\nErro: O número precisa ser maior que zero.')

print(f'\n\nFim do programa')
