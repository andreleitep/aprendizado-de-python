Q = int(input())

i = 0
IN = 0
OUT = 0
while i < Q:
    X = int(input())
    if 10 <= X <= 20:
        IN += 1
    else:
        OUT += 1
    i += 1
    
print(f'{IN} in\n{OUT} out')
