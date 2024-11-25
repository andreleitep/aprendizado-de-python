L1 = []
L2 = []

i = 0

while i < 10:
    L1.append(int(input("Escreva um número inteiro: ")))
    i+=1

i = 0
while i < 10:
    L2.append(int(input("Escreva um número inteiro para a segunda lista: ")))
    i+=1

O = L1 + L2
i = 0

while i < 20:
    print(O[i])
    i+=1
