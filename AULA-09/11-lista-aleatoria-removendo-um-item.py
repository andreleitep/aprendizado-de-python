from random import randint
N = int(input("Escreva o número de itens que você quer que tenha na lista: "))
L = []
POS = []
i = 0
o = 0
while i < N:
    X = randint(0, 1000)
    L.append(X)
    print(f'{i + 1}. {X}')
    i += 1

A = int(input("Escolha, localize e retire todas as ocorrências de um elemento da lista: "))
i = 0
cont = 0
while A >= 0 and A <= 1000:
    while i < len(L):
        if A == L[i]:
            POS.append(i+1)
            cont += 1
        i += 1
    for o in range(len(L)-1, -1, -1):
        if A == L[o]:
            del(L[o])
    if cont == 0:
        print(f'Não tem nenhum {A} na lista')
    else:
        print(f'Foram retiradas {cont} ocorrência(s) de {A} da lista, e estava(m) na(s) posição(ões) {POS}.')
    POS.clear()
    cont = 0
    o = 0
    i = 0
    A = int(input("Escolha, localize e retire todas as ocorrências de um elemento da lista: "))
while i < len(L):
    print(f'{i+1}. {L[i]}')
    i+=1
print("\nFim do programa.")
