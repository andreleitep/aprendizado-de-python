# Este programa lê o arquivo de entrada dados_pgm02.txt, que
#   contém em cada linha dois inteiros e um real separados pelo
#   caractere ';' (codigo;qtde;pcunitario).
# O programa deve gravar um arquivo de saída contendo os mesmos
#   dados da entrada, mais a multiplicação qtde * pcunitario

# Usar armazenamento Lista de listas

Dados = []
arqEnt = open('dados_pgm02.txt', 'r') # 'r' = read
s = arqEnt.readline().rstrip()
while s != '':
    s = s.split(';')
    item = [
            int(s[0]),
            int(s[1]),
            float(s[2]),
            int(s[1]) * float(s[2])
        ]
    Dados.append(item)
    s = arqEnt.readline().rstrip()
arqEnt.close()
print('\nDados lidos do arquivo')
for item in Dados:
    print(item)

# Leitura dos dados - criação da estrutura de armazenamento

# Processamento dos dados

# Geração da Saída solicitada

arqSai = open('saida_pgm02.txt')
for item in Dados:
    arqSai.write(f'{item[0]};{item[1]};{item[2]};{item[3]}\n')
arqSai.close()

print('\n\nFim do programa')
