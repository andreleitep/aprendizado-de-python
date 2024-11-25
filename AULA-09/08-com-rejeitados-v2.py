LMin = int(input("Digite um número mínimo: "))
LMax = int(input("Digite um número máximo: "))
N = int(input("Quantos números você quer listar? "))
L = []
R = []

if LMax < LMin:
    LMax, LMin = LMin, LMax

for i in range(N):
    X = int(input("Insira um número: "))
    if LMax >= X >= LMin:
        L.append(X)
    else:
        print("Valor ignorado.")
        R.append(X)

print(f"A lista L possui {len(L)} elementos:\n{L}\n")
print(f"{len(R)} valores foram ignorados:\n{R}")
