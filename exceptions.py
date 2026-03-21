try:
 value= int (input('Insira um número natural:')) 
 print('O recíproco de', valor, 'é', 1 / value) 
except: 
    print('Não sei o que fazer.')

# ---------------------------------------------------

try:
    value = int(input("Entre um valor: "))
    print(value/value)
except ValueError:
    print("Entrada incorreta...")
except ZeroDivisionError:
    print("Entrada muito ruim...")
except:
    print("Booo!")
 
# ---------------------------------------------------

value = input("Entre um valor: ")
print(10/value)
 
