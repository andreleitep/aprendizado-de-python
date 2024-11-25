from random import randint
N = int(input("Escreva um número entre 1 e 50: "))
while N<1 or N>50:
    N = int(input("Escreva um número entre 1 e 50: "))
L=[]
i=0
while i<N:
    X = randint(0, 1000)
    L.append(X)
    i+=1
i=0
while i<N:
    print(L[i])
    i+=1

A = int(input("Consulte por um número entre 0 e 1000: "))
while A >= 0 and A <= 1000:
    if A in L:
        print(f"{A} está na lista!")
    else:
        print(f"{A} não está na lista...")
    A = int(input("Consulte por um número entre 0 e 1000: "))
print("Volte sempre!")
