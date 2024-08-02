'''
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
'''

try:
    valor = float(input('Digite o valor que você ganha por hora: '))
    horas = float(input('Digite o número de horas trabalhadas no mês: '))
        
    if valor < 0 or horas < 0:
        raise ValueError("O valor por hora e as horas trabalhadas não podem ser negativos.")
        
    salario = valor * horas
    print(f'O seu salário no mês é: R$ {salario:.2f}')
        
except ValueError as e:
        print(f"Erro: {e}. Por favor, insira valores numéricos válidos.")