LMin = int(input('Insira um número inteiro mínimo: '))
LMax = int(input('Insira um número inteiro máximo: '))
i = 0
A = []

if LMin <= LMax:
    while i < 10:
        N = int(input(f'Insira um valor entre {LMin} e {LMax}: '))
        if LMin <= N <= LMax:
            A.append(N)
        else:
            print(f'Valor ignorado.')
        i += 1
elif LMin > LMax:
    while i < 10:
        N = int(input(f'Insira um valor entre {LMax} e {LMin}: '))
        if LMin >= N >= LMax:
            A.append(N)
        else:
            print(f'Valor ignorado.')
        i += 1

print(f'A lista possui os {len(A)} seguintes elementos: {A}')
