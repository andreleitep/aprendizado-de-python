from random import randint

# |-------------------|
# | DEFININDO OBJETOS |
# |-------------------|

N=int(input("Insira um número inteiro maior que 10: "))
while N <=10:
    N=int(input("Insira um número inteiro maior que 10: "))
i=0
L=[]
x=0
mudou=False

# |-----------|
# | ALGORITMO |
# |-----------|

# Gerando lista
for o in range(N):
    L.append(randint(0, 20))
print(L)

# Ordenando lista (Método bolha)
while not mudou:
    mudou=True
    while i < len(L)-1:
        if L[i] > L[i+1]:
            x = L[i]
            del(L[i])
            L.insert(i+1, x)
            mudou = False
        i+=1
    i=0
print(L)
