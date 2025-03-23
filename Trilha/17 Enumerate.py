friends = ['Brian', 'Judith', 'Reg', 'Loretta']

# i = 1                            # fica: 1 Brian
# for friend in friends:           #       2 Judith
#     print(i, friend)             #       3 Reg
#     i += 1                       #       4 Loretta

for num, friend in enumerate(friends):  # num recebe index criado pela funcao enumerate (0, 1, 2, 3)
    print(num, friend)                  # friend recebe o valor do elemento dentro da lista "friends" correspondente ao index
# fica: 0 Brian
#       1 Judith
#       2 Reg
#       3 Loretta
    
print(type(enumerate(friends)))         # <class 'enumerate'>                      
print(list(enumerate(friends)))         # [(0, 'Brian'), (1, 'Judith'), (2, 'Reg'), (3, 'Loretta')]


# Podemos modificar o start da contagem:
for num, friend in enumerate(friends,51):
    print(num, friend)
# fica: 51 Brian
#       52 Judith
#       53 Reg
#       54 Loretta


# e possivel enumerar a enumeracao...
for friend in enumerate(enumerate(friends,51),-100):
    print(friend)   
# fica: (-100, (51, 'Brian'))
#       (-99, (52, 'Judith'))
#       (-98, (53, 'Reg'))
#       (-97, (54, 'Loretta'))