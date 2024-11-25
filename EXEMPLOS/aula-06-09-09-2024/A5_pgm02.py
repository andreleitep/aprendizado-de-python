# Solução do exercício 2 do PDF da Aula 5
# O programa pede para exibir os divisíveis por 5 que estão ENTRE o
# o mínimo e o máximo, mas não deixa claro se os próprios valores
# limite estão ou não incluídos.
#
# Neste exercício essa ambiguidade é proposital.
# Vamos solucioná-la estabelecendo que os limites estão incluídos, ou
# seja, vamos considerar [LMin, LMax] um conjunto fechado.

LMin = int(input('Digite o mínimo: '))
LMax = int(input('Digite o máximo: '))
if LMax <= LMin:
    print(f'Os valores LMax = {LMax} e LMin = {LMin} são inválidos')
else:
    a = LMin
    while a <= LMax:
        if a % 5 == 0:
            print(a)
        a += 1

print('\n\nFim do Programa')
