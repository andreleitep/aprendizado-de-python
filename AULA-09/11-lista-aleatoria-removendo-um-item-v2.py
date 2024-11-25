from random import randint

def MostrarLista(arg):
    print(' ' * 5, end='')
    for a in range(10):
        print(f'{a:7}', end='')
    print('\n', '-' * 77, end='', sep='')
    i=0
    while i < len(arg):
        if i % 10 == 0:
            print(f'\n{i:4}: |', end='')
        print(f'{arg[i]:5} |', end='')
        i+=1
    print('\n', '-' * 77, end='', sep='')
    print(f'\nNa lista tem {len(arg)} elementos')

N = int(input("Escreva o número de itens que você quer que tenha na lista: "))
L = []
i=0
while i < N:
    X = randint(0, 1000)
    L.append(X)
    i += 1
MostrarLista(L)

A = int(input('Insira um elemento que você queira remover da lista: '))
while A >= 0 and A <= 1000:
    i=0
    while i < len(L):
        if A == L[i]:
            del(L[i])
        else:
            i+=1
    A = int(input('Insira mais um elemento que você queira remover da lista: '))
MostrarLista(L)

print("\nFim do programa.")
