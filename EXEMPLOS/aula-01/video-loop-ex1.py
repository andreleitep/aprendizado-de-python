n = int(input("Digite o valor que você quer somar: "))
cont = 1
soma = 0
while cont <= n:
    soma = soma + cont
    cont = cont + 1
    print(soma, " + ", cont)

print("Valor final: ", soma)
