# Tratamento de erros e exceções no Python com try/except -> Impede que o programa crashe rordando sempre o codigo
    # TRY e EXCEPT sao obrigatorias / ELSE e FINALLY sao opcionais:

# try: 
     # Bloco de código a ser executado

# except {exceção}:
     # Código que será executado caso a {exceção/erro} ocorra

# else:
     # Código que será executado caso nenhuma exceção/erro tenha sido capturada

# finally:
    # Código que sempre será executado independente se alguma exceção for capturada ou não


try:
    num = int(input('Enter a number: '))
    print(f"30 divided by {num}, is: {30/num}")
    print("**Thank you for playing!**")
# caso o valor de entrada para o input for diferente de um integer (bool, str,float), nos retorna o seguinte erro <ValueError>
# caso o valor de entrada para o input for o numero 0, nos retorna o seguinte erro <ZeroDivisionError>
except ValueError:
    print("Bad Value!")
    # entao podemos especificar o except para que rode apenas quando houver ValueError
except ZeroDivisionError as err:        # essa sintaxe permite evidenciar o erro
    print(f"{err} - You can't divide by Zero!!!")
    # especificando o erro ZeroDivisionError
except:
    print("Invalid Input!")
    # o except sozinho tambem pode ser usado mas executara qualquer outro tipo de erro (nao especificado)
# ATENCAO: os excepts sao capturados na sequencia de cima para baixo, entao caso um except seja capturado os outros nao serao e sera retornado um por vez


# Outra forma de capturar mutiplos erros:
    # except(ZeroDivisionError, ValueError):
    #     print("Erro de conversão ou divisor igual à zero")


# COM ELSE E FINALLY E USO DO RAISE
try:
    num=int(input('Enter a number between 1 and 30: '))
    num1 = 30/num
    if num > 30:
        raise ValueError(num)                   # (num) -> faz com que o numero 'num' se torne a excessao entao 'err' evidencia o numero (num) como erro
except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")
except ValueError as err:
    print(err, num, "Bad Value not between 1 and 30!")  # caso nao haja (num) la encima o err nao evidencia o erro
except:
    print("Invalid Input!")
else:
    print(f"30 divided by {num}, is: {30/num}")         # codigo que rodara caso nao tenha erro
finally:
    print("**Thank you for playing!**")
