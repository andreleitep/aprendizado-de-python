N = int(input('Digite um número inteiro maior que zero: '))
i = 2

primo = True
while i < N and primo:
    if N % i == 0:
        primo = False
        print(f'{N} não é um número primo.')
    i+=1
if primo:
    print(f'{N} é um número primo.')

print(f'\n\nFim do programa')
