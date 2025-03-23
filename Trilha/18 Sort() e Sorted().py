# essas funcoes sao usadas para organizar os elementos de um conjunto
# funcao sort() -> nao retorna um nova lista, apenas sorteia
# funcao sorted() -> sorteia a lista e a retorna como uma nova lista

my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python' 

print(my_list,'original')       # [1, 5, 3, 7, 2] original
print(my_list.sort())           # None                          como ele nao retorna uma nova lista entao nao printavel
print(my_list,'new')            # [1, 2, 3, 5, 7] new           mas nota-se que apos a funcao a nossa lista foi mudada e organizada em ordem

print(my_list,'original')       # [1, 5, 3, 7, 2] original
print(my_list.reverse())        # None                          funcao reverse() -> usado para espelhar a lista
print(my_list,'new')            # [2, 7, 3, 5, 1] new

print(my_list,'original')       # [1, 5, 3, 7, 2] original
print(sorted(my_list))          # [1, 2, 3, 5, 7]               ele nos retorna uma nova lista (novo dado) entao printavel
print(my_list,'new')            # [1, 5, 3, 7, 2] new           portanto nota-se que apos a funcao a lista original nao sofreu mudanca

print(my_tuple,'original')      # ('d', 'c', 'e', 'a', 'b') original    
print(sorted(my_tuple))         # ['a', 'b', 'c', 'd', 'e']             nota-se que quando usamos sorted() para nos retornar uma novo tuple organizado, ele tranforma o tuple em uma lista
print(my_tuple,'new')           # ('d', 'c', 'e', 'a', 'b') new         atencao: tuple nao pode ser usado com sort()


# COM DICIONARIOS:
print(my_dict,'original')       # {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} original
print(sorted(my_dict))          # ['add', 'bee', 'car', 'dog']                          nota-se que sao organizados apenas os valores chave e os retorna uma lista
print(my_dict,'new')            # {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} new

print(sorted(my_dict.items()))  # [('add', 3), ('bee', 1), ('car', 4), ('dog', 2)]      usando .items() os elementos sao organizados pelos valores chave mas sao acompanhados por seus dados

print(sorted(my_dict.values())) # [1, 2, 3, 4]                                          usando .values() selecionamos apenas os dados para serem organizados e retornados


my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list, key = abs))                    # [1, -2, -3, 5, 7]         absolute: organiza mas ignora o sinal de menos ou mais

# lista de lista:
print(sorted(my_llist))                              # [['add', 3, 10], ['bee', 1, 24], ['car', 4, 65], ['dog', 2, 30]]          nota-se que foi organizado de acordo com os primeiros elementos da lista interna
print(sorted(my_llist, key = lambda item :item[1]))  # [['bee', 1, 24], ['dog', 2, 30], ['add', 3, 10], ['car', 4, 65]]          foi organizado de acordo com o segundo item da lista interna