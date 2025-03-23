# PERMITE A CRIACAO DE FUNCOES ANONIMAS (SEM NOME)
# QUANDO SE TEM A INTENCAO DE USAR A FUNCAO APENAS UMA VEZ

# SINTAXE BASICA
# lambda {argumentos}: {expressão}
    # argumentos: dados de entrada que a funcao vai receber
    # expressao: codigo que sera executado

# Ele pode ser chamado diratamente ou ser armazenada numa variavel
soma = lambda x, y: x + y
print(soma(2, 3))

print((lambda x, y: x + y)(2, 3))

# USANDO FUNCAO LAMBDA DENTRO DE OUTRA FUNCAO
def func(n):
    return lambda a: a*n

doubler = func(2)       # A variavel doubler esta recebendo a funcao lambda dentro da funcao 'func' que recebeu o valor (2)
print(doubler(3))       # entao devemos chamar doubler atribuindo um valor que entrara como argumento para 'a' da funcao lambda

print(func(2)(3))       # podemos simplificar chamando a funcao def mas ja atribuindo os valores para 'n' e 'a'


# FUNCAO MAP: fornece uma maneira de aplicar uma função a todos os itens em um iterável, um de cada vez.
    # map(lambda item: item[] expression, iterable)
lista = [1, 2, 3, 4]
print(list(map(lambda x: x ** 2, lista)))
    # fica: [1, 4, 9, 16]

# FUNCAO FILTER: filtra elementos de uma sequência com base em uma condição
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, lista)))
    # fica: [2, 4, 6, 8, 10]