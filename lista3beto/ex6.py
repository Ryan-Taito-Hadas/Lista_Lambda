#_______________________________________________EX 6_Médio_________________________________________________________
"""
receber numeros e retornar um dicionário com as chaves "pares" e "impares"
"""

dic = {'Pares': [], 'Impares': []}
dic['Pares'] = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6]))
dic['Impares'] = list(filter(lambda y: y % 2 == 1, [1,2,3,4,5,6]))
print (dic)
