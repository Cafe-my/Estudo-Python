is_raining = True                   # estabelecemos que essa variavel e True
print("Good Morning!")
if is_raining:                      # SE trouxermos a variavel e ela for True entao roda o seguinte comando:
    print("Bring umbrella!")                
else:                               # SENAO, ou seja False, entao roda o seguinte comando:
    print("Umbrella optional!")
# Fica: Good Morning!
#       Bring umbrella!

is_raining = False                  # estabelecemos que essa variavel e False
print("Good Morning!")
if is_raining:                      
    print("Bring umbrella!")                
else:                               
    print("Umbrella optional!")
# Fica: Good Morning!
#       Umbrella optional!

is_raining = True
is_cold = False
print("Good Morning!")
if is_raining or is_cold:                           # Se uma ou outra variavel for True entao roda o seguinte comando:
    print("Bring umbrella or jacket or both!")
else:                                               # Senao, ou seja duas False, entao:
    print("Umbrella optional!")
# Fica: Good Morning!
#       Bring umbrella or jacket or both!

is_raining = True
is_cold = False
print("Good Morning!")
if is_raining and is_cold:                          # Aqui as duas variaveis precisam ser True pra rodar o comando
    print("Bring umbrella and jacket!")
else:
    print("Umbrella optional!")


is_raining = True
is_cold = True
print("Good Morning!")
if is_raining and is_cold:                  # Se (is_raining e is_cold = True)
    print("Bring umbrella and jacket!")
elif is_raining and not(is_cold):           # SENAO SE (is_raining = True) e (is_cold = False)
    print("Bring umbrella!")
elif not(is_raining) and is_cold:           # SENAO SE (is_raining = False) e (is_cold = True)
    print("Bring jacket!")
else:                                       # Senao
    print("Umbrella optional!")


amount = 51
if amount <= 50:
    print("Purchase approved")
else:
    print("Please enter your PIN")