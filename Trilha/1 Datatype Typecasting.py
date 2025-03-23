print('ola mundo')

# Comando para exibir o Datatype:
print(type('hello'))    # fica: <class 'str'>
print(type(1))          # fica: <class 'int'>
print(type(1.64))       # fica: <class 'float'>
print(type(True))       # fica: <class 'bool'>

variavel_4 = type(5)    # aplicando em variavel
print(variavel_4)       # fica: <class 'int'>


# Datatypes:
Integer = "Atribui propriedade de numero inteiro: int()"
Float = 'Atribui propriedade de numero decimal: float()'
Boolean = 'Atribui propriedade de True e False: bool()'
String = 'Atribui propriedade de mensagem/texto: str()'


# Como aplicar os Datatypes e praticar Typecasting (mudar o type)?
variavel_1 = 2 
print('Tenho um inteiro: ' + str(variavel_1))        # atencao se eu nao mudar o tipo dele de integer -> string da erro, pois nao posso juntar msg '+' numero 
print('tenho um inteiro:', variavel_1)               # com virgula poderia

# posso add datatype direto na variavel tbm
variavel_2 = str(2)                
variavel_3 = float(2)
print([variavel_2 , variavel_3])    # fica: ['2', 2.0]


a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'
print([a,b,c,d,e,f,g,h,i,j])   

# se tivermos c1 = int("3.4")       c1 nao poderia tranformar str em int, seria necessario: tranformar str -> float -> int
c1 = int(float("3.4"))              # c1 will be 3
