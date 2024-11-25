#rascunho gi
#Grupo formado por André Leite, Felipe Malbet, Giovanna Rosa, João Victor Bispo
print('Grupo formado por:\n\nAndré Leite\nFelipe Malbet\nGiovanna Rosa\nJoão Victor Bispo\n')

# |---------|
# | Funções |
# |---------|

def lerArquivo(nome):
    arq = open(nome, 'r')
    listaLinhas = []
    listaLinhas.append(arq.readline().rstrip())
    i = 0
    while listaLinhas[i] != '':
        listaLinhas.append(arq.readline().rstrip())
        i += 1
    arq.close()
    del listaLinhas[-1]
    return listaLinhas

def proc_produtos(lista):
  produtos = {}
  i = 0
  while i < len(lista):
    produto, EstInicial, QtMin = lista[i].split(';')
    produtos = {
        'Codigo do Produto' : int(produto),
        'Quantidade inicial no estoque': int(EstInicial),
        'Quantidade Min no Centro Operacional': int(QtMin)
        }
    i += 1
    return produtos

def proc_vendas(lista):
  vendas = {}
  i = 0
  while i < len(lista):
    produto, QtVendas, status, canal = lista[i].split(';')
    vendas = {
        'Codigo do Produto' : int(produto),
        'Quantidade vendida': int(QtVendas),
        'Status de vendas': int(status),
        'Canal de vendas': int(canal)
        }
    i += 1
  return vendas

# |-----------|
# | Principal |
# |-----------|

# Definindo objetos:

i = 0
o = 0
listaProdutos = []
listaVendas = []

# Algoritmo

while i < 2:
    listaProdutos = lerArquivo(f'c{i+1}_produtos.txt')
    listaVendas = lerArquivo(f'c{i+1}_vendas.txt')

    dict1 = proc_produtos(listaProdutos)
    dict2 = proc_vendas(listaVendas)

    for i in dict1:
        dictProdutos[dict1['Codigo do Produto']] = {
            'Quantidade inicial no estoque': dict1['Quantidade inicial no estoque'],
            'Quantidade Min no Centro Operacional': dict1['Quantidade Min no Centro Operacional']
            }
        dictProdutos[dict2['Codigo do Produto']] = {
            'Quantidade vendida': dict2['Quantidade vendida'],
            'Status de vendas': dict2['Status de vendas'],
            'Canal de vendas': dict2['Canal de vendas']
            }
        o += 1
    i += 1


'saida = ordem crescente'
