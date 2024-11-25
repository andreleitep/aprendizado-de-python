# Aula 9 - solução do exercício 5 do PDF da Aula 9 do site

A = []  # criar a lista vazia
N = int(input('Digite N: '))
while N < 1 or N > 50:
    print(f'  {N} inválido')
    N = int(input('Digite N: '))
    
for i in range(N):
    X = float(input(f'Digite o elemento {i+1} >> '))
    A.append(X)

print('Lista A')
print(A)

Neg = []
Pos = []
for valor in A:
    if valor >= 0:
        Pos.append(valor)
    else:
        Neg.append(valor)
        
print(f'\nLista Neg contém {len(Neg)}')
print(Neg)
print(f'\nLista Pos contém {len(Pos)}')
print(Pos)


print('\n\nFim do Programa')
