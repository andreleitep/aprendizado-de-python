V = int(input())
Vprocess = V
print(V)

n100 = Vprocess // 100
Vprocess = Vprocess - (n100 * 100)
n50 = Vprocess // 50
Vprocess = Vprocess - (n50 * 50)
n20 = Vprocess // 20
Vprocess = Vprocess - (n20 * 20)
n10 = Vprocess // 10
Vprocess = Vprocess - (n10 * 10)
n5 = Vprocess // 5
Vprocess = Vprocess - (n5 * 5)
n2 = Vprocess // 2
Vprocess = Vprocess - (n2 * 2)
n1 = Vprocess // 1

print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')
