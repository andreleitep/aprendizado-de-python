import time

A = int(input("Digite um valor para A: "))
B = int(input("Digite um valor para B: "))
if B == 0:
    print("Não é possível calcular a divisão.")
else:
    R = A / B
    print("Resultado: R = %.1f" % R)

time.sleep(5)
