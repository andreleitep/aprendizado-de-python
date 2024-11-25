# |---------|
# | Funções |
# |---------|

def abrirArquivo(arquivo):
    with open(arquivo, "r") as texto:
        linhas = texto.readlines()
    return linhas

def salvarArquivo(arquivo, dados):
    with open(arquivo, 'w') as f:
        for linha in dados:
            f.write(linha + '\n')

# |-----------|
# | Principal |
# |-----------|


nome_arquivo = input("Escreva o nome do arquivo de entrada: ")
arquivo_saida = 'saida_chinelos.txt'


listaLinhas = abrirArquivo(nome_arquivo)
laco = int(listaLinhas[0].rstrip())
i = 1
D = []
E = []
rep = []
lidos = []


while i <= laco:
    chins = listaLinhas[i].rstrip().split()
    chinE = str(f'{chins[0]} E')
    chinD = str(f'{chins[1]} D')

    if chinD in D:
        rep.append(chinD)
    else:
        D.append(chinD)

    if chinE in E:
        rep.append(chinE)
    else:
        E.append(chinE)

    i += 1


rep.sort()


resultado = []


for item in rep:
    if item not in lidos:
        resultado.append(f'{item} {rep.count(item)}')
        lidos.append(item)


if resultado:
    salvarArquivo(arquivo_saida, resultado)
else:
    salvarArquivo(arquivo_saida, ["SEM TROCAS DESTA VEZ"])

print(f"Saída gravada no arquivo: {arquivo_saida}")
