coordenadas = input()
L = [int(n) for n in coordenadas.split()]

while L[0] != 0 and L[1] != 0:
    if L[0] > 0 and L[1] > 0:
        print('primeiro')
    elif L[0] < 0 and L[1] > 0:
        print('segundo')
    elif L[0] < 0 and L[1] < 0:
        print('terceiro')
    elif L[0] > 0 and L[1] < 0:
        print('quarto')
    coordenadas = input()
    L = [int(n) for n in coordenadas.split()]
