#---------------------
#Declaração de objetos
#---------------------

from random import randint
A=[]
B=[]
AB=[]
nA=int(input("Tamanho da lista A: "))
nB=int(input("Tamanho da lista B: "))
i=0

#--------------
#Gerando listas
#--------------

while i < nA:
    A.append(randint(0, 100))
    i+=1
print(f'Lista A: {A}')
i=0
while i < nB:
    B.append(randint(101, 200))
    i+=1
print(f'Lista B: {B}')

#---------------
#Juntando listas
#---------------

while len(A) > 0:
    AB.append(A[0])
    del(A[0])
while len(B) > 0:
    AB.append(B[0])
    del(B[0])

print(f'Listas A e B somadas: {AB}')
print('\nFim do programa')
