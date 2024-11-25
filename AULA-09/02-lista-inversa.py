i=0
L=[]
while i<10:
    X=input("Escreva um item para a lista: ")
    L.append(X)
    i+=1
while i>0:
    print(L[i-1])
    i-=1
