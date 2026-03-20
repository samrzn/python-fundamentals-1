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

