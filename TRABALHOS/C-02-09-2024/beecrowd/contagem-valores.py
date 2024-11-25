i = 0
par = 0
impar = 0
positivo = 0
negativo = 0

while i < 5:
    N = int(input())
    if N % 2 == 0:
        par += 1
    else:
        impar += 1
    if N != 0:
        if N > 0:
            positivo += 1
        else:
            negativo += 1
    i += 1
        
print(f'{par} valor(es) par(es)\n{impar} valor(e)s impar(es)\n{positivo} valores positivos\n{negativo} valores negativos')
