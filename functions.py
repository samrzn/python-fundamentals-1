# Definindo uma função simples que imprime uma mensagem
def message():
    print("Entre um valor: ")
 
print("Começamos aqui.")
message()
print("terminamos aqui.")

# Ref.: https://docs.python.org/3/library/functions.html

# --------------------------------------------------

# Definindo uma função que recebe um argumento e imprime uma mensagem personalizada
def hello(name):    # definindo uma função
    print("Olá,", name)    # o corpo da função
  
name = input("Entre um valor: ")
hello(name)    # chamando a função

# Definindo outra função que recebe um argumento e imprime uma mensagem personalizada 
def message(number):
    print("Digite um número:", number)
 
message(1)

# --------------------------------------------------
 
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")
 
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
 
# ---------------------------------------------------

# Passagem de argumentos por palavra-chave
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
 
# ----------------------------------------------------

# Definindo uma função que recebe três argumentos e imprime a soma deles
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
 
adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
 
# Passando parâmetro misturados por posição e palavra-chave
adding(3, c = 1, b = 2)
 
adding(3, a = 1, b = 2) # Vai estourar erro ao passar o argumento 'a' por posição e palavra-chave ao mesmo tempo
 
# ----------------------------------------------------

# Parâmetros opcionais com valores padrão
def introduction(first_name, last_name="Smith"):
     print("Olá meu nome é", first_name, last_name)
 
introduction("James", "Doe") # Sobrescreve o valor padrão do parâmetro 'last_name' se passado um argumento neste
introduction("Henry")
introduction(first_name="William") # Imprime o valor passado no parâmetro presente + o valor padrão de 'last_name'

# ----------------------------------------------------

# Funções com retorno
def happy_new_year(wishes = True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not wishes:
        return  # A palavra-chave 'return' é usada para sair da função imediatamente, sem executar o restante do código
 
    print("Feliz Ano Novo!")
 
happy_new_year()
happy_new_year(False)

# Função que retorna um valor
def boring_function():
    return 123
x = boring_function()
print("A aborrecimento_função retornou seu resultado. Isso é:", x)
 
# Função que retorna um valor booleano
def strange_function(n):
 if(n % 2 == 0):
    return True

print(strange_function(4)) # True
print(strange_function(2)) # True
print(strange_function(1)) # None
 
# -----------------------------------------------------

# Iterando sobre uma lista dentro de uma função
def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
 
print(list_sum([5, 4, 3])) # output: 12
print(list_sum(5)) # output: TypeError: 'int' object is not iterable
 
# Criando uma lista dentro de uma função
def strange_list_fun(n):
 strange_list = []
 
 for i in range(0, n):
    strange_list.insert(0, i)
 
 return strange_list

print(strange_list_fun(5))

# ------------------------------------------------------

# Imprime uma mensagem e retorna um valor (mas o valor não é usado)
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
wishes()
 
# Imprime uma mensagem e retorna um valor (mas o valor é usado, pois a função é chamada dentro de um print)
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
print(wishes())

# Definindo uma função que recebe uma lista de nomes e imprime uma mensagem personalizada para cada nome
def hi_everybody(my_list):
    for name in my_list:
        print("Oi,", name)
 
hi_everybody(["Adão", "John", "Lucy"])
 
# ------------------------------------------------------

# Definindo uma função que verifica se um dado é do tipo inteiro
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False
 
print(is_int(5))
print(is_int(5.0))
print(is_int("5"))

# Função que recebe um número e retorna uma lista de números pares menores que o número dado 
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst
 
print(even_num_lst(11))
 