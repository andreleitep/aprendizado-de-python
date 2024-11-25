N = 0
i = 0
notas = []

while i < 2:
    N = round(float(input()), 1)
    if 0 <= N <= 10:
        notas.append(N)
        i+=1
    else:
        print('nota invalida')

print(f'media = {(notas[0] + notas[1]) / 2:.2f}')
