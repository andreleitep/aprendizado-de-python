# |-----------|
# | Cabeçalho |
# |-----------|

print("André Leite Pires")
print("Questão 1")
print()

# |-------------------|
# | Definindo objetos |
# |-------------------|

LMin = int(input('Determine o valor mínimo maior que zero: '))
while LMin < 1:
    LMin = int(input('Determine o valor mínimo MAIOR QUE ZERO: '))

LMax = int(input('Determine o valor máximo maior que o mínimo: '))
if LMax < LMin:
    LMin, LMax = LMax, LMin
    print('Os valores de LMin e LMax foram trocados.')

X = int(input('Determine o divisor: '))

L = []
listado = False
primeiroFoi = False
i = 0

Y = int(input('Digite um número diferente de zero (0): '))

Maior = 0
Menor = 0
Soma = 0
Media = 0

# |-----------|
# | ALGORITMO |
# |-----------|

while Y != 0:
    listado = False
    if Y <= LMax and Y >= LMin:
        if Y % X == 0:
            if primeiroFoi:
                i = len(L)
                while i > 0 and not listado:
                    if L[i-1] == Y:
                        listado = True
                        print(f'{Y} já está na lista.')
                    i -= 1
                if not listado:
                    L.append(Y)
                    if Y > Maior:
                        Maior = Y
                    if Y < Menor:
                        Menor = Y
                    Soma = Soma + Y
            else:
                L.append(Y)
                Maior = Y
                Menor = Y
                primeiroFoi = True
                Soma = Soma + Y
        else:
            print(f'{Y} não é divisível por {X}.')
    else:
        print(f'Número inválido, fora do intervalo {LMin} e {LMax}.')
    
    Y = int(input('Digite um número diferente de zero (0): '))
print('\nLista válida:')
print(L)
print(f'\nA lista possui {len(L)} elementos;')
print(f'A soma de todos os valores da lista é de {Soma};')
print(f'A média total dos valores da lista é de {Soma / len(L)};')
print(f'O Maior valor da lista é {Maior};')
print(f'O Menor valor da lista é {Menor}.')

print('\n\nFim do programa.')

