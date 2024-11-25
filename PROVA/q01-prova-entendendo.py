# Declarações

LMin = 0        # Limite mínimo (situação inicial do controle de laço)
LMax = 0        # Limite máximo
X = 0           # Divisor (situação inicial do controle de laço)
T = True        # Condição inicial de controle do laço principal
Same = False    # Objeto de controle de repetições
Size = 0        # Objeto para o tamanho da Lista (para o contador)
F = False       # Objeto sem utilidade
L = []          # Lista principal
Cont = 0        # Contador 
Sum = 0         # Resultado da soma de todos os elementos da lista
NMin = 0        # Menor número da lista
NMax = 0        # Maior número da lista

# Algoritmo

#-------------------------------------------------------------------

# |-- Laço que garante que LMin não é menor nem igual a zero --|
#   Laço que usa LMin == 0 como controle
#   Repete a partir de um if que atribui 0 ao objeto LMin

while LMin == 0:
    LMin = int(input('Digite o LMin:    '))
    if LMin <= 0:
        print('Valor inválido, favor digitar novamente')
        LMin = 0

#-------------------------------------------------------------------

# |-- Laço que garante que LMin não é maior nem igual a LMax --|
#   Mesma lógica do laço anterior, só que agora o laço repete enquanto o
#   LMax for igual ao LMin, e ele recebe esse valor caso o LMin seja maior
#   ou igual ao LMax

LMax = LMin # (situação inicial do controle de laço)
while LMin == LMax:
    LMax = int(input('Digite o LMax:    '))
    if LMin >= LMax:
        print('Valor inválido, favor digitar novamente')
        LMax = LMin

#-------------------------------------------------------------------

# |-- Laço que garante que o divisor não é zero --|
#   Repete se o usuário colocar zero de entrada

while X == 0:
    X = int(input('Digite o X:    '))
    if X == 0:
        print('Valor inválido, favor digitar novamente')

#-------------------------------------------------------------------

# |-- Laço principal do programa --|
print()
while T:
    N = int(input('Digite um valor:    '))
    if LMin <= N and N <= LMax: # Se N estiver entre LMin e LMax, inclusive:
        if N % X == 0: # Se N for divisível pelo divisor X:
            Size = len(L)
            Same = False
            i = 0
            while i != Size: # laço contador até o tamanho da lista
                if N == L[i]: # confere se o N é igual a todos os itens da lista
                    Same = True
                i += 1
            if Same == False: # Se N não tiver N na lista
                L.append(N) # Adiciona o número N ao final da lista
                Cont += 1
                Sum += N # Soma o valor de N ao total
                if Cont == 1: # Se for o primeiro número da lista
                    NMin = N
                    NMax = N
                else:
                    if N < NMin: # Se for menor que o mínimo
                        NMin = N
                    else:
                        if N > NMax: # Se for maior que o máximo
                            NMax = N
    if N == 0:
        T = False # Controle do loop principal

print()
print(L)
if Cont == 0:
    print('Não foram digitados elementos válidos para a lista')
elif Cont == 1:
    print(f'Foi digitado {Cont} elemento válido e único')
    print(f'O maior e o menor número da lista foram {NMax}')
else:
    print(f'Foram digitados {Cont} elementos válidos e únicos')
    print(f'A soma dos elementos aceitos é {Sum}, e a média é {Sum/Cont}')
    print(f'O maior número da lista foi o {NMax}, e o menor foi o {NMin}')

print('\n\nFim do programa')
