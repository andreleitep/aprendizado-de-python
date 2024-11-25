L = []

entrada = input()
L = entrada.split()
a = int(L[0])
b = int(L[1])
c = int(L[2])

MaiorAB = (a + b + abs(a - b)) / 2
MaiorABC = (MaiorAB + c + abs(MaiorAB - c)) / 2

print(f'{MaiorABC:.0f} eh o maior')
