from itertools import groupby
ventas = [15000, 22000, 12000, 17000, 81000, 13000, 21000, 41200, 25000, 21500, 91000, 21000]
ventas.sort()
diccionario= {k: len(list(v)) for k, v in groupby(ventas)}
print(diccionario)
