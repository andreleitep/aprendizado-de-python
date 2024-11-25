Q = int(input())
i = 0
Lsoma = []

while i < Q:
    entrada = input()
    L = [int(n) for n in entrada.split()]
    i2 = 0
    soma = 0
    if L[0] < L[1]:
        i2 = L[0]
        while i2 < L[1]:
            i2+=1
            if i2 % 2 != 0 and i2 != L[1]:
                soma = soma + i2
    elif L[1] < L[0]:
        i2 = L[1]
        while i2 < L[0]:
            i2+=1
            if i2 % 2 != 0 and i2 != L[0]:
                soma = soma + i2
    elif L[0] == L[1]:
        soma = 0
    
    Lsoma.append(soma)
    i+=1


i = 0
while i < Q:
    print(Lsoma[i])
    i+=1
