F = 1 # Multiplicador de Espaços ---> MdE
i = 0 # Contador
C = 0 # Multiplicador de Espaços no Meio ---> MdEM
D = 0

#----------------------- Lendo o número ------------------------

X = int(input('Digite seu número: ')) # Largura do Diamante ---> LdD
while X < 6 or X > 32 or X % 2 != 0:
    print(f'    O número {X} é inválido')
    X = int(input('    Digite um número válido: '))

#-------------------------- Algoritmo --------------------------

S = int((X/2)-1)        # Multiplicador de Asteriscos ---> MdA
                        #   - Metade da largura do diamante menos 1
                    
D = (((X - 6)/2) + 5)   # Condição do contador principal
                        #   - LdD menos 6, divido por 2, mais 5
                        
while i < D: # Enquanto o Contador não atinge o valor da Condição

    if i == 1:          # Se for a segunda linha
        F = 0           # MdE recebe 0
        S = int(X / 2)  # MdA recebe metade da LdD
        
    elif i == 2:        # Se for a terceira linha
        F = 0           # MdE recebe 0
        C = X - 4       # MdEM recebe LdD menos 4
        
    elif i == D-1:      # Se for a última linha
        S = 1           # MdA recebe 1

#--------------------------- O Print -----------------------------------
        
    print((" " * F) + ("*" * S) + (" " * C) + ("*" * S) + (" " * F))

    #   Espaço vezes MdE
    #   Asterisco vezes MdA
    #   Espaço vezes MdEM
    #   Asterisco vezes MdA
    #   Espaço vezes MdE

#---------------------- Condições de Repetição -------------------------    
    S = 2           # MdA recebe 2 depois do primeiro laço já feito
    F += 1          # MdE recebe mais 1
    if C != 0:      # Se MdEM for diferente de 0
        C -= 2          # MdEM recebe menos 2
    i += 1          # Contador recebe mais 1 (Controle do laço)

print('\n\nFim do programa')
