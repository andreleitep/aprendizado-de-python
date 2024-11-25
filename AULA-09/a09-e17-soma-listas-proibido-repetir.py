from random import randint

# |--------------------|
# | Declarando métodos |
# |--------------------|

#Declaração de objetos

def CriarLista(arg2):
    arg1=[]
    i=0
    o=0
    tem=False
    primeiroFoi=False

#Quantidade de elementos

    while i<arg2: 
        X=randint(0, 100)
        while o < len(arg1) and not tem:
            if X == arg1[o] and primeiroFoi:
                tem=True
                print(X)
                print('Esse número já foi adicionado à lista.')
            o+=1
        if o == len(arg1) and not tem and primeiroFoi:
            arg1.append(X)
            print(X)
            i+=1
        if not primeiroFoi:
            arg1.append(X)
            primeiroFoi=True
            print(X)
            i+=1
        o=0
        tem=False
    print(f'A lista tem os seguintes elementos: \n{arg1}')
    return arg1


# |--------------------|
# | Declarando objetos |
# |--------------------|

A=[]
B=[]
R=[]

# |-----------------|
# | Desenvolvimento |
# |-----------------|

nA=int(input('Quantidade de elementos da lista A: '))
A = CriarLista(nA)
nB=int(input('Quantidade de elementos da lista B: '))
B = CriarLista(nB)
print(f'Lista A: {A}\nLista B: {B}')
for i in range(len(A)):
    R.append(A[i])
for i in range(len(B)):
    R.append(B[i])
print(f'\nLista R: {R}')
print('\n\nFim do programa')
