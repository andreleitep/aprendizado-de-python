Q = int(input("Escreva a quantidade de números que quer comparar: "))

PrimeiroJaFoi = False
i = 0
while i < Q:
    N = int(input('Escreva um número: '))
    if not PrimeiroJaFoi:
        NMin = N
        NMax = N
        PrimeiroJaFoi = True
    if N > NMax:
        NMax = N
    if N < NMin:
        NMin = N
    i += 1

print(f'O menor número digitado foi {NMin}\nO maior número digitado foi {NMax}')
