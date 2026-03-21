# Tuplas com e sem parênteses
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
 
print(tuple_1)
print(tuple_2)
 
# Criando uma tupla vazia
empty_tuple = ()
 
# Criando uma tupla com um único elemento
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,

# Acessando elementos de uma tupla
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
 print(elem)

# Operações com tuplas
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# Alterando o valor de diversas tuplas ao mesmo tempo
var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)

# ------------------------------------------------------

# Dicionários
# um dicionário não é uma lista - a lista contém conjunto de valores numerados, enquanto o dicionário contém pares de valores
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"} # dicionário é um conjunto de pares 'key-value'
phone_numbers = {'chefe': 5551234567, 'Suzy': 22657854310} # cada chave deve ser única - não é possível chaves do mesmo valor
empty_dictionary = {} # a cahve pode ser um número (inteiro ou flutuante), ou até mesmo uma string, mas não uma lista
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
 
print(dictionary['gato']) # se a chave for uma string, você precisará especificá-la como uma string
print(phone_numbers['Suzy']) # chaves fazem distinção entre maiúsculas e minúsculas
 
# Acessando chaves que não existem (possível apenas com In ou Not In, sem isso gerará um erro)
words = ['gato', 'lion', 'cavalo']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")
 
# Loop For para acessar chaves e valores
for key in dictionary.keys(): # obrigatório usar o método .keys() para iterar o dicionário
    print(key, "->", dictionary[key])

# Loop For para acessar chaves e valores usando o método .items() 
for english, french in dictionary.items():
    print(english, "->", french)
 
# Substituindo valor em um dicionário
dictionary['gato'] = 'minou'
print(dictionary)
 
# Acessando apenas valores de um dicionário usando o método .values() 
for french in dictionary.values():
    print(french)
 
# Adicionando um novo par chave-valor a um dicionário 
dictionary['swan'] = 'cygne'
print(dictionary)
 
# Adicionando um novo par chave-valor a um dicionário usando o método .update()
dictionary.update({"pato": "canard"})
print(dictionary)
 
# Removendo uma chave de um dicionário usando o del(), consequentemente, o valor associado a chave também é removido
del dictionary['cachorro'] 
print(dictionary)
 
