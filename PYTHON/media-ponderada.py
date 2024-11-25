Q = int(input())
i = 0
media = []
while i < Q:
    notas = input().split()
    a = float(notas[0])
    b = float(notas[1])
    c = float(notas[2])
    media.append((a*2 + b*3 + c*5) / 10)
    i+=1

i = 0
while i < Q:
    print(round(media[i], 1))
    i+=1
