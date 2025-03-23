import random

# Gera um numero aleatorio entre 0 e 1
print(random.random())  

# Retorna um numero decimal aleatorio entre o intervalo de dois numeros especificados (ambos incluidos)
print(random.uniform(1,6))

# Retorna um numero inteiro aleatorio entre o intervalo de dois numeros especificados (ambos incluidos)
print(random.randint(1,6))

# Retorna um numero inteiro aleatorio dentro de um intervalo (start, stop, step) (obrigatorio especificar o ponto stop, start e step opcionais) 
print(random.randrange(2,100,2))

# Uso do for in range(5) para gerar 5 numeros aleatorios
for i in range(5):
    print(random.random())


# RANDOM COM LISTA DE STR
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']

# Retorna um elemento aleatorio de uma lista
print(random.choice(friends_list))

# Retorna uma lista com um especifico numero de elementos aleatorios de uma sequencia (impossivel obter elementos duplicados)
print(random.sample(friends_list,3))

# Retorna uma lista com um especifico numero de elementos aleatorios de uma sequencia (pode-se obter elementos duplicados)
# random.choices(sequence, weights=None, cum_weights=None, k=1) -> com os parametros weights podemos estabelecer o peso da possibilidade de cada elemento ser escolhido / cum_weights : nao entendido
print(random.choices(friends_list, k=2))

mylist = ["apple", "banana", "cherry"]
print(random.choices(mylist, weights = [10, 1, 1], k=3))        # entao ha 10 vezes mais possibilidade de selecionar "apple" do que os outros dois

# Reorganiza os elementos de uma sequencia (modifica a lista original, nao retorna uma nova lista)
random.shuffle(friends_list)
print(friends_list)


# RANDOMNESS COM O MODULO STRING
import string
# a constante string.ascii_letters é uma string predefinida que contém todas as letras ASCII minúsculas e maiúsculas: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    # It is equivalent to the concatenation of string.ascii_lowercase and string.ascii_uppercase.
# a constante string.digits é uma string predefinida que contem todos os digitos de 0 a 9: 0123456789
letters_numbers = string.ascii_letters + string.digits      # fica: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

# gerando strings aleatorias da sequencia letters_numbers
word = ''
for i in range(7):
    word += random.choice(letters_numbers)              # usando for pode-se gerar string aleatorio com elementos duplicados

word1 = ''.join(random.sample(letters_numbers,7))       # usando a funcao join pode-se gerar string aleatorio sem elementos duplicados

# Ou apenas usar: word = random.choices(letter_numbers, k=7)