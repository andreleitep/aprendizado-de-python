# |-----------|
# | Cabeçalho |
# |-----------|

print ('Alex Moreira Roda')
print ('André Leite Pires')
print ('Questão 02\n\n')

# |-------------------|
# | Definindo objetos |
# |-------------------|

Inc = []
V = 0
Vt = 0
LI = 0
LF = 0
LM = 0
Test = True

# |-----------|
# | ALGORITMO |
# |-----------|

while Test:
    L = []
    L = input().split()

    Cd = int(L[0])
    CdL = str(Cd)
    Qt = int(L[1])
    Vl = float(L[2])
    
    if Cd == 0 and Qt == 0 and Vl == 0:
        Test = False
    else:
        if len(CdL) != 7:
            Inc.append (Cd)
        else:
            CdR = int(str(Cd)[:3])
            V = Qt * Vl
            if CdR <= 399:
                LI += V

            elif CdR <=799:
                LF += V

            else:
                LM += V
            Vt += V

print ('\nSubTotais')
print (f'   Linha Infantil = {LI:.2f}')
print (f'   Linha Feminina = {LF:.2f}')
print (f'   Linha Masculina = {LM:.2f}')
print (f'\nTotal Geral = {Vt:.2f}')
print ('\nInconsistencias')
if len(Inc) > 0:
    for i in Inc:
        print (f'   codigo invalido: {i}')
else:
    print ('   Nao ha inconsistencias')


print ('\n\nFim do programa')
