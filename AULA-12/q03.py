N = int(input('digite N: '))

print(' ', '*' * (N-2), sep='')
print('*'*N)
ll = (N - 2) // 2
for i in range(ll):
    print(' '*i, '**', ' '*(N-4-2*i), '**', sep='')
print(' '*(ll-1), '**')


print('\n\nFim do Programa')
