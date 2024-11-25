def abrirArquivo(arquivo):
  with open(arquivo, "r") as texto:
    linhas = texto.readlines()
  return linhas

# Entradas e variáveis
modelos_iniciais = []
repeticoes_esquerda = {}
repeticoes_direita = {}

nome_arquivo = input("Escreva o nome do arquivo: ")
listaLinhas = abrirArquivo(nome_arquivo)

# Número de pares total
num_pares = int(listaLinhas[0].rstrip())
if num_pares < 1 or num_pares > 2000:
    print("O número de pares deve estar entre 1 e 2000.")

# Coleta dos pares

else:
    print('ok')
    for _ in range(num_pares):
        while True:
            entrada = input("Digite o modelo do lado esquerdo e direito (separados por espaço): ")
            try:
                esquerdo, direito = map(int, entrada.split())
            except ValueError:
                print("Entrada inválida. Certifique-se de usar o formato 'num num'.")
                continue

            # Verifica se os números são iguais
            if esquerdo == direito:
                print("Os valores para o lado esquerdo e direito não podem ser iguais.")
                continue

            # Verificação e armazenamento das repetições
            modelos_iniciais.append((esquerdo, direito))
            
            # Verifica e conta repetições no lado esquerdo
            if any(esquerdo == m[0] for m in modelos_iniciais[:-1]):
                repeticoes_esquerda[esquerdo] = repeticoes_esquerda.get(esquerdo, 0) + 1

            # Verifica e conta repetições no lado direito
            if any(direito == m[1] for m in modelos_iniciais[:-1]):
                repeticoes_direita[direito] = repeticoes_direita.get(direito, 0) + 1

            break

    # Exibindo o resultado das repetições
    print("\nRepetições detectadas:")
    for modelo, qtd in repeticoes_direita.items():
        print(f"{modelo} D {qtd}")
    for modelo, qtd in repeticoes_esquerda.items():
        print(f"{modelo} E {qtd}")
