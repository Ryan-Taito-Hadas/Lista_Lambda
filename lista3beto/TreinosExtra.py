from functools import reduce
"""
isinstance() - Verificar se é número ou string
Dado a lista dados = [12, "Python", 45.6, "42", "Códigos", 78], crie um programa que:

Separe os números e as strings em listas diferentes.
Exiba as duas listas separadamente.
"""

dados = [12, "Python", 45.6, "42", "Códigos", 78]
palavras = []
numeros = []

for i in dados:
        if (isinstance(i,str)):
                palavras.append(i)
        else:
                numeros.append(i)
print(palavras)
print(numeros)
        
"""
Manipulação de listas
Crie um programa que:

Peça ao usuário para digitar 5 números separados por espaço.
Transforme essa entrada em uma lista de números inteiros.
Some todos os números e exiba o resultado.
Inverta a lista e exiba.
"""
num = [1,2,3,4,5]
soma = reduce(lambda x,y:x+y,num)

print (soma)
print (num[::-1])

"""
Manipulação de string (split() e replace())
Dado o texto: "Aprender Python é muito divertido, Python é incrível!"

Substitua "Python" por "programação" em toda a frase.
Separe a frase em uma lista de palavras e exiba.
"""

texto = "Aprender Python é muito divertido, Python é incrível!"
texto = texto.replace('Python','Programação')
print(texto)

"""
filter()
Dada a lista numeros = [10, 15, 22, 33, 40, 55, 60], use filter() para:

Criar uma nova lista contendo apenas os números pares.
"""

numeros = [10, 15, 22, 33, 40, 55, 60]
pares = list(filter(lambda x: x % 2 == 0,numeros))
print (pares)

"""
map()
Dada a lista valores = [5, 10, 15, 20], use map() para:

Criar uma nova lista onde cada valor seja dobrado.
"""

valores = [5, 10, 15, 20]
dobro = list(map(lambda x: x * 2,valores))
print(dobro)

"""
reduce()
Dada a lista valores = [1, 2, 3, 4, 5], use reduce() para:

Multiplicar todos os elementos, obtendo um único resultado.
"""

valores = [1, 2, 3, 4, 5]

multi = reduce(lambda x, y: x * y, valores)
print (multi)

"""
Manipulação de tuplas
Dada a tupla dados = ("Carlos", 25, "Engenheiro", "São Paulo"), crie um programa que:

Exiba cada elemento da tupla separadamente usando um laço for.
"""
dados = ("Carlos", 25, "Engenheiro", "São Paulo")

for i in dados:
        print(i)

"""
Laços (for e while)
Crie um programa que:

Peça um número ao usuário.
Exiba a tabuada desse número de 1 a 10 usando for.
Depois, faça a mesma tabuada usando while.
"""
numero = 5
for i in range(11):
        print (f'=',numero,'x',i,'=',numero*i)

"""
Separando tipos e dobrando valores (Fácil)
Dada a lista:

python
Copiar
Editar
dados = [10, "Python", 20.5, "35", "Code", 50, "100"]
Crie um programa que:

Separe os números e as strings em listas diferentes.
Converta as strings numéricas em inteiros e adicione à lista de números.
Use map() para dobrar os números.
Exiba os resultados.
"""

dados = [10, "Python", 20.5, "35", "Code", 50, "100"]
dados[3,6] = int(list(dados[3,6])) 
dic = {'numeros': [],
       'palavras':[]}

for i in dados:
        if isinstance(i,int):
                dic['numeros'].append(i)
        else:
                dic['palavras'].append(i)

print(dic)

"""
Exercise 4: Map with Conditional Logic

Write a Python program that takes a list of integers and returns a new list where:

    If the number is positive, it is squared.

    If the number is negative, it is converted to its absolute value.

    If the number is zero, it is replaced with None.

Use map and lambda.
"""
