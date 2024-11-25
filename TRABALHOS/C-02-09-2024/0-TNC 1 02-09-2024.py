P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Q = int(input("Digite a quantidade de elementos: "))
cont = 0
soma = 0

while cont < Q:
    print("Termo", cont + 1, "da PA =", P)
    soma = soma + P
    P = P + R
    cont = cont + 1

print("Soma dos termos:", soma)
