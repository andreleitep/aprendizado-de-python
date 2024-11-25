A = float(input("Escreva um dos lados do seu triângulo: "))
B = float(input("Escreva outro lado do seu triângulo: "))
C = float(input("Escreva o último lado do seu triângulo: "))

if A+B>C and A+C>B and B+C>A:
    print("Triângulo válido.")
    if A == B == C:
        print("É um triângulo equilátero.")
    elif A == B or B == C or A == C:
        print("É um triângulo isóceles.")
    elif A != B and A != C and B != C:
        print("É um triângulo escaleno.")

    if A**2+B**2==C**2 or A**2+C**2==B**2 or B**2+C**2==A**2:
        print("É um triângulo retângulo.")
else:
    print("Não é um triângulo.")
