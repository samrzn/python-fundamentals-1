# Loop infinito usando while
while True:
    print("Estou preso dentro de um loop.")

# -----------------------------------------------

# Armazene o maior número atual aqui.
largest_number = -999999999
# Insira o primeiro valor.
number = int(input("Digite um número ou digite -1 para parar: "))
# Se o número não for igual a -1, continue.
while number != -1:
    # O número é maior que o maior_número?
    if number > largest_number:
        # Sim, atualize o maior_número.
        largest_number = number
    # Insira o próximo número.
    number = int(input("Digite um número ou digite -1 para parar: "))
# Imprima o maior número.
print("O maior número é:", largest_number)
 
# -----------------------------------------------

# Um programa que lê uma sequência de números
# e conta quantos números são pares e quantos são ímpares.
# O programa termina quando zero é digitado.
odd_numbers = 0
even_numbers = 0
# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))
# 0 termina a execução.
while number != 0:
    # Verifique se o número é ímpar.
    if number % 2 == 1:
        # Aumente o contador odd_numbers.
        odd_numbers += 1
    else:
        # Aumente o contador even_numbers.
        even_numbers += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))
# Imprimir resultados.
print("Números ímpares contam:", odd_numbers)
print("Números pares contam:", even_numbers)
 
# -----------------------------------------------

# Loop While com um contador
counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)
 
# Loop While compacto com um contador (os dois loops fazem a mesma coisa, porém o segundo, é menos legivel)
counter = 5
while counter:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)
 
# -----------------------------------------------

# Loop For usando range()
for i in range(100):
    # do_something()
    pass
 
# Loop For usando range() com uma instrução de impressão
for i in range(10):
   print("O valor de i é atualmente", i)

# Loop For usando range() com parâmetro inicial diferente de zero
for i in range(2, 8):
    print("O valor de i é atualmente", i)
 
# Loop For usando range() com três parâmetros, o terceiro é um incremento
for i in range(2, 8, 3):
  print("O valor de i é atualmente", i)

# Loop For usando range() para calcular potências de 2
power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2

# -----------------------------------------------

# As instruções break e continue
# break - para a execução do loop
print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")

# continue - segue a execução do loop, mesmo após atender uma condicional de finalização
print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")

# -----------------------------------------------

# Demonstração do uso da instrução break
largest_number = -99999999
counter = 0
while True:
    number = int(input("Digite um número ou digite -1 para terminar o programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("O maior número é", largest_number)
else:
    print("Você não inseriu nenhum número.")

# Demonstração do uso da instrução continue
largest_number = -99999999
counter = 0
number = int(input("Insira um número ou digite -1 para finalizar o programa: "))
while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Insira um número ou digite -1 para finalizar o programa: "))
if counter:
    print("O maior número é",  largest_number)
else:
    print("Você nnão tem inseriu qualquer número.")

# -----------------------------------------------

# Loop While com uma cláusula else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# Loop For com uma cláusula else
for i in range(5):
 print(i)
else:
 print("else:", i)