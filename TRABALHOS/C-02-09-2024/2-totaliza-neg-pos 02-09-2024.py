N = 1
pos = 0
neg = 0

while N != 0:
    N = int(input("Digite um número inteiro positivo ou negativo: "))
    if N < 0:
        neg = neg + N
    else:
        pos = pos + N

print("A soma dos números negativos é:", neg)
print("A soma dos números positivos é:", pos)
