NMin = int(input('Escreva um número mínimo: '))
NMax = int(input('Escreva um número máximo: '))

if NMin < NMax:
    cont = NMin
    print(f'Os números divisíveis por 5 entre {NMin} e {NMax} são:')
    while cont <= NMax:
        if cont % 5 == 0:
            print(cont)
        cont += 1
else:
    print("Erro: O número mínimo deve ser menor que o número máximo.")
