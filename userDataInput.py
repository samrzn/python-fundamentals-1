# Função Input p/ entrada de dados
print("Conta-me qualquer coisa...")
anything = input()
print("Hum...", anything, "...Realmente?")
 
# Variação de forma de implementação da função Input()
anything = input("Conta-me qualquer coisa: ")
print("Hum...", anything, "...Realmente?")

# Não é possível fazer operações aritméticas com entradas da função Input por serem primitivamente uma string
anything = input("Digite um número: ")
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

# Mas é possível manipular e convertes esses dados de entrada
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

# É possível declarar expressões no argumento da função print()
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é", (leg_a**2 + leg_b**2) ** .5)

# Concatenando caracteres
fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")

# Replicação de caracteres
print("James" * 3)
print(3 * "ah")
print("2" * 5)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# Convertendo números em string
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é " + str((leg_a**2 + leg_b**2) ** .5))

# Operadores e expressões
x = float(input("Digite o valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

# Exemplos de operações aritméticas
print(1//2 * 3)

x = int(input())
y = int(input())

x = x % y
x = x % y
y = y % x

print(y)

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)