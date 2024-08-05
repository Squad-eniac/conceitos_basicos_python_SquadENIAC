'''Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros. '''

def converter_distancia(km):
    metros = km * 1000
    centimetros = km * 100000
    milimetros = km * 1000000

    print(f'\n{km} quilômetros é igual a: \n- {metros} metros \n -{centimetros} centímetros \n- {milimetros} milímetros')


print('--- Conversor de quilômetros para metros, centímetros e milímetros---')
try:
    km = float(input('\nPor favor, Digite a quantidade de quilômetros: '))

except ValueError:
    print('Erro, a entrada digitada é inválida! Por favor, digite um número válido')
    
else:
    converter_distancia(km)
