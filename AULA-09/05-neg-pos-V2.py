N = int(input("Insira um número inteiro entre 1 e 50: "))
while N<1 or N>50:
    N = int(input("Insira um número inteiro entre 1 e 50: "))
i=0
NEG=[]
POS=[]
'''
while i<N:
    X=float(input("Insira um número real: "))
    if X<0:
        NEG.append(X)
    else:
        POS.append(X)
    i+=1
'''
for n in range(N):
    X=float(input("Insira um número real: "))
    if X<0:
        NEG.append(X)
    else:
        POS.append(X)
    
print(f'A lista de números positivos inseridos tem {len(POS)} elementos:\n{POS}')
print(f'A lista de números negativos inseridos tem {len(NEG)} elementos:\n{NEG}')
