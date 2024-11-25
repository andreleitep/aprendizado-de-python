LMin = int(input("Digite um número mínimo: "))
LMax = int(input("Digite um número máximo: "))
N = int(input("Quantos números você quer listar? "))
i = 0
L = []
R = []

if LMax > LMin:
    while i < N:
        X = int(input("Insira um número: "))
        if LMax >= X >= LMin:
            L.append(X)
        else:
            print("Valor ignorado.")
            R.append(X)
        i += 1
elif LMax < LMin:
    while i < N:
        X = int(input("Insira um número: "))
        if LMax <= X <= LMin:
            L.append(X)
        else:
            print("Valor ignorado.")
            R.append(X)
        i += 1
else:
    print("Error: LMax = LMin")

print(f"A lista L possui {len(L)} elementos:\n{L}\n")
print(f"{len(R)} valores foram ignorados:\n{R}")
