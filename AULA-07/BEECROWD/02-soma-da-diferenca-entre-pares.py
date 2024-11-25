entrada = input()
L = [int(n) for n in entrada.split()]
i = 0
soma = 0

while L[0] > 0 and L[1] > 0:
    if L[0] < L[1]:
        i = L[0]
        while i <= L[1]:
            soma = soma + i
            print(i, end=" ")
            i+=1
        print(f"Sum={soma}")
    elif L[1] < L[0]:
        i = L[1]
        while i <= L[0]:
            soma = soma + i
            print(i, end=" ")
            i+=1
        print(f"Sum={soma}")
    elif L[0] == L[1]:
        print(L[0], L[1], f"Sum={L[0] + L[1]}")
    entrada = input()
    L = [int(n) for n in entrada.split()]
    soma = 0
