# Solução do exercício 3 do PDF da Aula 5
N = int(input('Digite N: '))
i = 0
while i < N:
    valor = float(input('Digite um número real: '))
    if i == 0 or valor < guardaMenor:
        guardaMenor = valor
    if i == 0 or valor > guardaMaior:
        guardaMaior = valor
    i += 1

if N > 0:
    print(f'Menor valor = {guardaMenor}')
    print(f'Maior valor = {guardaMaior}')
else:
    print('Não foram fornecidos dados válidos')

print('\n\nFim do Programa')
