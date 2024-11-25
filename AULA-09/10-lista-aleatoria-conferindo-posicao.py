from random import randint
N = int(input("Escreva o número de itens que você quer que tenha na lista: "))
L=[]
POS=[]
i=0
while i<N:
    X = randint(0, 1000)
    L.append(X)
    print(f"{i+1}. {X}")
    i += 1

A = int(input("Consulte por um número entre 0 e 1000: "))
i = 0
cont = 0
while A >= 0 and A <= 1000:
    while i < N:
        if A == L[i]:
            POS.append(i+1)
            cont += 1
        i+=1
    if cont == 0:
        print(f"Não tem nenhum {A} na lista.")
    else:
        print(f"Tem {cont} número(s) {A} na lista e está(ão) na(s) posição(ões) {POS}.")
    POS.clear()
    i = 0
    cont = 0
    A = int(input("Consulte por um número entre 0 e 1000: "))
print("\nFim do programa.")
