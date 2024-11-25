# |-----------|
# | Cabeçalho |
# |-----------|

print("André Leite Pires")
print("Questão 2")

# |-------------------|
# | Definindo objetos |
# |-------------------|

infantil = 0
feminina = 0
masculina = 0

incon = []
entrada = input('Digite o código, a quantidade vendida e o valor unitário: ')
L = entrada.split()
C = int(L[0])
C = str(C)
Q = int(L[1])
V = float(L[2])

# |-----------|
# | ALGORITMO |
# |-----------|

while L != ['0', '0', '0']:
    if len(C) != 7:
        incon.append(C)
    else:
        CL = int(str(C)[:3])
        if CL >= 100 and CL < 400:
            infantil = infantil + V * Q
        elif CL >= 400 and CL < 800:
            feminina = feminina + V * Q
        elif CL >= 800 and CL < 1000:
            masculina = masculina + V * Q
        else:
            incon.append(C)
    entrada = input('Digite o código, a quantidade vendida e o valor unitário: ')
    L = entrada.split()
    C = int(L[0])
    C = str(C)
    Q = int(L[1])
    V = float(L[2])

print('\nSubTotais')
print(f'    Linha Infantil  = {infantil:.2f}')
print(f'    Linha Feminina  = {feminina:.2f}')
print(f'    Linha Masculina = {masculina:.2f}')
print(f'\nTotal Geral = {infantil + feminina + masculina:.2f}')
print('\nInconsistências')

if len(incon) > 0:
    for n in incon:
        print(f'    código inválido: {n}')
else:
    print('    Não há inconsistências')

print('\n\nFim do programa.')
