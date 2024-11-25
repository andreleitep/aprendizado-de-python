# Solução do exercício 5 do PDF da Aula 5
X = int(input('Digite um inteiro: '))
while X != 0:
    if X % 2 == 0 and X % 3 == 0:
        print(f'  {X} é divisível por 2 e por 3')  
    X = int(input('Digite um inteiro: '))    

print('\n\nFim do Programa')
