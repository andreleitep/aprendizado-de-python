L=[]
primeiroFoi=False
i=0

x = int(input('Digite um número inteiro positivo: '))
while x > 0:
    if primeiroFoi:
        i=len(L)
        listado=False
        while i > 0 and not listado:
            if L[i-1] < x:
                L.insert(i, x)
                listado=True
            i-=1
        if not listado:
            L.insert(0, x)
    else:
        L.append(x)
        primeiroFoi=True
        
    x = int(input('Digite um número inteiro positivo: '))
    
print(L)
