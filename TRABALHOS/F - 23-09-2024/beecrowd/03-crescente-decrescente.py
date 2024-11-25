entrada = input()
L = [int(n) for n in entrada.split()]

while L[0] != L[1]:
    if L[0] > L[1]:
        print('Decrescente')
    elif L[0] < L[1]:
        print('Crescente')
    entrada = input()
    L = [int(n) for n in entrada.split()]
