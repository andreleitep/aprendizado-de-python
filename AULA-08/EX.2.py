N = int(input("Digite um número diferente de 0: "))
L = []
i = 0
Q = 0

while N != 0:
    L.append(N)
    N = int(input("Digite um número diferente de 0 (ou 0 para finalizar): "))
    Q+=1

while i < Q:
    print(L[i])
    i+=1
