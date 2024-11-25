# Solução do exercício 4 do PDF da Aula 5
N = int(input('Digite N: '))
PrimeiroJaFoi = False
i = 0
while i < N:
    valor = float(input('Digite um número real: '))
    if valor <= 0:
        print(f'  valor {valor} foi ignorado')
    else:
        if not PrimeiroJaFoi or valor < guardaMenor:
            guardaMenor = valor
        if not PrimeiroJaFoi or valor > guardaMaior:
            guardaMaior = valor
        PrimeiroJaFoi = True
    i += 1

if PrimeiroJaFoi:
    print(f'Menor valor = {guardaMenor}')
    print(f'Maior valor = {guardaMaior}')
else:
    print('Não foram fornecidos dados válidos')

print('\n\nFim do Programa')
