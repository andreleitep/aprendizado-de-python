N=int(input("Escreva um número entre 1 e 50: "))
while N < 1 or N > 50:
    N=int(input("Escreva um número entre 1 e 50: "))
L=[]
i=0
while i<N:
    X = float(input("Escreva um número real: "))
    L.append(X)
    i+=1
i=0
while i<N:
    print(L[i])
    i+=1
