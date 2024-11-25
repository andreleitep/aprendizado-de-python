N = int(input('Digite um número: '))

while N != 0:
    if N % 2 == 0 and N % 3 == 0:
        print(f'    {N} é divisível por 2 e por 3.')
    N = int(input('Digite um número: '))


print(f'\n\nFim do programa')
