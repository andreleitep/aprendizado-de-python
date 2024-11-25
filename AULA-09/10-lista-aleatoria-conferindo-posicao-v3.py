from random import randint
N = int(input("Escreva um número: "))
L=[]
cont=0
for i in range(N):
    X = randint(0, 1000)
    L.append(X)
    print(f'{cont+1}. {X}')
    cont+=1
i=0
A = int(input("Consulte por um número entre 0 e 1000: "))
while A >= 0 and A <= 1000:
    Q = L.count(A)
    print(f"Tem {Q} ocorrência(s) de {A} na lista.")
    if Q > 0:
        print(f"Nas seguintes posições:")
        print(L.index(A))
        o = L.index(A)
        while i < Q:
            print(L[o+1:-1].index(A)+1)
            o = L[o+1:-1].index(A)
            i+=1
    i=0
    A = int(input("Consulte por um número entre 0 e 1000: "))
