# Primeiro
# COM DUAS LISTAS
# from os import RTLD_DEEPBIND
# |---------|
# | Funções |
# |---------|

def abrirArquivo(arquivo):
  with open(arquivo, "r") as texto:
    linhas = texto.readlines()
  return linhas

# def salvarArquivo(arquivo):

# |-----------|
# | Principal |
# |-----------|

# Definindo objetos

nome_arquivo = input("Escreva o nome do arquivo: ")
listaLinhas = abrirArquivo(nome_arquivo)
laco = int(listaLinhas[0].rstrip())
i = 1
D = []
E = []
repD = []
repE = []
chins = []
lidosE = []
lidosD = []

#Algoritmo

if laco < 1 or laco > 2000:
  print('O número de pares deve estar entre 1 e 2000')
else:
  while i <= laco:
      chins = listaLinhas[i].rstrip()
      chins = chins.split()
      chinE = int(chins[0])
      chinD = int(chins[1])
      if len(D) > 0 and len(E) > 0:
          if chinD in D:
              repD.append(chinD)
          else:
              D.append(chinD)
          if chinE in E:
              repE.append(chinE)
          else:
              E.append(chinE)
      else:
          D.append(chinD)
          E.append(chinE)
      i+=1

  repE.sort()
  repD.sort()

  saida = input('Digite o nome do arquivo: ')
  with open(saida, 'w') as arquivo_saida:
    for item in repE:
        if item in lidosE:
          continue
        else:
          arquivo_saida.write(f'{item} E {repE.count(item)}\n')
          lidosE.append(item)
    for item in repD:
        if item in lidosD:
          continue
        else:
          arquivo_saida.write(f'{item} D {repD.count(item)}\n')
          lidosD.append(item)
