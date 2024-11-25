salarioIni = round(float(input()), 2)

if salarioIni <= 400.00:
    aum = salarioIni * 0.15
    salarioAtu = salarioIni + aum
    print(f'Novo salario: {salarioAtu:.2f}\nReajuste ganho: {aum:.2f}\nEm percentual: 15%')
if salarioIni > 400.00 and salarioIni <= 800.00:
    aum = salarioIni * 0.12
    salarioAtu = salarioIni + aum
    print(f'Novo salario: {salarioAtu:.2f}\nReajuste ganho: {aum:.2f}\nEm percentual: 12%')
if 800.00 < salarioIni <= 1200.00:
    aum = salarioIni * 0.10
    salarioAtu = salarioIni + aum
    print(f'Novo salario: {salarioAtu:.2f}\nReajuste ganho: {aum:.2f}\nEm percentual: 10%')
if 1200.00 < salarioIni <= 2000.00:
    aum = salarioIni * 0.07
    salarioAtu = salarioIni + aum
    print(f'Novo salario: {salarioAtu:.2f}\nReajuste ganho: {aum:.2f}\nEm percentual: 7%')
if salarioIni > 2000.00:
    aum = salarioIni * 0.04
    salarioAtu = salarioIni + aum
    print(f'Novo salario: {salarioAtu:.2f}\nReajuste ganho: {aum:.2f}\nEm percentual: 4%')
