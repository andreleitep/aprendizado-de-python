# Aula 9 - solução do exercício 6 do PDF da Aula 9 do site

LMin = int(input('Digite LMin: '))
LMax = int(input('Digite LMax: '))
if LMax < LMin:
    LMin, LMax = LMax, LMin
    print('LMin e LMax foram invertidos')

A = []
for i in range(10):
    X = int(input(f'digite valor entre {LMin} e {LMax} >> '))
    if LMin <= X and X <= LMax:
        A.append(X)
print(f'\nLista final contém {len(A)} elementos')
print(A)

print('\n\nFim do Programa')
