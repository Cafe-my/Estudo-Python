print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
print('Ola vc esta na calculadora virtual!')
op = input('Escolha a operacao aqui. Escreva + para adicao, - para subtracao, * para multiplicacao, / para divisao e f para conversao de celsius para fahrenheit: ')
num1 = float(input('Me de o primeiro numero: '))
if op == 'f':
    print(f'O valor {num1} Celsius equivale a {num1*9/5 + 32} Fahrenheit')
else:
    num2 = float(input('Me de o segundo numero: '))

    if op == '+':
        print(f'A soma de {num1} e {num2} e igual a {num1 + num2}')
    elif op == '-':
        print(f'A subtracao de {num1} e {num2} e igual a {num1 - num2}')
    elif op == '*':
        print(f'A multiplicacao de {num1} e {num2} e igual a {num1 * num2}')
    elif op == '/':
        print(f'A divisao de {num1} e {num2} e igual a {num1 / num2}')
    else:
        print('Por favor digite uma das operacoes possiveis!')
