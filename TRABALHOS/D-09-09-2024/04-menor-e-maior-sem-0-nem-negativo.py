Q = int(input("Escreva a quantidade de números que quer comparar: "))

PrimeiroJaFoi = False
i = 0
while i < Q:
    N = int(input('Escreva um número: '))
    if N > 0:
        if not PrimeiroJaFoi:
            NMin = N
            NMax = N
            PrimeiroJaFoi = True
        if N > NMax:
            NMax = N
        if N < NMin:
            NMin = N
    else:
        print('Número inválido ignorado.')
    i += 1

print(f'\nO menor número digitado foi {NMin}\nO maior número digitado foi {NMax}')
print(f'\n\nFim do programa')
