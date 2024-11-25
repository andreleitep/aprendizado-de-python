# Aula 10 - Conceito de Lista - classe list do Python
# Exercício 10 do PDF da Aula 9
from random import randint

def ExibeLista(lista):
    print('\nElementos da lista')
    print(' ' * 6, end='')
    for a in range(10):
        print(f'{a:5}', end='')
    print('\n', '-' * 56, end='', sep='')
    i = 0
    while i < len(lista):
        if i % 10 == 0:
            print(f'\n{i:4}: ', end='')
        print(f'{Dados[i]:5}', end='')
        i += 1
    print(f'\na lista tem {len(lista)} elementos')


# Aqui começa o programa principal
# 1ª Parte - Geração da lista
Dados = []
N = int(input('Digite N: '))
for i in range(N):
    valor = randint(0, 20)
    Dados.append(valor)
ExibeLista(Dados)

# 2ª Parte - Lê e remove X de Dados, caso exista
X = int(input('\n\nDigite X: '))
while X >= 0:
    # Algoritmo de Busca Sequencial usado em substituição ao operador in -> if X in Dados:
    print(f'Eliminação de {X} da lista')
    i = 0
    while i < N:
        if Dados[i] == X:
            del(Dados[i])
            N -= 1
        else:
            i += 1
    ExibeLista(Dados)

    X = int(input('\nDigite X: '))



print('\n\nFim do Programa')









