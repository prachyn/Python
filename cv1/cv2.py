jmeno = "Tomas"
print(jmeno.upper())
print(jmeno.lower())

hodnoty = ['12', '1', '7', '-11']
hodnoty[2] = str(int(hodnoty[2])+4)
print(hodnoty)

hodnoty = '12.1 1.68 7.45 -11.51'.split(' ')
hodnoty[3] = str(float(hodnoty[3])+0.25)
hodnoty = ' '.join(hodnoty)
print(hodnoty)
