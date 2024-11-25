# Aula 10 - Conceito de Lista - classe list do Python
# Exercício 9 do PDF da Aula 9
#   solução a - na qual é permitido uso do operador in
from random import randint

# 1ª Parte - Geração da lista
Dados = []
N = int(input('Digite N: '))
for i in range(N):
    valor = randint(0, 1000)
    Dados.append(valor)
print(Dados)

# 2ª Parte - Lê e pesquisa se X está em Dados
X = int(input('Digite X: '))
while X >= 0:
    if X in Dados:
        print(f'  {X} está na lista')
    else:
        print(f'  {X} não está na lista')
    X = int(input('Digite X: '))

print('\n\nFim do Programa')
