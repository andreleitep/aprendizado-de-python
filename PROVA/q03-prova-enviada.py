# |-----------|
# | Cabeçalho |
# |-----------|

print ('Alex Moreira Roda')
print ('André Leite Pires')
print ('Questão 03\n\n')

# |-------------------|
# | Definindo objetos |
# |-------------------|

F = 1
i = 0
C = 0
D = 0


# |-----------|
# | ALGORITMO |
# |-----------|

X = int(input('Digite seu número:  '))

while X < 6 or X > 32 or X % 2 != 0: 
    print (f'   O número {X} é inválido')
    X = int(input('   Digite um número válido:  '))

S = int((X/2)-1)
D = (((X - 6)/2) + 5)
while i < D:
    
    if i == 1:
        F = 0
        S = int(X/2)
    elif i == 2 :
        F = 0
        C = X - 4
    elif i == D-1:
        S = 1   
    print ((" " * F) + ("*" * S) + (" " * C) + ("*" * S) + (" " * F))
    S = 2
    F += 1
    if C != 0:
       C -= 2
    i += 1

print ('\n\nFim do programa')
