# Aula 10 - Conceito de Lista - classe list do Python
# Exercício 10 do PDF da Aula 9
from random import randint

# 1ª Parte - Geração da lista
Dados = []
N = int(input('Digite N: '))
for i in range(N):
    valor = randint(0, 1000)
    Dados.append(valor)
print('\nLista gerada')
print(' ' * 6, end='')
for a in range(10):
    print(f'{a:5}', end='')
i = 0
while i < len(Dados):
    if i % 10 == 0:
        print(f'\n{i:4}: ', end='')
    print(f'{Dados[i]:5}', end='')
    i += 1

# 2ª Parte - Lê e pesquisa se X está em Dados
X = int(input('\n\nDigite X: '))
while X >= 0:
    # Algoritmo de Busca Sequencial usado em substituição ao operador in -> if X in Dados:
    print(f'Verificando se {X} está na lista')
    Achou = False
    i = 0
    while i < N:
        if Dados[i] == X:
            Achou = True
            print(f'  encontrado na posição {i}')
        i += 1

    if not Achou:
        print(f'  não encontrado')
    X = int(input('\nDigite X: '))

print('\n\nFim do Programa')
