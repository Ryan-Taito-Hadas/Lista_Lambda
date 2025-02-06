#_______________________________________________EX 8_Difícil________________________________________________________
"""
recebe lista de palavras e conta quantas letras todas as palavras juntas têm, map e reduce
"""
from functools import reduce
palavras = ['casa', 'Jorge', 'aranha', 'hipopotomonstrozesquipedaliofobia']
soma = (reduce(lambda x, y: x + y,map(len, (palavras))))
print (f'Ao todo soma ',{soma},' letras')
