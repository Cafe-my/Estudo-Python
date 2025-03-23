# Comparacao
a = 7
b = 3
print(a == b)       # a igual b?            fica: False
print(a != b)       # a diferente de b?     fica: True
print(a > b)        # a maior que b?        fica: True
print(a < b)        # a menor que b?        fica: False
print(a <= b)       # a menor ou igual b?   fica: False
print(a >= b)       # a maior ou igual b?   fica: True

print('o' in 'John')        # 'o' aparece em 'John"?         fica: True
print('o' not in 'John')    # 'o'  nao aparece em 'John"?    fica: False

a = [3,7,42]
b = a
print(a == b)           # a igual a b?      fica: True
print(a is b)           # a identico ao b?  fica: True      significa que os dois ocupam o mesmo espaco de memoria
print(id(a), id(b))     # checar o ID       fica: 1629055967360 1629055967360       se ocupam a mesma memoria entao o ID e identico

a = [3,7,42]
b = [3,7,42]
print(a == b)           # fica: True
print(a is b)           # fica: False       eles sao equivalentes mas nao ocupam a mesma memoria 
print(id(a), id(b))     # fica: 2225258144128 2225259850944     IDs diferentes


# Booleans
print(int(False))       # fica: 0
print(int(True))        # fica: 1

print(42 + False)       # fica: 42
print(42 + True)        # fica: 43

print(bool('String'))   # Todo objeto transformado em boolean que nao for 0 ou vazio recebera True       fica: True
print(bool(''))         # fica: False
print(bool([]))         # fica: False

