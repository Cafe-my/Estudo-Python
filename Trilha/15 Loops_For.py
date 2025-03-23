# FOR é utilizado para percorrer ou iterar sobre uma sequência de dados, executando um conjunto de instruções em cada item.

# Sintaxe básica: for <nome variável> in <iterável>
    # <nome variável> é o nome da variável que vai receber os elemento de <iterável>.
    # <iterável> é o container de dados sobre o qual vamos iterar, podendo ser: uma lista, uma tupla, uma string, um dicionário, entre outros.

lista = [1, 2, 3, 4, 5]

for item in lista:          # for ira percorrer por cada elemento da lista (iteracao), em cada iteracao a variavel <item> ira receber o valor do elemento correspondente da lista 
    print(item)             # entao na primeira iteracao item recebeu 1 e sera printado, na segunda iteracao item recebeu 2 e sera printado e assim por diante
# fica: 1
#       2
#       3
#       4
#       5


# Percorrendo strings:
for letter in 'Blue':
    print(letter)
# fica: B
#       l
#       u
#       e


# Uso do range:
for a in range(8):          # Range funciona como uma faixa de distancia        no exemplo: distancia do 0 ao 8 (proprio 8 nao incluso), portanto tera 8 iteracoes 
    print(a)                # Podemos especificar esse intervalo: range(2,8) -> distancia do 2 ao 8 (8 nao incluso), range(2,12,2) -> distancia do 2 ao 12 de 2 em 2
# fica: 0
#       1
#       2
#       3
#       4
#       5
#       6
#       7                   nota-se que o 8 nao esta, porque o ultimo elemento nao e incluso

# For dentro de For
friends = ['John','Terry','Eric']
for friend in friends:              # Iteracao 1 friend recebera o elemento John
    for number in [1,2,3]:          # esse bloco de codigos sera executado em sequencia antes de irmos para a iteracao 2 de friends
        print(friend, number)       # entao number recebera 1, sera printado John 1
                                    # em seguida number recebera 2, sera printado John 2
                                    # em seguida number recevera 3, sera printado John 3 e aqui terminaremos de percorrer (for number)
                                    # Comeca iteracao 2 friend recerbera o elemento Terry e o bloco de codigos abaixo sera executado novamente. Acontecera a mesma coisa com "Eric"
# fica: John 1
#       John 2
#       John 3
#       Terry 1
#       Terry 2
#       Terry 3
#       Eric 1
#       Eric 2
#       Eric 3


# Uso do enumerate():
computador = ['Processador', 'Teclado', 'Mouse']
for  indice, valor in enumerate(computador):         # indice e valor sao variaveis que receberao elementos:
    print(f"Índice={indice} | Valor={valor}")           # indice recebe o index de cada elemento da lista, possibilitado pela funcao enumerate()
                                                        # valor recebe o elemento em si da lista