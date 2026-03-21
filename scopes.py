# Escopo de variáveis
def my_function():
 print("Eu conheço aquela variável?", var)

var = 1
my_function()
print(var)
 
# Escopo de variáveis - parte 2
def my_function():
    var = 2
    print("Eu conheço aquela variável?", var)
 
var = 1
my_function()
print(var)

# Escopos gloais 
def my_function():
 global var
 var = 2
 print("Eu conheço aquela variável?", var)

var = 1
my_function()
print(var)

# ------------------------------------------------

def my_function(my_list_1):
    print("Print #1:", my_list_1) # Imprime a lista passada como argumento
    print("Print #2:", my_list_2) # Imprime a lista global my_list_2
    del my_list_1[0]  # Remove o primeiro elemento da lista my_list_1
    print("Print #3:", my_list_1) # Imprime a lista my_list_1 após a remoção do primeiro elemento
    print("Print #4:", my_list_2) # Imprime a lista my_list_2 de novo para mostrar que não foi afetada pela mudança de my_list_1
 
my_list_2 = [2, 3] # Define a lista global my_list_2
my_function(my_list_2) # Chama a função my_function passando my_list_2 como argumento
print("Print #5:", my_list_2) # Imprime a lista my_list_2 para mostrar que ela não foi afetada pela função my_function
# se o argumento for uma lista, a alteração do valor do parâmetro correspondente não afeta a lista
# mas se você alterar uma lista identificada pelo parâmetro (Nota: a lista, não o parâmetro!), a lista refletirá a alteração
