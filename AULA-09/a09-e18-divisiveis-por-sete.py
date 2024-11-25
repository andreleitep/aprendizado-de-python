Min = int(input('Digite Min: '))
Max = int(input('Digite Max: '))
L=[]

for i in range(Min+1, Max):
    if i % 7 == 0:
        L.append(i)

for i in range(len(L)):
    if i % 8 == 0:
        print()
    print(f'{L[i]:5}', end='')
