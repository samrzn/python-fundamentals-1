# Operador de atribuição
operadorDeAtribuicao = "="

# Operador de igualdade
operadorDeIgualdade = "=="

# Operador de desigualdade
operadorDeDesigualdade = "!="

# Operadores de comparação
operadoresDeComparacao = ">, >=, <, <="
# Maior
operadorMaiorQue = ">"
# Maior ou igual
operadorMaiorOuIgual = ">="
# Menor
operadorMenorQue = "<"
# Menor ou igual
operadorMenorOuIgual = "<="

# Prioridades dos Operadores
# 1: **
# 2: +, - (unário) 
# 3: *, /, //, % 
# 4: +, - (binário)
# 5: <, <=, >, >=
# 6: ==, !=

n = int(input("Digite um número: ")) 
print(n >= 100) 

# Condições e execução condicional
the_weather_is_good = False
def go_for_a_walk(): print('Walk.')
def have_lunch(): print('Lunch time, yummy!')
# As instruções contidas no Bloco If devem estar todas alinhadas no mesmo nível de identação, o interprete Python não aceita linhas em ordens diferentes para ler o código do bloco condicional
if the_weather_is_good:
    go_for_a_walk()
have_lunch()

# Exemplo de identação para recuo correto de Blocos If (descomente o código)
# if sheep_counter >= 120:
#     make_a_bed()
#     take_a_shower()
#     sleep_and_dream()
# feed_the_sheepdogs()

def have_fun(): print('Having fun.')
def go_to_a_theater(): print('Going to the theater.')
def enjoy_the_movie(): print('Watching movie.')
# Tudo que foi dito sobre identação anteiormente, também se aplica no Bloco Else
if the_weather_is_good:
    go_for_a_walk()
    have_fun()
else:
    go_to_a_theater()
    enjoy_the_movie()
have_lunch()

# Aninhamentos de If-Else
def eat_a_sandwich(): print('Eating a delicious sandwich.')
def go_to_the_theater(): print('In the theater.')
def go_shopping(): print('Shopping.')
nice_restaurant_is_found = False
tickets_are_available = True
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

# Condicional Elif
def go_for_lunch(): print('Lunch time, yummy!')
def play_chess_at_home(): print("It's better to stay at home playing some chess...")
table_is_available = True
tickets_are_available = False
# Montagens de 'if-elif-else' subsequentes são chamadas de cascata
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

# Exemplos de operadores de comparação e condicionais
# Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
# Escolha o número maior
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
# Imprimir o resultado
print("O maior número é:", larger_number)

# Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
# Escolha o número maior
if number1 > number2: larger_number = number1
else: larger_number = number2 
# Imprimir o resultado
print("O maior número é:", larger_number)

# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Assumimos temporariamente que o primeiro número
# é o maior deles.
# Em breve verificaremos isso.
largest_number = number1
 
# Nós verificamos se o segundo número é maior que o maior_número atual
# E atualize o maior_número, se necessário
if number2 > largest_number:
    largest_number = number2
# Nós verificamos se o terceiro número é maior que o maior_número atual
# E atualize o maior_número, se necessário
if number3 > largest_number:
    largest_number = number3
# Imprimir o resultado
print("O maior número é:", largest_number)

# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
# Assumimos temporariamente que o primeiro número é o maior deles
# Em breve verificaremos isso
largest_number = number1
# Nós verificamos se o segundo número é maior que o maior_número atual
# E atualize o maior_número, se necessário
if number2 > largest_number:
    largest_number = number2
# Nós verificamos se o terceiro número é maior que o maior_número atual
# E atualize o maior_número, se necessário
if number3 > largest_number:
    largest_number = number3
# Imprimir o resultado
print("O maior número é:", largest_number)

# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
# Verifique qual dos números é o maior
# E passe-o para a variável de número_maior
largest_number = max(number1, number2, number3)
# Imprimir o resultado
print("O maior número é:", largest_number)
 
# If, Elif, Else
name = input("Insira o nome da flor: ")
if name == "Spathiphyllum":
    print("Sim - Spathiphyllum é a melhor planta de todos os tempos!")
elif name == "spathiphyllum":
    print("Não, eu quero uma grande Spathiphyllum!")
else:
    print("Spathiphyllum! Não", name + "!")

# Ano bissexto checker
year = int(input("Digite um ano: "))
if year < 1582:
 print("Não dentro do período do calendário gregoriano")
else:
   if year % 4 != 0:
     print("ano comum")
   elif year % 100 != 0:
     print("Ano bissexto")
   elif year % 400 != 0:
     print("ano comum")
   else:
     print("Ano bissexto") 
 