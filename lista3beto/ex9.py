#_______________________________________________EX 9_Difícil________________________________________________________
"""
recebe lista tuplas, lê a média dos valores e separa a média maior e menos que 5, map e filter
"""

tuplas = [(2, 8), (4, 5, 6), (1, 2)]
acima_media = list(filter(lambda x: sum(x) > 5, tuplas))
abaixo_media = list(filter(lambda x: sum(x) < 5, tuplas))
print (f'Média acima de 5:',acima_media,'Média abaixo de 5:',abaixo_media)