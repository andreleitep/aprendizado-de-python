import math

print("Calculando uma equação de segundo grau:")
a = float(input("Escreva o valor de a: "))
b = float(input("Escreva o valor de b: "))
c = float(input("Escreva o valor de c: "))
delta = b ** 2 - 4 * a * c

if delta == 0:
    X1 = -b / (2 * a)
    X2 = ""
elif delta > 0:
    rtDelta = math.sqrt(delta)
    X1 = (-b + rtDelta) / (2 * a)
    X2 = (-b - rtDelta) / (2 * a)
else:
    X1 = ""
    X2 = ""

print(f"Delta é igual a {delta}")
if X1 != "" and X2 != "":
    print(f"X é igual a {X1} ou {X2}.")
elif X1 != "":
    print(f"X é igual a {X1}.")
else:
    print("Esta equação não possui raízes reais.")
