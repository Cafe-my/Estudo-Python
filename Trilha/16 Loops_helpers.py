# # BREAK: usado para parar a execucao do loop
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print(f'Found {friend}!')
        break                       
    print(friend)


# # CONTINUE: usado para pular todo o codigo que estiver abaixo dele dentro do bloco de codigos do loop, partindo para a proxima iteracao
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '!')
        continue                            # O codigo "print(friend)" nao sera executado, que no caso seria "Eric"
    print(friend)
# fica: John                  se nao houvesse continue: John
#       Terry                                           Terry
#       Found Eric!                                     Found Eric!
#       Michael                                         Eric
#       George                                          Michael
#                                                       George


# PASS: usamos o pass para dizer ao Python que o bloco de código está vazio
while False:
    pass        # sem o pass nao podemos estabelecer o while false vazio -> da erro

