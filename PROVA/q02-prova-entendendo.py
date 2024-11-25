Inc = [] # Lista de incoerências
V = 0 # Valor do produto multiplicado pela quantidade vendida (Subtotal)
Vt = 0 # Valor total
LI = 0 # Subtotal Linha Infantil
LF = 0 # Subtotal Linha Feminina
LM = 0 # Subtotal Linha Masculina
Test = True # Controle de laço

while Test:
    L = [] # Zera a lista no começo do laço
    L = input().split() # input já com método split

    Cd = int(L[0]) # Código
    CdL = str(Cd) # Código em string
    Qt = int(L[1]) # Quantidade de itens vendidos
    Vl = float(L[2]) # Preço unitário

    if Cd == 0 and Qt == 0 and Vl == 0:
        Test = False # finaliza o programa se for digitado "0 0 0"
    else:
        if len(CdL) != 7:
            Inc.append(Cd) # adiciona o número digitado à lista de incoerências
        else:
            CdR = int(str(Cd)[:3]) # Três primeiros dígitos transformados em int
            V = Qt * Vl # Cálculo do produto de valor por quantidade
            if CdR <= 399:
                LI += V # Adição do valor na Linha Infantil
            elif CdR <= 799:
                LF += V # Adição do valor na Linha Feminina
            else:
                LM += V # Adição do valor na Linha Masculina
            Vt += V # Soma do valor ao Total Geral

print('\nSubtotais')
print(f'    Linha Infantil = {LI:.2f}')     #  _________
print(f'    Linha Feminina = {LF:.2f}')     # |         |
print(f'    Linha Masculina = {LM:.2f}')    # | Display |
print(f'\nTotal Geral = {Vt:.2f}')          # |_________|
print(f'Inconsistências')
if len(Inc) > 0:
    for i in Inc:
        print(f'    código inválido: {i}')
else:
    print('    Não há inconsistências')


print('\n\nFim do programa')
