Q = int(input())

i = 0
L = []
M = []

while i < Q:
    Notas = input()
    L = Notas.split()

    N1 = float(L[0])
    N2 = float(L[1])
    N3 = float(L[2])

    M.append(float(((N1 * 2) + (N2 * 3) + (N3 * 5)) / 10))

    i+=1

i = 0
while i < Q:
    print(round(M[i],1))
    i+=1
