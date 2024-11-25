Nome = input("Escreva o nome do lutador: ")
Peso = float(input(f"Escreva o peso do {Nome}: "))

if Peso < 65:
    Categoria = "Pena"
elif Peso >= 65 and Peso < 72:
    Categoria = "Leve"
elif Peso >= 72 and Peso < 79:
    Categoria = "Ligeiro"
elif Peso >= 79 and Peso < 86:
    Categoria = "Meio médio"
elif Peso >= 86 and Peso < 93:
    Categoria = "Médio"
elif 93 <= Peso < 100:
    Categoria = "Meio pesado"
elif Peso >= 100:
    Categoria = "Pesado"

print(f"Nome fornecido: {Nome}")
print(f"Peso fornecido: {Peso}")
print(f"Saída exibida na tela: O lutador {Nome} pesa {Peso} kg e se enquadra na categoria {Categoria}")
