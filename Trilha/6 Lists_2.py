friends = ['John','Michael','Terry','Eric','Graham']    # fica: ['John', 'Michael', 'Terry', 'Eric', 'Graham']
# Adicionando elementos na lista
friends.append('Alan')      # add um novo elemento no final da lista                            fica: ['Eric', 'Graham', 'John', 'Michael', 'Terry', 'Alan']
friends.insert(1,'Leo')     # insere um novo elemento na numeracao escolhida                    fica: ['John', 'Leo', 'Michael', 'Terry', 'Eric', 'Graham', 'Alan']
friends[0] = 'Iso'          # remove o elemento antigo no numeracao escolhida e add um novo     fica: ['Iso', 'Leo', 'Michael', 'Terry', 'Eric', 'Graham', 'Alan']


friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
# Extendendo e somando listas
friends.extend(cars)        # extende a lista com outra lista que escolher                          fica: ['John', 'Michael', 'Terry', 'Eric', 'Graham', 911, 130, 328, 535, 740, 308]
new_list = friends + cars   # Somando listas em uma nova       nao considerando o comando anterior, fica: ['John', 'Michael', 'Terry', 'Eric', 'Graham', 911, 130, 328, 535, 740, 308]
print(new_list)

friends = ['John','Michael','Terry','Eric','Graham','Lisa','Ana'] 
# Removendo elementos da lista
friends.remove('Eric')      # remove um elemento especifico da lista        fica: ['John', 'Michael', 'Terry', 'Graham', 'Lisa', 'Ana']
friends.pop()               # remove e retorna o ultimo elemento            fica: ['John', 'Michael', 'Terry', 'Graham', 'Lisa']
friends.pop(2)              # remove e retorna o elemento especifico        fica: ['John', 'Michael', 'Graham', 'Lisa']

a = friends.pop()           # retornando o ultimo elemento da lista     
print(a)                    # fica: Lisa
print(friends)              # fica: ['John', 'Michael', 'Graham']
del friends[1]              # deleta um elemento especifico                 fica: ['John', 'Graham']

# Removendo a lista
friends.clear()             # limpa a lista                                 fica: []
del friends                 # deleta a lista ocasionando erro               fica: NameError: name 'friends' is not defined


friends = ['John','Michael','Terry','Eric','Graham'] 
# Copiando listas
new_friends = friends[:]        # cria uma nova lista copia da outra
new_friends = friends.copy()    # mesma funcao
new_friends = list(friends)     # mesma funcao
