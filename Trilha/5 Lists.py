friends = ['Jhon', 'Michael', 'Sara', 'Eve', 'Eric']
#             0        1        2       3      4        : Os elementos da lista podem ser indexados
print(friends)                  # Fica: ['Jhon', 'Michael', 'Sara', 'Eve', 'Eric']
print(friends[1], friends[4])   # Fica: Michael Eric
print(friends[:3])              # Fica: ['Jhon', 'Michael', 'Sara']
print(len(friends))             # Fica: 5  -> contando o numero de itens da lista
print(friends.index('Sara'))    # Fica: 2  -> indica em qual posicao o elemento esta
print(friends.count('Sara'))    # Fica: 1  -> conta quantas vezes aparece na lista

# Manipulacao de listas
friends = ['John','Michael','Terry','Eric','Graham']    # fica: ['John', 'Michael', 'Terry', 'Eric', 'Graham']
cars = [911,130,328,535,740,308]                        # fica: [911, 130, 328, 535, 740, 308]

friends.sort()              # comando para ordenar a lista em ordem ascendente --> A-Z ou menor num para maior        # fica: ['Eric', 'Graham', 'John', 'Michael', 'Terry']
friends.sort(reverse=True)  # comando para ordenar de forma decrescente         fica: ['Terry', 'Michael', 'John', 'Graham', 'Eric']
friends.reverse()           # comando para inverter a lista anterior            fica: ['Eric', 'Graham', 'John', 'Michael', 'Terry']
cars.reverse()              # exemplo com cars                                  fica: [308, 740, 535, 328, 130, 911]

print(min(cars))            # busca o valor minimo da lista cars        fica: 130
print(max(cars))            # busca o valor maximo da lista cars        fica: 911
print(sum(cars))            # soma todos os valores da lista cars       fica: 2952

print(min(friends))         # busca em ordem ascendente o menor valor do alfabeto       fica: Eric
print(max(friends))         # busca em ordem ascendente o maior valor do alfabeto       fica: Terry
