# Named notation: Ao inves de escrevermos um dado especifico ('27', 'brian', etc) que sera lido pelo parametro e impresso seguindo a regra do posicionamento, 
# podemos nomear os argumentos com os parametros referenciando cada um deles
def greeting(name, age=28, color="red"):
    print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
    print(f"We hear you like the color {color.lower()}!")

greeting(age=27, name="brian",color="Blue")     # Nota-se que nao esta na ordem, e cada dado recebeu seu parametro


# Funcao com Return: retornar valores através da palavra reservada return

def value_added_tax(amount):        # se na funcao nao inserirmos um comando que retorna um valor (print?)
    tax = amount * 0.25             # e charmarmos a funcao, ela nos retornara um objeto vazio

print(value_added_tax(100))         # fica: None


def value_added_tax(amount):        # amount recebe o argumento 20 e pedimos que retorne o valor da variavel tax
    tax = amount * 0.25             # entao quando 'chamamos' a funcao, sera impresso o que pedimos para retornar
    return tax                      
    
print(value_added_tax(20))          # fica: 5.0

    # Retornar multiplos dados
def soma_e_media(valor1):
    soma = valor1 + 10
    media = (valor1 + 10)/2
    return soma, media              # pede-se o retorno de dois valores                     

valores = soma_e_media(50)          # a variavel esta recebendo esses dois valores retornados pela funcao
print(valores)                      # fica: (60, 30.0)     --> nota-se que o type = tuple


def soma_e_media(valor1):
    soma = valor1 + 10
    media = (valor1 + 10)/2
    return f'{soma}, {media}'       # posso modificar o tipo do valor que estou retornando

valores = soma_e_media(50)          
print(valores, type(valores))       # fica: 60, 30.0 <class 'str'>                
