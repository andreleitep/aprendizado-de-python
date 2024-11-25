#Grupo formado por André Leite, Felipe Malbet, Giovanna Rosa, João Victor Bispo


# Entradas e variáveis
modelos_iniciais = []
repeticoes_esquerda = {}
repeticoes_direita = {}

nome_arquivo_entrada = input("Digite o nome do arquivo de entrada (com .txt): ")

try:
    with open(nome_arquivo_entrada, 'r') as arquivo:
        linhas = arquivo.readlines()
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e tente novamente.")
    exit()

#Algoritmo
num_pares = int(linhas[0].strip())
if num_pares < 1 or num_pares > 2000:
    print("O número de pares deve ser entre 1 e 2000.")
    exit()

for linha in linhas[1:num_pares + 1]:
    try:
        esquerdo, direito = map(int, linha.split())
    except ValueError:
        print("Entrada inválida no arquivo. Certifique-se de usar o formato 'num num'.")
        continue

    if esquerdo == direito:
        print("Os valores para o lado esquerdo e direito não podem ser iguais.")
        continue

    modelos_iniciais.append((esquerdo, direito))
    
    if any(esquerdo == m[0] for m in modelos_iniciais[:-1]):
        repeticoes_esquerda[esquerdo] = repeticoes_esquerda.get(esquerdo, 0) + 1

    if any(direito == m[1] for m in modelos_iniciais[:-1]):
        repeticoes_direita[direito] = repeticoes_direita.get(direito, 0) + 1

# Ordenação
repeticoes = []

for modelo, qtd in repeticoes_esquerda.items():
    repeticoes.append((modelo, 'E', qtd))

for modelo, qtd in repeticoes_direita.items():
    repeticoes.append((modelo, 'D', qtd))

repeticoes.sort()

# Saída
nome_arquivo_saida = "saida_repeticoes.txt"
with open(nome_arquivo_saida, 'w') as arquivo_saida:
    if repeticoes:
        for modelo, lado, qtd in repeticoes:
            arquivo_saida.write(f"{modelo} {lado} {qtd}\n")
    else:
        arquivo_saida.write("SEM TROCAS DESTA VEZ\n")

print(f"Resultado salvo no arquivo '{nome_arquivo_saida}'.")
