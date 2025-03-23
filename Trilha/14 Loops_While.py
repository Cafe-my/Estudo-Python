# Loops sao estruturas de repeticao que rodam um bloco de codigos repetidamente ate que algumas condicional o faca parar
# Python contem duas estruturas: for e while

# SINTAXE BASICA:
# while condition:      determina que o bloco de código sera executado ENQUANTO determinada condição for satisfeita.
#     code              bloco de codigo
#     iterator          iterador: é um objeto que permite percorrer uma coleção de elementos, como listas, arrays ou conjuntos, de forma sequencial. 

# Three Loop Questions:
#1. What do I want to repeat?
#2. What do I want to change each time?
#3. How long should we repeat?


i=0                                     # 1 - temos o iterador i que determinamos ser 0                       
while i < 5:                            # 2 - enquanto i for menor do que 5 (no momento e 0)                   5 - i recebera o valor 1 e o loop continuara pois 1 < 5
    print(f"{i}. Loops are awesome")    # 3 - rodara esse bloco de codigo                                      6 - o codigo sera executado novamente e
    i=i+1                               # 4 - no final o iterador i recebera seu antigo valor(0) + 1           7 - i recebera seu antigo valor(1) + 1   --> i = 2, entao loop o continuara
# 0. Loops are awesome
# 1. Loops are awesome
# 2. Loops are awesome
# 3. Loops are awesome
# 4. Loops are awesome

i=0                                     # i comecara do 0
while i < 5:                            # enquanto i for menor do que 5
    i+=1                                # mesmo significado de i = i + 1
    print(f"{i}. Loops are awesome")    # "1. Loops are awesome"  --> i = 1, entao loop continuara
# 1. Loops are awesome
# 2. Loops are awesome
# 3. Loops are awesome
# 4. Loops are awesome
# 5. Loops are awesome


# Uso do else com while: 
contador = 0

while contador < 10:                                                # enquanto contador for menor que 10
    contador += 1
    print(f'Valor do contador é {contador}')    
else:                                                               # senao, ou seja conatdor maior que 10 entao:
    print(f'Fim do while e o valor do contador é {contador}')