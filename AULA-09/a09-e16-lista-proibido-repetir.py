#Declaração de objetos

L=[]
i=0
o=0
tem=False
primeiroFoi=False

#Quantidade de elementos

N=int(input('Digite o número de elementos da lista: '))
while i<N: 
    X=int(input('Adicione um elemento à lista: '))
    while o < len(L) and not tem:
        if X == L[o] and primeiroFoi:
            tem=True
            print('Esse número já foi adicionado à lista.')
        o+=1
    if o == len(L) and not tem and primeiroFoi:
        L.append(X)
        i+=1
    if not primeiroFoi:
        L.append(X)
        primeiroFoi=True
        i+=1
    o=0
    tem=False
print(f'A lista L tem os seguintes elementos: \n{L}')
