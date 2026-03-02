# +, -, *, /, //, %, **

# Multiplicação
print(2 * 3)
print(2 * 3.)
print(2. * .3)
print(2. * 3.)

# Divisão
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# Divisão arredondada
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
# O resultado da divisão do número inteiro é sempre arredondado para o valor inteiro mais próximo que é menor que o resultado real (não arredondado)
print(6 // 4)
print(6. // 4)
print(-6 // 4)
print(6. // -4)

# Restante (módulo)
print(14 % 4)
# 14 // 4 dá 3 → este é o quociente inteiro
# 3 * 4 dá 12 → como resultado da multiplicação de quociente e divisor
# 14 - 12 dá 2 → este é o restante

# Não é possível realizar divisão por zero
# Ou divisão inteira por zero
# Ou o restante de uma divisão (módulo) por zero

# Adição
print(-4 + 4)
print(-4. + 8)

# Subtração (unários e binários)
# Binários (representam operação aritmética)
print(-4 - 4)
print(4. - 8)
# Unários (representam uma propriedade do valor)
print(-1.1)
print(+2)
print(4 ** -1)

# A maioria dos operadores do Python tem ligação do lado esquerdo, o que significa que o cálculo da expressão é realizado da esquerda para a direita
print(9 % 6 % 2)

# Exceto com expoentes que o operador de exponenciação usa a associação do lado direito
print(2 ** 2 ** 3)
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

# Prioridades dos Operadores
# 1: **
# 2: +, - (unário) 
# 3: *, /, //, % 
# 4: +, - (binário)
print(2 * 3 % 5)

# Operadores e parênteses
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
