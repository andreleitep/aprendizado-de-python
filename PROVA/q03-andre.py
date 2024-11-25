# |-----------|
# | Cabeçalho |
# |-----------|

print("André Leite Pires")
print("Questão 3")
print()

# |-------------------|
# | Definindo objetos |
# |-------------------|

A = '*' # Asterisco
S = ' ' # Espaço
i = 0   # Contador

# Largura do Diamante ---> LdD
N = int(input('Escreva um número par maior ou igual a 2 (ou 0 para terminar): '))
while N != 0 and (N % 2 != 0 or N < 2):
    N = int(input('Escreva um número par maior ou igual a 2 (ou 0 para terminar): '))

L = int(N/2) # Metade da LdD
    
# |-----------|
# | ALGORITMO |
# |-----------|

while N != 0:               # Laço principal
    print()
    print(f' {A*(N-2)}')        # Primeira linha 
    print(f'{A*N}')             # Segunda linha
    
    while i < L-1:              # Laço de escrita das demais linhas

#-------------------------- Demais linhas -------------------------------
        
        print(f'{S*i}{A*2}{S*(L-i-2)}{S*(L-i-2)}{A*2}')

        # Espaço vezes contador
        # Asterisco vezes 2
        # Espaço vezes metade da LdD menos contador menos 2
        # Espaço vezes metade da LdD menos contador menos 2
        # Asterisco vezes 2

#------------------------------------------------------------------------
        
        i+=1
        
    print(f'{S*(L-1)}{A*2}')    # Última linha
    print()

    # |--- Retorno ---|
    
    N = int(input('Escreva um número par maior ou igual a 2 (ou 0 para terminar): '))
    while N != 0 and (N % 2 != 0 or N < 2):   # Aqui o laço precisa
                                                        # respeitar primeiro
                                                        # o N != 0, depois
                                                        # as outras condições
        N = int(input('Escreva um número par maior ou igual a 2 (ou 0 para terminar): '))
    L = int(N/2)
    i=0

print('\n\nFim do programa')
