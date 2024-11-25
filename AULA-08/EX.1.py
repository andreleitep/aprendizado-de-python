N = int(input("Digite um número diferente de 0: "))
L = []

while N != 0:
    L.append(N)
    N = int(input("Digite um número diferente de 0 (ou 0 para finalizar): "))

print(L)
