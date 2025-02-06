#_______________________________________________EX 7_Difícil________________________________________________________
"""
recebe lista de numeros, coloca num dicionario separando em 3 listas, "positivos", "negativos" e "zeros"
"""

dic1 = {'Positivos': [], 'Negativos': [], 'Zeros': []}
dic1['Positivos'] = list(filter(lambda x: x > 0, [1, -2, 0, -5, 0]))
dic1['Negativos'] = list(filter(lambda x: x < 0, [1, -2, 0, -5, 0]))
dic1['Zeros'] = list(filter(lambda x: x == 0, [1, -2, 0, -5, 0]))
print (dic1)
