'''Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.'''

def soma(a, b, c):
    return a + b + c

num1 = float(input('Digite o primeiro número a ser somado: '))
num2 = float(input('Digite o segundo número a ser somado: '))
num3 = float(input('Digite o terceiro número a ser somado: '))

print(f'A soma dos três argumentos é: {soma(a=num1, b=num2, c=num3)}')