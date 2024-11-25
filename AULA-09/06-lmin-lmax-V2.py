LMin = int(input("LMin: "))
LMax = int(input("LMax: "))

#if LMin > LMax:
#    LMin, LMax = LMax, LMin

if LMin > LMax:
    Temp=LMin
    LMin=LMax
    LMax=Temp
    print("Atenção, o LMin estava maior que o LMax, os valores foram trocados.")
i=0
A=[]

'''
while i<10:
    X=int(input("Elemento: "))
    if X<=LMax and X>=LMin:
        A.append(X)
    else:
        print("Valor ignorado.")
    i+=1
'''

for i in range(10):
    X=int(input("Elemento: "))
    if X<=LMax and X>=LMin:
        A.append(X)
    else:
        print("Valor ignorado.")

print(f'A lista "A" tem {len(A)} elementos:\n{A}')
