# Listas (Arrays)

numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
numbers[0] = 111
print("Novo conteúdo da lista: ", numbers)  # Conteúdo atual da lista após atribuição de novo valor no index 0.
 
numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
 
numbers[0] = 111
print("\nConteúdo da lista anterior:", numbers)  # Imprimindo conteúdos de listas anteriores.
 
numbers[1] = numbers[4]  # Copiando o valor do quinto índice para o segundo
print("Novo conteúdo da lista:", numbers)  # Imprime conteúdo atual da lista.

# -----------------------------------------------

# Função len() para obter o comprimento da lista
print ("\n List length:", len (numbers)) # Imprimindo o comprimento da lista

# Função del() para excluir um elemento da lista
del numbers[1]
print(len(numbers))
print(numbers)

# Função append() para adicionar um elemento ao final da lista
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
numbers.append (4) # Adicionando o número 4 ao final da lista.
print(len(numbers))
print(numbers)

numbers.insert (0, 222) # Inserindo o número 222 no início da lista (índice 0)
print(len (numbers))
print(numbers)

# Função insert() para inserir um elemento em uma posição específica da lista
numbers.insert(1, 333) # Inserindo o número 333 na posição de índice 1 da lista.
print(len(numbers))
print(numbers)

# -----------------------------------------------

# Utilizando um loop For para iterar sobre os elementos de uma lista e calcular a soma total dos elementos
my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
  total += my_list[i]
print(total)

# Outra forma de iterar sobre os elementos da lista usando loop For, sem precisar usar a função range() e o índice
my_list = [10, 1, 8, 3, 5]
total = 0
for i in my_list:
    total += i
print(total)
 
# -----------------------------------------------

# Índices negativos para acessar elementos a partir do final da lista.
numbers = [111, 7, 2, 1]
print(numbers[-1])  # Imprime o último elemento da lista.
print(numbers[-2])  # Imprime o penúltimo elemento da lista.

# -----------------------------------------------

# Atribuindo valores COM auxiliar de armazenamento
variable_1 = 1
variable_2 = 2
 
auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
 
print(variable_1)  # Imprime o valor de variable_1 após a troca.
print(variable_2)  # Imprime o valor de variable_2 após a troca.

# Atribuindo valores SEM auxiliar de armazenamento
variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1
 
print(variable_1)  # Imprime o valor de variable_1 após a troca.
print(variable_2)  # Imprime o valor de variable_2 após a troca.

# Atribuindo valores SEM auxiliar de armazenamento em uma lista
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)

# -----------------------------------------------
 
my_list = [1, None, True, 'eu sou um barbante', 256, 0]
print(my_list[3])  # outputs: eu sou um barbante
print(my_list[-1])  # outputs: 0
 
my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'eu sou um barbante', 256, 0]
 
my_list.insert(0, "primeiro")
my_list.append("último")
print(my_list)  # outputs: ['primeiro', 1, '?', True, 'eu sou um barbante', 256, 0, 'último']
 
# Aninhando listas
my_list = [1, 'a', ["lista", 64, [0, 1], False]]
print(my_list[2])  # outputs: ['lista', 64, [0, 1], False]
print(my_list[2][2])  # outputs: [0, 1]
print(my_list[2][2][1])  # outputs: 1