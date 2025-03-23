def enigma():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[::-1]
# create two dictionaries: one for encoding, one for decoding
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))
# user input 'the message' and mode of machine
    msg = input('Enter your secret message quietly: ').lower()
    mode = input('Crypto mode: encode (e) OR decrypt as default: ')
# run encode or decode
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg])        # para cada caractere 'letter' in msg -> atribuimos ele como key para o dicio dict_e -> para voltar a lista de values dessas keys -> join para formar str
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg])
# return result
    return new_msg
# clean and beautify the code 

print(enigma())