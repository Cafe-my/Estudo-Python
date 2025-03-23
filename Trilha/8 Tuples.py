# Tuples sao listas que sao imutaveis, sao processados mais rapidamente do que listas normais
friends = ['John','Michael','Terry','Eric','Graham']            # lista normal
friends_tuple = ('John','Michael','Terry','Eric','Graham')      # Tuple, representado por ()

# podemos analisar e indexar os elementos:
print(friends_tuple[2])     # fica: Terry
print(friends_tuple[2:4])   # fica: ('Terry', 'Eric')
print(len(friends_tuple))   # fica 5

# Mas nao podemos modificar: 
# print(friends_tuple.replace('John', 'Ali'))     # fica: AttributeError: 'tuple' object has no attribute 'replace'
# print(friends_tuple.sort())                     # fica: AttributeError: 'tuple' object has no attribute 'sort'  
# Outros exemplos que nao podemos usar: append / remove / pop

# Entao caso quisermos mudar o Tuple sera necessario criar um novo e inserir o antigo nele
# Recomenda-se usar o Tuple quando vc nao tem intencao de mudar os dados dele dpeois