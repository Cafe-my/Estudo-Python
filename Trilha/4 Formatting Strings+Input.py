name = 'Michele Ye'
print('My name is ' + name + '. Nice to meet you!')
print(f'My name is {name}. Nice to meet you!')          # Forma mais clean de escrever msm resultado

# usando uma datatype
num1 = 2
print(f'Number: {float(num1)}')     # fica: Number: 2.0
# modificando a str
a = 'hello world'
print(f'I say: {a.upper()}')        # fica: I say: HELLO WORLD    


# Uso do Input (inserir um dado):
num1 = int(input('Give me a integer number: '))                                     # Colocando: 4
num2 = int(input('Give me another: '))                                              # Colocando: 3
add = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
print(f'Adicao: {add}, Subtracao: {sub}, Divisao: {div}, Multiplicacao: {mult} ')   # Adicao: 7, Subtracao: 1, Divisao: 1.3333333333333333, Multiplicacao: 12
# Podemos diminuir a "Divisao: 1.3333333333333333"
print(f'Adicao: {add}, Subtracao: {sub}, Divisao: {div:.2f}, Multiplicacao: {mult} ')   # :.2f --> Adicao: 7, Subtracao: 1, Divisao: 1.33, Multiplicacao: 12


# Quebra de Linha e Juncao de Linha:
print('Ola! Tudo \nbem?')
        # Ficara assim: Ola! Tudo
                      # bem?
print(f'Meu nome e {name}! Tenho 22 anos! ', end='')    # ficara assim: Meu nome e Michele Ye! Tenho 22 anos! Prazer em te conhecer!
print('Prazer em te conhecer!')
