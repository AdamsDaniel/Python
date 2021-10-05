ano = 365
mes = 30

x = int(input(''))

A = int(x / ano)
M = int((x % ano) / mes)
D = int((x % ano) % mes)

print (f'{A} ano(s) \n{M} mes(es) \n{D} dia(s)')


