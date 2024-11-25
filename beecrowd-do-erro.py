X = int(input())
Y = int(input())
SOMA = 0

if X > Y:
    X, Y = Y, X
i = X+1

while i < Y:
    if i % 2 != 0:
        SOMA = SOMA + i
    i += 1

print(SOMA)
