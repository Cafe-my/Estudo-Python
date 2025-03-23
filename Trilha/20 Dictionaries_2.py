# Juntando 2 ou mais dicionarios:
roupas = {'Camiseta': 20, 'Meia': 10}
elenco = {'Arthur': 40, 'Galahad': 35}
frutas = {'Banana': 3, 'Pera': 5}

people = {}
people1 = {}
people2 = {}

# metodo 1 - .update()
people.update(roupas)
people.update(elenco)
people.update(frutas)
print(people)                   # fica: {'Camiseta': 20, 'Meia': 10, 'Arthur': 40, 'Galahad': 35, 'Banana': 3, 'Pera': 5}

# metodo 2 - comprehension
for groups in (elenco, frutas, roupas): people1.update(groups)
print(people1)                  # fica: {'Arthur': 40, 'Galahad': 35, 'Banana': 3, 'Pera': 5, 'Camiseta': 20, 'Meia': 10}

# metodo 3 - unpacking (version3.5 later)
people2 = {**roupas,**frutas,**elenco}
print(people2)                  # fica: {'Camiseta': 20, 'Meia': 10, 'Banana': 3, 'Pera': 5, 'Arthur': 40, 'Galahad': 35}

# Usando unpacking na funcao:
# dicionario = {'argumento': 1}
# def funcao(parametro):          # definindo o "parametro"
#     print(parametro)            # o bloco de codigos sera o print do parametro que mostrara diferentes resulatdos de acordo com os dados que escolheremos a seguir para serem impressos:
# funcao(dicionario)              # entao o parametro recebera os dados do "dicionario" --> {'argumento': 1}
# funcao(**dicionario)            # entao o parametro recebera os dados do unpacking dicionario (valor) --> 1


# Criando dicionarios a partir de lista - dict.fromkeys(a,b)
chaves = ['chave1', 'chave2', 'chave3']
valor = 0
dicio = dict.fromkeys(chaves , valor)
print(dicio)


# O método dict.setdefault(): retorna o valor da chave especificada, e, caso a chave não exista, a cria com o valor especificado.
dicio = {'coleta': 'scrapy', 'dados': 200}
set_data = dicio.setdefault('data')
set_teste = dicio.setdefault('teste', 1)

print(set_data)                 # fica: None        / a chave data nao existe
print(set_teste)                # fica: 1           / a chave teste nao existe mas demos um valor default a ela "1" 
print(dicio)                    # fica: {'coleta': 'scrapy', 'dados': 200, 'data': None, 'teste': 1}        / ambas as chaves foram adicionadas ao dicio


# Copiando dicionario - .copy()
dicio = {"operacao": "web scraping", "dados": 250}
copia = dicio.copy()

