#Grupo formado por André Leite, Felipe Malbet, Giovanna Rosa, João Victor Bispo

print('Grupo formado por:\n\nAndré Leite\nFelipe Malbet\nGiovanna Rosa\nJoão Victor Bispo\n')

def abrirArquivo(arquivo):
    try:
        with open(arquivo, "r") as texto:
            linhas = texto.readlines()
        return linhas
    except FileNotFoundError:
        print('Arquivo não encontrado. Verifique o nome e tente novamente.')
        exit()

# Entrada do usuário para o nome do arquivo
nome_arquivo = input("Escreva o nome do arquivo: ")
listaLinhas = abrirArquivo(nome_arquivo)
laco = int(listaLinhas[0].rstrip())
i = 1
lidosE = []
lidosD = []
chinelos = []
chinelosRepetidos = {}
repeticoes = 1

# Algoritmo
if laco < 1 or laco > 2000:
    print('O número de pares deve estar entre 1 e 2000')
else:
    while i <= laco:
        chinelos = listaLinhas[i].rstrip().split()
        chinE = f'{int(chinelos[0])} E'
        nModE = int(chinelos[0])
        chinD = f'{int(chinelos[1])} D'
        nModD = int(chinelos[1])

        if nModE == nModD:
            print("Os valores para o lado esquerdo e direito não podem ser iguais.")
        
        else:
            if chinE in lidosE:
                if chinE in chinelosRepetidos:
                    chinelosRepetidos[chinE]["repetido"] += 1
                else:
                    chinelosRepetidos[chinE] = {
                        "modelo": nModE,
                        "pe": "E",
                        "repetido": 1
                    }
            else:
                lidosE.append(chinE)

            if chinD in lidosD:
                if chinD in chinelosRepetidos:
                    chinelosRepetidos[chinD]["repetido"] += 1
                else:
                    chinelosRepetidos[chinD] = {
                        "modelo": nModD,
                        "pe": "D",
                        "repetido": 1
                    }
            else:
                lidosD.append(chinD)
        
        i += 1

    chinelosOrdenados = dict(sorted(chinelosRepetidos.items(), key=lambda x: x[1]["modelo"]))

    # Exibindo os chinelos que ainda não foram lidos
    for key, value in chinelosOrdenados.items():
        print(f'{value["modelo"]} {value["pe"]} {value["repetido"]}')

    if len(chinelosRepetidos) == 0:
        print('\nSEM TROCAS DESTA VEZ')

    print()

    saida = input('Digite o nome do arquivo: ')
    with open(saida, 'w') as saidaArq:
        for key, value in chinelosOrdenados.items():
            saidaArq.write(f'{value["modelo"]} {value["pe"]} {value["repetido"]}\n')
        if len(chinelosRepetidos) == 0:
            saidaArq.write('SEM TROCAS DESTA VEZ')
            
    print(f'\nResultado salvo no arquivo "{saida}"')
