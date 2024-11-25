# Aula 9 - Conceito de Lista - classe list do Python

L = [16, 5, 81, 44, 37, 24]
print('Objetos Lista em Python são da classe', type(L))

print('\nDados da lista L, exibidos em conjunto')
print(L)

print('\nDados da lista L, exibidos um a um com uso de índice e while')
i = 0
while i < len(L):
    print(L[i])
    i += 1

print('\nDados da lista L, exibidos um a um com uso do iterador for')
for valor in L:
    print(valor)

print('\nDados da lista L, exibidos um a um com uso do iterador for e índice')
for i in range(len(L)):
    print(L[i])

print('\nCaso em que queremos alterar os elementos da lista L')
print('Vamos multiplicar todos por 2')
for i in range(len(L)):
    L[i] *= 2            # é o mesmo que L[i] = L[i] * 2
    print(L[i])
print('lista completa =>', L)
print('\n\nFim do Programa')





