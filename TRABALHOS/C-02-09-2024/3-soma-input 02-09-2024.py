Q = int(input("Digite a quantidade de números reais que você quer somar: "))
cont = 0
soma = 0.0
N = 0.0

while cont < Q:
    N = float(input("Digite um número real: "))
    soma = soma + N
    cont = cont + 1

print("A soma dos", Q, "números que você digitou é: ", soma)

"""
Saiu esse resultado, por quê?
A soma dos 2 números que você digitou é:  3.3000000000000003
"""
