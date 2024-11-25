# Funções - Conceito e usos de funções
# Escreva um programa que leia dois valores LMin e LMax (LMin < LMax) e
#   em seguida determine quais são os números primos existentes na faixa
#   de valores compreendida por [LMin, LMax].
# Exiba na tela esses primos, com uma formatação legal.
# Grave esses primos em um arquivo de saída, cujo nome deve ser lido no
#   programa. Cada valor em uma linha do arquivo.

def ObtemLimites():
    a = int(input('Digite o valor menor: '))
    b = int(input('Digite o valor maior: '))
    while a >= b:
        print('  valor inválido, digite novamente')
        b = int(input('Digite o valor maior: '))    
    return a, b

def DeterminaPrimos(ini, fim):
    lp = []
    for valor in range(ini, fim+1):
        if EPrimo(valor):
            lp.append(valor)
    return lp

def EPrimo(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        raiz = n ** 0.5
        cont = 3
        while cont <= raiz:
            if n % cont == 0:
                return False
            cont += 2
        return True

def ExibeLista(lista):
    print('\nElementos da lista')
    print(' ' * 6, end='')
    for a in range(10):
        print(f'{a:7}', end='')
    print('\n', '-' * 79, end='', sep='')
    i = 0
    while i < len(lista):
        if i % 10 == 0:
            print(f'\n{i:4}: ', end='')
        print(f'{lista[i]:7}', end='')
        i += 1
    print(f'\na lista tem {len(lista)} elementos')

def GravaArquivo(nomearq, lista):
    arq = open(nomearq, 'w')
    for valor in lista:
        arq.write(f'{valor}\n')
    arq.close()


# Parte principal do programa
LMin, LMax = ObtemLimites()
print(f'LMin = {LMin}')
print(f'LMax = {LMax}')
Primos = DeterminaPrimos(LMin, LMax)
ExibeLista(Primos)
nome = input('Digite o nome do arquivo: ')
GravaArquivo(nome, Primos)

print('\n\nFim do Programa')
