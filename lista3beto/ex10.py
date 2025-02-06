#_______________________________________________EX 10_Difícil________________________________________________________
"""
função que recebe um dicionário onde as chaves são nomes de alunos e
os valores são listas de notas (com pesos na última posição). A função deve calcular
a média ponderada de cada aluno usando reduce e retornar um novo dicionário
com os resultados.
"""

dic3 = {'João': (8,7,9,2),
        'Ana': (5,6,7,3),
        'Média do João': (),
        'Média da Ana': ()}

dic3['Média do João'] = lambda x: sum(x[:3]) * 2 / (3 * 2)
print (dic3['Média do João'](dic3['João']))
dic3['Média da Ana'] = lambda x: sum(x[:3]) * 3 / (3 * 3)
print (dic3['Média da Ana'](dic3['Ana']))