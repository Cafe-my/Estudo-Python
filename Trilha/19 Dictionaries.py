# modelo basico:
# variable = {'key': 'value'}
    # key serve para indexar no dicionario
    # value recebe valores de diversos tipos: listas, outros dicionários, inteiros, strings e etc.

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael']
}
print(movie)                                # fica: {'title': 'Life of Brian', 'year': 1979, 'cast': ['John', 'Eric', 'Michael']}

# Acessando itens do dict:

print(movie['title'])                       # fica: Life of Brian       se tentar acessar uma chave inexistente no dict ocasiorana em erro
print(movie.get('title'))                   # fica: Life of Brian
print(movie.get('budget'))                  # fica: None                se tentar acessar uma chave inexistente com get ocasionara em "None"

    # você pode definir um valor default, para o caso da chave não ser encontrada
print(movie.get('budget','Not found'))      # fica: Not found


# Atualizando e Adicionando itens:

movie['title'] = 'The Holy Grail'           # Atualizando title no dict
print(movie.get('title'))                   # fica: The Holy Grail
movie['budget'] = 250000                    # Adicionando budget no dict
print(movie)                                # fica: {'title': 'The Holy Grail', 'year': 1979, 'cast': ['John', 'Eric', 'Michael'], 'budget': 250000}

movie.update({'title' : 'Imortal',                                  # Modificando/Atualizando todo o dicionario com update()
              'year': 2001, 
              'cast': ['John','Eric','Michael','George','Terry'], 
              'budget': 300000})   
print(movie)                                # fica: {'title': 'Imortal', 'year': 2001, 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry'], 'budget': 300000}

movie.update({'age':18})                    # Apenas adicionando no dict com update()    
print(movie.get('age'))                     # fica: 18


# Excluindo elementos: 

del movie['cast']
print(movie)                                # fica: {'title': 'Imortal', 'year': 2001, 'budget': 300000, 'age': 18}


# Excluindo elementos do dict e retornando ele - .pop() / excluindo e retornando o ultimo elemento - .popitem()

year1 = movie.pop('year')                   # pop() exclui o elemento year do dict e retornou seu valor na variavel year1
print(movie)                                # fica: {'title': 'Imortal', 'budget': 300000, 'age': 18}                       nota-se que a chave year e seu valor foram removidos do dict
print(year1)                                # fica: 2001

ages = movie.popitem()                      # popitem() exclui o ultimo elemento do dict e retorna (chave e valor)
print(movie)                                # fica: {'title': 'Imortal', 'budget': 300000}
print(ages)                                 # fica: ('age', 18)


# Obtendo chave e valores:

print(movie.keys())                         # fica: dict_keys(['title', 'budget'])
print(movie.values())                       # fica: dict_values(['Imortal', 300000])
print(movie.items())                        # fica: dict_items([('title', 'Imortal'), ('budget', 300000)])


# Percorrendo dict com for:

for key, value in movie.items():            # fica: title e Imortal
    print(f'{key} e {value}')               #       budget e 300000
