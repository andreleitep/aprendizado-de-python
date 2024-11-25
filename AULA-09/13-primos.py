i=0
o=2
L=[]
primo=True

N=int(input('Insira a quantidade de números primos que você deseja: '))

while len(L) < N:
    while o < i and i != 0 and o != 0 and primo:
        if i % o == 0:
            primo=False
        o+=1
    if o>=i or not primo:
        if i > 1 and primo:
            L.append(i)
        i+=1
    o=2
    primo=True

j=0
while j < len(L):
    if j % 10 == 0:
        print()
    print(f'{L[j]:7}', end='')
    j+=1
