N = int(input("Escreva um número inteiro entre 0 e 50: "))
i = 0
POS = []
NEG = []

while N < 1 or N > 49:
    N = int(input("Escreva um número inteiro entre 0 e 50: "))

while i < N:
    A = float(input("Escreva um número real."))
    if A >= 0:
        POS.append(A)
    elif A < 0:
        NEG.append(A)
    
    i +=1

print(f'Os números positivos são: {POS}, o conjunto possui {len(POS)} elemento(s)')
print(f'Os números negativos são: {NEG}, o conjunto possui {len(NEG)} elemento(s)')
