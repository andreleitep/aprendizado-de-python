# |-----------|
# | Principal |
# |-----------|

i = 0
linhaDict = {}
p = 0
v = 0
lista = []

Q = int(input('Quantos casos de teste você quer executar? '))

try:
    while i < Q:
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
                lista.append(f'Linha {p+1} - Código do produto inválido') # Relatório de divergências
            linhaP = arqProdutos.readline().rstrip()
            p += 1
        arqProdutos.close()
        
        arqVendas = open(f'c{i+1}_vendas.txt')
        linhaV = arqVendas.readline().rstrip()
        while linhaV != '':
            listaLinhaV = linhaV.split(';')
            listaLinhaV[0] = int(listaLinhaV[0])
            if listaLinhaV[2] == '135':
                lista.append(f'Linha {v+1} - Venda cancelada')
                    # Relatório de divergências
            elif listaLinhaV[2] == '190':
                lista.append(f'Linha {v+1} - Venda não finalizada')
                    # Relatório de divergências
            elif listaLinhaV[2] == '999':
                lista.append(f'Linha {v+1} - Erro desconhecido. Acionar a equipe de TI.')
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
                    lista.append(f'Linha {v+1} - Código de Produto não encontrado {listaLinhaV[0]}')
                        # Relatório de Divergências
            linhaV = arqVendas.readline().rstrip()
            v += 1
        arqVendas.close()

        # Necessidade de transferência Armazém para CO

        saida2 = open(f'c{i+1}_TRANSFERE.TXT', 'w')
        
        saida2.write('Necessidade de transferência Armazém para CO\n\n')
        saida2.write('Produto  EstInicial  QtMin  QtVendas  Estq.após  Necess.  Transf. de\n')
        saida2.write('                                         Vendas            Arm p/ CO\n')
        for li in linhaDict:
            saida2.write(f'{li:>7}')
            saida2.write(f'{linhaDict[li]["EstInicial"]:>12}')
            saida2.write(f'{linhaDict[li]["QtMin"]:>7}')
            saida2.write(f'{linhaDict[li]["QtVendas"]:>10}')
            saida2.write(f'{linhaDict[li]["EstInicial"]-linhaDict[li]["QtVendas"]:>11}')
            QtMin = linhaDict[li]['QtMin']
            Resto = linhaDict[li]["EstInicial"]-linhaDict[li]["QtVendas"]
            if Resto < QtMin:
                necess = QtMin - Resto
            else:
                necess = 0
            saida2.write(f'{necess:>9}')
            if necess < 10 and necess != 0:
                necess = 10
                saida2.write(f'{necess:>12}\n')
            else:
                saida2.write(f'{necess:>12}\n')
        saida2.close()
            
        # Totais por Canal de Vendas

        saida1 = open(f'c{i+1}_TOTCANAL.TXT', 'w')

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
        
        saida1.write('Quantidade de Vendas por canal\n\n')
        saida1.write('Canal                 QtVendas\n')
        saida1.write(f'1 - Representantes {Representantes:>11}\n')
        saida1.write(f'2 - Website {Website:>18}\n')
        saida1.write(f'3 - App móvel Android {Android:>8}\n')
        saida1.write(f'4 - App móvel iPhone {iPhone:>9}\n')

        saida1.close()

        # Relatório de Divergências

        saida3 = open(f'c{i+1}_DIVERGENCIAS.TXT', 'w')

        saida3.write('Relatório de Divergências\n\n')
        for ot in lista:
            saida3.write(f'{ot}\n')

        saida3.close()

        i += 1
        
except FileNotFoundError:
    print(f'Arquivo pertencente ao {i+1}º caso teste não encontrado.')
    print('Os arquivos de testes devem ser nomeado da seguinte maneira:')
    print('\nc#_produtos.txt')
    print('c#_vendas.txt\n')
    print('substituindo o "#" pelo número do caso teste que se deseja fazer.\n\n')


for n in range(i):
    print(f'\nSaídas do {n+1}º caso gravadas nos arquivos:')
    print(f'    c{n+1}_TRANSFERE.TXT')
    print(f'    c{n+1}_DIVERGENCIAS.TXT')
    print(f'    c{n+1}_TOTCANAL.TXT')

print('\nFim do programa')
