# comando list()
print(list('Ola mundo!'))           # fica: ['O', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o', '!']



# .split(): reconhece os espaços nas strings e realiza a divisão nesses lugares gerando tecnicamente uma lista de palavras
msg = 'Ola, seja muito bem vindo, aprenda!'
print(msg.split())                  # fica: ['Ola,', 'seja', 'muito', 'bem', 'vindo,', 'aprenda!']

# podemos escolher onde que queremos dividir:
print(msg.split(','))               # fica: ['Ola', ' seja muito bem vindo', ' aprenda!']



# ''.join(): adiciona o elemento que esta entre as '' entre cada numeracao e nos volta uma string
lista = ['Eric','John','Michael','Terry','Graham']

# numa string cada caractere tem numeracao
print('-'.join(msg))                # fica: O-l-a-,- -s-e-j-a- -m-u-i-t-o- -b-e-m- -v-i-n-d-o-,- -a-p-r-e-n-d-a-!

# numa lista cada elemento tem numeracao
print('|'.join(lista))              # fica: Eric|John|Michael|Terry|Graham
print('|'.join(lista + lista))      # fica: Eric|John|Michael|Terry|Graham|Eric|John|Michael|Terry|Graham



# Entao podemos tranformar uma string --split--> lista --join--> string
print('-'.join(msg.split()))        # fica: Ola,-seja-muito-bem-vindo,-aprenda!