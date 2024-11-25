# Só falta fazer os arquivos de saída
    # Para isso, eu preciso transformar os casos do relatório de
    # divergências em listas para depois escrever no arquivo.

# |---------|
# | Funções |
# |---------|

# |-----------|
# | Principal |
# |-----------|

i = 0
linhaDict = {}
p = 0
v = 0

Q = int(input('Quantos casos de teste você quer executar? '))

try:
    while i < Q:
        print('\n')
        print(f'{i+1}º caso teste:\n')
        arqProdutos = open(f'c{i+1}_produtos.txt')
        linhaP = arqProdutos.readline().rstrip()
        while linhaP != '':
            listaLinhaP = linhaP.split(';')
            listaLinhaP[0] = int(listaLinhaP[0])
            listaLinhaP[1] = int(listaLinhaP[1])
            listaLinhaP[2] = int(listaLinhaP[2])
            if listaLinhaP[0] >= 10000 and listaLinhaP[0] <= 99999:
                linhaDict[listaLinhaP[0]] = {
                    'EstInicial' : listaLinhaP[1],
                    'QtMin' : listaLinhaP[2]
                    }
            else:
                print(f'Linha {p+1} - Código do produto inválido') # Relatório de divergências
            linhaP = arqProdutos.readline().rstrip()
            p += 1
        arqProdutos.close()
        
        arqVendas = open(f'c{i+1}_vendas.txt')
        linhaV = arqVendas.readline().rstrip()
        while linhaV != '':
            listaLinhaV = linhaV.split(';')
            listaLinhaV[0] = int(listaLinhaV[0])
            if listaLinhaV[2] == '135':
                print(f'Linha {v+1} - Venda cancelada')
                    # Relatório de divergências
            elif listaLinhaV[2] == '190':
                print(f'Linha {v+1} - Venda não finalizada')
                    # Relatório de divergências
            elif listaLinhaV[2] == '999':
                print(f'Linha {v+1} - Erro desconhecido. Acionar a equipe de TI.')
                    # Relatório de divergências
            else:
                if listaLinhaV[0] in linhaDict:
                    listaLinhaV[1] = int(listaLinhaV[1])
                    linhaDict[listaLinhaV[0]].update({
                        'QtVendas' : listaLinhaV[1],
                        'Status' : listaLinhaV[2],
                        'Canal' : listaLinhaV[3]
                        })
                else:
                    print(f'Linha {v+1} - Código de Produto não encontrado {listaLinhaV[0]}')
                        # Relatório de Divergências
            linhaV = arqVendas.readline().rstrip()
            v += 1
        arqVendas.close()

        # Necessidade de transferência Armazém para CO

        print('\nNecessidade de transferência Armazém para CO\n')
        print('Produto  EstInicial  QtMin  QtVendas  Estq.após  Necess.  Transf. de')
        print('                                         Vendas            Arm p/ CO')
        for li in linhaDict:
            print(f'{li:>7}', end='')
            print(f'{linhaDict[li]["EstInicial"]:>12}', end='')
            print(f'{linhaDict[li]["QtMin"]:>7}', end='')
            print(f'{linhaDict[li]["QtVendas"]:>10}', end='')
            print(f'{linhaDict[li]["EstInicial"]-linhaDict[li]["QtVendas"]:>11}', end='')
            QtMin = linhaDict[li]['QtMin']
            Resto = linhaDict[li]["EstInicial"]-linhaDict[li]["QtVendas"]
            if Resto < QtMin:
                necess = QtMin - Resto
            else:
                necess = 0
            print(f'{necess:>9}', end='')
            if necess < 10 and necess != 0:
                necess = 10
                print(f'{necess:>12}', end='')
            else:
                print(f'{necess:>12}', end='')
            print()

        # Totais por Canal de Vendas

        Representantes = 0
        Website = 0
        Android = 0
        iPhone = 0
        for li in linhaDict:
            if linhaDict[li]['Canal'] == '1':
                Representantes += linhaDict[li]['QtVendas']
            elif linhaDict[li]['Canal'] == '2':
                Website += linhaDict[li]['QtVendas']
            elif linhaDict[li]['Canal'] == '3':
                Android += linhaDict[li]['QtVendas']
            elif linhaDict[li]['Canal'] == '4':
                iPhone += linhaDict[li]['QtVendas']
        
        print('\nQuantidade de Vendas por canal\n')
        print('Canal                 QtVendas')
        print(f'1 - Representantes', f'{Representantes:>11}')
        print(f'2 - Website', f'{Website:>18}')
        print(f'3 - App móvel Android', f'{Android:>8}')
        print(f'4 - App móvel iPhone', f'{iPhone:>9}')
        print('\n')
        print('-'*68)
        
        i += 1
except FileNotFoundError:
    print(f'Arquivo pertencente ao {i+1}º caso teste não encontrado.')
    print('Os arquivos de testes devem ser nomeado da seguinte maneira:')
    print('\nc#_produtos.txt')
    print('c#_vendas.txt\n')
    print('substituindo o "#" pelo número do caso teste que se deseja fazer.\n\n')


for n in range(i):
    print(f'Saídas do {n+1}º caso gravadas nos arquivos:')
    print(f'    c{n+1}_TRANSFERE.TXT')
    print(f'    c{n+1}_DIVERGENCIAS.TXT')
    print(f'    c{n+1}_TOTCANAL.TXT')
    print()

print('/nFim do programa.')
