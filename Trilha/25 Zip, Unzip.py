nums = [1,2,3,4] 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

# COMANDO ZIP

# forma uma lista com tuples que combinam/relacionam os elementos que estao no mesmo indice
combo = list(zip(nums,letters))
    # fica: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# tambem podemos usar para formar dicionarios
combo = dict(zip(nums,letters))
    # fica: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# Combinando mais de 2 listas
combo = list(zip(nums,letters,names))
    # fica: [(1, 'a', 'John'), (2, 'b', 'Eric'), (3, 'c', 'Michael'), (4, 'd', 'Graham')]

print(combo)


# COMANDO UNZIP

# Uso do *, nota-se que divide em tuples e nao listas
num,let,nam = zip(*combo)
    # fica: (1, 2, 3, 4) ('a', 'b', 'c', 'd') ('John', 'Eric', 'Michael', 'Graham')

print(num,let,nam)


# USO EM DICIONARIOS

keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
# formando lista de palavras com split
keys = keys.split()
values = values.split()

# Usando zip para formar um dicionario
en_sv_dict = dict(zip(keys,values))
    # fica: {'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}

# descompactando o diconario em listas
en,sv = list(en_sv_dict.keys()),list(en_sv_dict.values())
    # fica: ['this', 'parrot', 'is', 'deceased'] ['denna', 'papegojan', 'är', 'avliden']

# descompanctando usando unzip
en1,sv1 = zip(*en_sv_dict.items())
    # fica: ('this', 'parrot', 'is', 'deceased') ('denna', 'papegojan', 'är', 'avliden')

# Dictionarie Comprehension: outro metodo p/ formar um dicionario
new_dict = {key:value for key,value in zip(keys,values)}
    # fica: {'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}