msg = 'My name is Michele and I have 22yo!'

# Podemos adicionar, multiplicar strings
print(msg+msg)      # ficando: My name is Michele and I have 22yo!My name is Michele and I have 22yo!
print(msg*2)        # ficando: My name is Michele and I have 22yo!My name is Michele and I have 22yo!
print(msg,msg)      # ficando: My name is Michele and I have 22yo! My name is Michele and I have 22yo!

# Podemos modificar strings:
print(msg.upper())      # ficando: MY NAME IS MICHELE AND I HAVE 22YO!
print(msg.lower())      # ficando: my name is michele and i have 22yo!
print(msg.capitalize()) # ficando: My name is michele and i have 22yo!
print(msg.title())      # ficando: My Name Is Michele And I Have 22Yo!
print(msg.strip())      # remove os espacos inuteis no inicio e final da frase


# Podemos analisar strings:
print(len(msg))                                 # Length: conta quantidade de caracteres da frase                       (35)
print(msg.count('Michele'), msg.count('a'))     # Conta a quantidade de vezes que determ. elemento aparece no texto     (1 3)

# Slicing (enumeracao de caracteres em str comeca do 0)
print(msg[0], msg[4], msg[-1], msg[-3])     # Atencao ao uso de [] e uso do - implica na contagem a partir do ultimo caractere      (M a ! y)
print(msg[3:])                              # Pega pedaco a partir do 3 caractere ate o fim                                         (name is Michele and I have 22yo!)
print(msg[3:9])                             # Pega a partir do 3 caractere ate o 9, mas nao inclui o 9 caractere                    (name i)

print(msg.find('Michele'))                  # Indicca em qual numero comecou o determ. elemento                                     (11)
print('Michele' in msg, 'michele' in msg, 'michele' not in msg)     # Indica se existe o elemento na frase determinada, se sim True, se nao False           (True False True)       
print(msg.replace('Michele','Enzo'))        # ficando: My name is Enzo and I have 22yo!
print(msg[::-1])                            # Truque para espelhar a string                                                         (!oy22 evah I dna elehciM si eman yM)

# Multiplas linhas no Python
msg="""Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(msg)
