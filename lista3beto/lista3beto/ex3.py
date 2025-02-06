#_______________________________________________EX 3_Médio_________________________________________________________
"""
Somas numeros de uma lista com reduce
"""
from functools import reduce
soma = (reduce(lambda x, y: x + y, [1,2,3,4]))
print (soma)
