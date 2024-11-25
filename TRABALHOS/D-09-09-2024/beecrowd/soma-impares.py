N1 = int(input())
N2 = int(input())

i = N1
soma = 0
if N1 < N2:
    while i < N2:
        if i % 2 != 0:
            soma = soma + i
        i += 1
if N1 >= N2:
    while i > N2:
        if i % 2 != 0:
            soma = soma + i
        i -= 1
            
    

print(soma)
