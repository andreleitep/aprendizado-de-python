Q = int(input("Digite a quantidade de números reais que você gostaria de somar: "))
cont = 0
N = 0.0
soma = 0.0

while cont < Q:
    N = float(input("Digite o número que gostaria de somar: "))
    if N >= 0.0:
        soma = soma + N
    cont = cont + 1

print("Desprezando os valores negativos, o resultado da soma dos números que você digitou é:", soma)
