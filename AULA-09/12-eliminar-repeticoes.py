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
    print(f'\nA lista tem {len(arg)} elementos')

#Primeira parte - gerar a lista
N = int(input("Escreva o número de itens que você quer que tenha na lista: "))
L = []
i=0
while i < N:
    X = randint(0, 50)
    L.append(X)
    i += 1
MostrarLista(L)

#Segunda parte - conferir todos os itens com todos os itens
i=0
o=0
cortar = False
cortar = bool(input('Deseja cortar os números repetidos? '))
if cortar == True:
    while i < len(L):
        while o < len(L):
            if o != i:
                if L[i] == L[o]:
                    del(L[o])
                else:
                    o+=1
            else:
                o+=1
        o=0
        i+=1

MostrarLista(L)

print("\nFim do programa.")
