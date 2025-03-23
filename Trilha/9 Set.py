# Set e representado por {}, com processamento bem mais rapido que uma lista normal
# Ele e desordenado entao podem aparecer em uma ordem diferente cada vez que você os utiliza
# E nao registra o mesmo elemento mais de 1 vez na lista

fruts = {'banana', 'kiwi', 'morango', 'pera', 'kiwi', 'morango'}   # fica: {'pera', 'banana', 'morango', 'kiwi'}       removeu o kiwi e o morango, e apareceu desordenado

# Add novos itens:
convidados = {'Pedro', 'Maria', 'Eduarda'}
convidados.add('Michele')                   # adiciona o elemento Michele ao set        fica: {'Michele', 'Eduarda', 'Pedro', 'Maria'}

novos_convidados = {'Eduarda', 'Gustavo', 'Lisa'}
convidados.update(novos_convidados)         # add itens de outro conj. ao set           fica: {'Pedro', 'Gustavo', 'Lisa', 'Michele', 'Maria', 'Eduarda'}


# Removendo itens:
convidados.remove('Lisa')                   # fica: {'Gustavo', 'Pedro', 'Michele', 'Eduarda', 'Maria'}
convidados.discard('Michele')               # fica: {'Eduarda', 'Maria', 'Gustavo', 'Pedro'}


# Intersecao
fila1 = {'Titi', 'Lana', 'Dom'}
fila2 = {'Kiko', 'Lana', 'Victor', 'Titi'}

u_fila = fila1.intersection(fila2)          # retorna um novo conjunto contendo apenas os itens presentes em ambos      fica: {'Titi', 'Lana'}
print(fila1 & fila2)                        # mesmo resultado                                                           fica: {'Lana', 'Titi'}

fila2.intersection_update(fila1)            # atualiza a fila2 com a intersecao entre fila1 e fila2         entao fila2 fica: {'Titi', 'Lana'}


# Uniao
set1 = {1, 2, 3}
set2 = {'z', 'x', 'a'}

print(set1.union(set2))                     # une os dois sets                                                          fica: {1, 2, 3, 'z', 'x', 'a'}
print(set1 | set2)                          # mesmo resultado

# Diferenca
animais1 = {'Gato', 'Tigre', 'Leao', 'Galo'}
animais2 = {'Galo', 'Sapo', 'Gato'}

print(animais1.difference(animais2))        # retorna os elementos que estao presentes no animais1 e nao no animais2    fica: {'Leao', 'Tigre'}
print(animais1 - animais2)                  # mesmo resultado

print(animais1.symmetric_difference(animais2))  # retorna a diferenca de ambos os sets                                  fica: {'Leao', 'Sapo', 'Tigre'}           
print(animais1 ^ animais2)                      # mesmo resultado

animais1.symmetric_difference_update(animais2)  # retorna dentro do animais a diferenca de ambos os sets, modificando-o 
print(animais1)                                 # fica: {'Tigre', 'Sapo', 'Leao'}
animais1 ^= animais2                            # mesmo resultado
print(animais1)


# Declarando Sets
empty_list = []
empyt_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}          # Forma errada, isso e um dicionario
empty_set = set()
