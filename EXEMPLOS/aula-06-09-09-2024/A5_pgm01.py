# Solução do exercício 1 do PDF da Aula 5
N = int(input('Digite um inteiro: '))
print('Exibição usando string formatado')
cont = 1
while cont <= 10:
    print('{} x {} = {}'.format(N, cont, N*cont))
    cont += 1

print('\nExibição usando f-string')
cont = 1
while cont <= 10:
    print(f'{N} x {cont} = {N*cont}')
    cont += 1

print('\n\nFim do Programa')
