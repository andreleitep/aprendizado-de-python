P = int(input("Digite o Primeiro termo da PG: "))
R = int(input("Digite a Razão da PG: "))
Q = int(input("Digite a quantidade de termos da PG: "))
soma = 0
cont = 0

while cont < Q:
    print("O Termo", cont+1, "da PG é:", P)
    soma = soma + P
    P = P * R
    cont = cont + 1

print("A soma dos", Q, "termos da PG é:", soma)
