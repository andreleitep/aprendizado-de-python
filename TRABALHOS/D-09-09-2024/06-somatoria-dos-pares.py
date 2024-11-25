N = int(input('Digite um número maior ou igal a 100: '))

i = 1
soma = 0
if N >= 100:
    while i <= N:
        if i % 2 == 0:
            soma = soma + i
        i += 1
    print(f'A soma dos números pares entre 1 e {N} é {soma}')
else:
    print('O número deve ser maior que 100.')

print(f'\n\nFim do programa')
