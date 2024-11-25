# Este programa lê o arquivo de entrada dados_pgm02.txt, que
#   contém em cada linha dois inteiros e um real separados pelo
#   caractere ';' (codigo;qtde;pcunitario).
# O programa deve gravar um arquivo de saida contendo os mesmos
#   dados da entrada, mais a multiplicação qtde * pcunitario

# Usar uma estrutura de armazenamento Lista de listas



# Leitura dos dados - criação da estrutura de armazenamento
Dados = []
arqEnt = open('dados_pgm02.txt', 'r')
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



# Processamento dos dados
#   em termos práticos, neste programa não há um processamento
#   que queiramos fazer. Mas se houvesse, faríamos aqui.



# Geração da Saida solicitada
arqSai = open('saida_pgm02.txt', 'w')
for item in Dados:
    arqSai.write(f'{item[0]};{item[1]};{item[2]:.2f};{item[3]:.2f}\n')
arqSai.close()


print('\n\nFim do Programa')
