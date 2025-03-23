# Os arquivos podem conter uma variedade de informações, como texto, dados estruturados, imagens, entre outros.
# Ao abrir e ler esses arquivos, podemos realizar diversas tarefas, como extrair informações, processar dados e até mesmo criar novos arquivos.

# ABRINDO ARQUIVOS - open()
arquivo = open("D:\Michele Ye\CC\Estudo Python/21.1 Greeting.txt", 'r') # --> dois parametros: nome do arquivo e modo de abertura do arquivo
# MODOS:
# 'r': modo de leitura, o arquivo deve existir previamente
# 'w': modo de escrita, se o arquivo não existir, ele será criado
# 'a': modo de anexar, adiciona informações ao final do arquivo
# 'x': modo exclusivo, cria um novo arquivo somente se ele não existir
# 'b': modo binário, usado para arquivos binários, como imagens ou vídeos
# 't': modo de texto, usado para arquivos de texto


# LENDO ARQUIVOS:
conteudo = arquivo.read()       # retorna todo o conteúdo do arquivo como uma string.
print(conteudo)

# print(arquivo.read(10))         # especificando quantos caracteres queremos ler

# print(arquivo.readline())       # ler o arquivo linha por linha e a cada chamada do método readline(), uma nova linha do arquivo é lida em sequencia

# line_by_line = arquivo.readlines()  # ler o arquivo e retorna ele todo mas com cada linha separada
# print(line_by_line)
# line_by_line1 = arquivo.read().splitlines()   # faz a mesma funcao mas acredito que seja melhor
# print(line_by_line1)


# ESCREVENDO EM ARQUIVOS:
# arquivo = open("D:\Michele Ye\CC\Estudo Python/21.1 Greeting.txt", 'w')     # atencao o arquivo foi aberto no modo 'w'
# arquivo.write('Olá, Mundo!')


# FECHANDO O ARQUIVO:
    # É importante fechar o arquivo depois de terminar de escrever para liberar os recursos do sistema operacional.
# arquivo.close()


# MANIPULANDO ARQUIVOS COM STATEMENT WITH
    # Dispensa o uso do .close() para fechar o arquivo
with open('Estudo Python/21.2 Friends.csv', 'r') as f:
    # print(f.read())
    #     # fica:   John, 1939
    #     #         Eric, 1943
    #     #         Michael, 1943
    #     #         Graham, 1941
    #     #         TerryG, 1940
    #     #         TerryJ, 1942

    friends = f.read().splitlines()
    # print(friends)              # fica: ['John, 1939', 'Eric, 1943', 'Michael, 1943', 'Graham, 1941', 'TerryG, 1940', 'TerryJ, 1942']

    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 2030 {name} will be {2030 -year} years old')
            # fica: In 2030 John will be 91 years old
            #       In 2030 Eric will be 87 years old
            #       In 2030 Michael will be 87 years old
            #       In 2030 Graham will be 89 years old
            #       In 2030 TerryG will be 90 years old
            #       In 2030 TerryJ will be 88 years old

# arquivo csv: Um arquivo CSV (Comma-Separated Values) é um arquivo de texto que armazena dados em linhas e colunas, separados por vírgulas.