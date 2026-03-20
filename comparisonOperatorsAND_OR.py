# Operador AND
counter = 10
value = 100
counter > 0 and value == 100

# Tabela verdade AND
# A (false) &  B (false) = A and B (false)
# A (false) &  B (true)  = A and B (false)
# A (true)  &  B (false) = A and B (false)
# A (true)  &  B (true)  = A and B (true)

# -----------------------------------------------

# Operador OR
counter > 0 and value == 100

# Tabela verdade OR
# A (false) |  B (false) = A or B (false)
# A (false) |  B (true)  = A or B (true)
# A (true)  |  B (false) = A or B (true)
# A (true)  |  B (true)  = A or B (true)

# -----------------------------------------------

# Operador NOT
var = 10
print(var > 0)
print(not (var <= 0)) # False mas o operador NOT inverte o resultado para True
  
print(var != 0)
print(not (var == 0)) # False mas o operador NOT inverte o resultado para True
 
# Operadores Bit a Bit
print('& (e comercial) - conjunção bit a bit')
print('| (barra) - disjunção bit a bit')
print('~ (til) - negação bit a bit')
print('^ (circunflexo) ‒ bit a bit exclusivo ou (xor)')

# Prioridades dos Operadores
# 1: ˜, +, - (unário)
# 2: **
# 3: *, /, //, % 
# 4: +, - (binário) 
# 5: <<, >>
# 6: <, <=, >, >=
# 7: ==, !=
# 8: &
# 9: |
# 10: =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=