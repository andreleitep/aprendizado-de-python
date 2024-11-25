#Grupo formado por André Leite, Felipe Malbet, Giovanna Rosa, João Victor Bispo
print('Grupo formado por:\n\nAndré Leite\nFelipe Malbet\nGiovanna Rosa\nJoão Victor Bispo\n')

import random
from random import randint

# |---------|
# | Funções |
# |---------|

def GeraSenha(tipo, tamanho):
    senha = ''
    for caractere in range(tamanho):
        if tipo == 'A': # Numérica
            senha += str(randint(0, 9))
        if tipo == 'B': # Alfabética
            senha += chr(random.choice(list(range(65, 90)) + list(range(97, 122))))
        if tipo == 'C': # Alfanumérica 1 (algarismos e letras maiúsculas)
            senha += chr(random.choice(list(range(48, 57)) + list(range(65, 90))))
        if tipo == 'D': # Alfanumérica 2 (algarismos e letras)
            senha += chr(random.choice(list(range(48, 57)) + list(range(65, 90)) + list(range(97, 122))))
        if tipo == 'E': # Geral (todos acima + [+, -, _ , !, ?, #, @, *, &, =, $, %])
            senha += chr(random.choice(list(range(48, 57)) + list(range(65, 90)) + list(range(97, 122)) + [33, 35, 36, 37, 38, 42, 43, 45, 61, 64, 95]))
    return senha
        
        


# |-----------|
# | Principal |
# |-----------|

tpTmn = input('Escreva o tipo de senha, entre A e E; e o número de caracteres por senha, entre 6 e 25 (separado por espaço): ')
tpTmnList = tpTmn.split()
tp = tpTmnList[0]
tmn = int(tpTmnList[1])
while (tmn < 6 or tmn > 25) or (tp != 'A' and tp != 'B' and tp != 'C' and tp != 'D' and tp != 'E'):
    print('Valores inválidos')
    tpTmn = input('Escreva o tipo de senha, entre A e E; e o número de caracteres por senha, entre 6 e 25 (separado por espaço): ')
    tpTmnList = tpTmn.split()
    tp = tpTmnList[0]
    tmn = int(tpTmnList[1])
    
Senha = GeraSenha(tp, tmn)
print(Senha)
