#sepa deu certo -gi
#Grupo formado por André Leite, Felipe Malbet, Giovanna Rosa, João Victor Bispo
print('Grupo formado por:\n\nAndré Leite\nFelipe Malbet\nGiovanna Rosa\nJoão Victor Bispo\n')

import random
from random import randint

# |---------|
# | Funções |
# |---------|

# Função de geração de senhas
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

#função abrir arquivo matrículas
def abrirArquivo(arquivo_entrada):
    linhas = []
    with open(arquivo_entrada, "r") as arq:
        for linha in arq:
            linhas.append(linha.rstrip())
    arq.close()
    return linhas

#função salvar senhas no arquivo
def salvararq(dados):
     try:
        with open(arquivo_saida, "w") as arq:
            for matricula, senha in dados.items():
                arq.write(f"{matricula};{senha};\n")
        print(f"Senhas salvas no arquivo {arquivo_saida}.")
     except Exception as e:
        print("Erro ao salvar o arquivo.")
        print("Detalhes do erro:", e)


# |-----------|
# | Principal |
# |-----------|

# Declarando variáveis
matriculas = []

# Nome do arquivo entrada fixo
arquivo_entrada = "MATR.TXT"

#Nome do arquivo saída fixo
arquivo_saida = "SENHAS.TXT"

#abre arquivo de matrículas
matriculas = abrirArquivo(arquivo_entrada)

# Dados de entrada
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


dados_senhas = {}
for matricula in matriculas:
    senha = GeraSenha(tp, tmn)
    dados_senhas[matricula] = senha

print(dados_senhas)

# salvar as matrículas e senhas no arquivo SENHAS.TXT
salvararq(dados_senhas)




# testar se o código do aluno tem 6 dígitos

