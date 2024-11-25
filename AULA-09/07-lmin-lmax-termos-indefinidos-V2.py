LMin = int(input('Insira um número inteiro mínimo: '))
LMax = int(input('Insira um número inteiro máximo: '))
Q = int(input('Insira o número de elementos que você quer comparar: '))
i = 0
A = []

if LMin >= LMax:
    Temp = LMin
    LMin = LMax
    LMax = Temp
    
for i in range(Q):
    N = int(input(f'Insira um valor entre {LMin} e {LMax}: '))
    if LMin <= N <= LMax:
        A.append(N)
    else:
            print(f'Valor ignorado.')

print(f'A lista possui os {len(A)} seguintes elementos: {A}')
