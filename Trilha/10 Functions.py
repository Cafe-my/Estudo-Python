# Para que utilizamos funcoes:
# Reutilizar o código, evitando repetições desnecessárias em um programa

# Como definimos uma funcao? 
def nome():                     # iniciamos com 'def', atribuimos um 'nome' a ela e entre os () definimos os dados de entrada da funcao, chamamos de parametros (semelhante a variavel)
    print('Bloco de codigo')    # aqui temos o bloco de codigo a ser executado pela funcao (definido pelo recuo)

nome()                          # para que o bloco de codigos seja executado precisamos 'chamar' a funcao utilizando seu nome        fica: Bloco de codigo


# Especificando parametros:
def imprime_nome(nome):         # 1 estabelecemos o parametro 'nome'
    print(f"Nome: {nome}")      # 3 aqui o parametro que recebeu um determinado argumento sera impresso

imprime_nome("Erickson")        # 2 entre () inserimos argumentos = dados de entrada que serao recebidos la no parametro e serao impressos dentro do bloco de codigos
imprime_nome("Renan")           # 4 se chamarmos a funcao outra vez o bloco de codigos sera executado outra vez so que com o novo dado "Renan"
imprime_nome("Daniel")
# fica: Nome: Erickson
#       Nome: Renan
#       Nome: Daniel


# Se nao inserirmos o argumento ocorre ERRO
def imprime_nome(nome):
    print(f"Nome: {nome}")
    
imprime_nome()                  


# Se nao inserirmos um argumento mas determinarmos Valores Padrao ao parametro:
def flor(flor='Rosa', cor='Vermelha'):
    print(f"A cor da {flor} é {cor}")

flor()                                      # fica: A cor da Rosa é Vermelha


# Funcao Posicional
def greeting(name, age):                    # Temos mais de um parametro, o argumento recebido por eles esta pararelo ao posicionamento dos argumentos
    print(f"Hello {name}, you are {age}!")
    
greeting("Brian","32")                      # fica: Hello Brian, you are 32!


# Extra: Paremetro com valores padrao, argumento definido seguido de argumentos nao definidos
def greeting(name,age="28"):
    print(f"Hello {name}, you are {age}!")
    
greeting("Brian","32")                      # fica: Hello Brian, you are 32!
greeting("Judith")                          # fica: Hello Judith, you are 28!


# Extra: uso do input
def greeting(name,age):
    print(f"Hello {name}, you are {age}!")

name = input("Enter your name: ")    
greeting(name,"32")                         # fica: Hello Michele, you are 32!


