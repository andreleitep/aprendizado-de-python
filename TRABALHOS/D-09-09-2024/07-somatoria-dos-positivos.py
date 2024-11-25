N = int(input('Digite um número inteiro maior que zero: '))

cont = 0
soma = 0
PrimeiroJaFoi = False
i = 0
while N > 0:
    if not PrimeiroJaFoi:
        NMin = N
        NMax = N
        PrimeiroJaFoi = True
    soma = soma + N
    if N > NMax:
        NMax = N
    if N < NMin:
        NMin = N
    i += 1
    N = int(input('Digite um número inteiro maior que zero: '))

print(f'\nForam digitados {i} números inteiros maiores que zero\nA soma deles é {soma}\nO maior número digitado foi {NMax}\nO menor número digitado foi {NMin}')

print(f'\n\nFim do programa')
