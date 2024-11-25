# |-----------|
# | Cabeçalho |
# |-----------|

print ('Alex Moreira Roda')
print ('André Leite Pires')
print ('Questão 01\n\n')

# |-------------------|
# | Definindo objetos |
# |-------------------|

LMin = 0
LMax = 0
X = 0
T = True
Same = False
F = False
L = []
Cont = 0
Sum = 0
NMin = 0
NMax = 0

# |-----------|
# | ALGORITMO |
# |-----------|

while LMin == 0:
    LMin = int(input('Digite o LMin:   '))
    if LMin <= 0:
        print ('Valor invalido, favor digitar novamente')
        LMin = 0

LMax = LMin        
while LMin == LMax:
    LMax = int(input('Digite o LMax:   '))
    if LMin >= LMax:
        print ('Valor invalido, favor digitar novamente')
        LMax = LMin

while X == 0:
    X = int(input('Digite o X:   '))
    if X == 0:
        print ('Valor invalido, favor digitar novamente')

print ('')
while T :

    N = int(input('Digite um valor:   '))
    if LMin <= N and N <= LMax:
        if (N % X == 0):
            Size = len(L)
            Same = False
            i = 0
            while i != Size:                
                if N == L[i]:
                    Same = True
                i += 1
            if Same == False:
                L.append(N)
                Cont += 1
                Sum += N
                if Cont == 1:
                    NMin = N
                    NMax = N
                else:
                    if N < NMin:
                        NMin = N
                    else:
                        if N > NMax:
                            NMax = N
                
    if N == 0:
        T = False
print ('')
print (L)
if Cont == 0:
    print (f'Não foram digitados elementos válidos para a lista')   
elif Cont == 1:
    print (f'Foi digitado {Cont} elemento válido e único')
    print (f'O maior e o menor número da lista foi {NMax}')    
else:
    print (f'Foram digitados {Cont} elementos válidos e únicos')
    print (f'A soma dos elementos aceitos é {Sum}, e a média é {Sum/Cont}')
    print (f'O maior número da lista foi o {NMax}, e o menor foi o {NMin}')


print ('\n\nFim do programa')
