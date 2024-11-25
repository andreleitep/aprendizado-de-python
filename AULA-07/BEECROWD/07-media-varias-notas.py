L = [0,0]
X = 1
i = 0

while X == 1:
    N = float(input())
    if 0 <= N <= 10:
        L.insert(i, float(N))
        i+=1
    else:
        print("nota invalida")
    if i == 2:
        print(f'media = {(L[0] + L[1]) / 2:.2f}')
        i = 0
        print("novo calculo (1-sim 2-nao)")
        X = int(input())
        while X < 1 or X > 2:
            print("novo calculo (1-sim 2-nao)")
            X = int(input())

'''
while len(L) < 2:
    N = float(input())
    if 0 <= N <= 10:
        L.append(N)
    else:
        print("nota invalida")
'''
