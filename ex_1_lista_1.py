#Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f'A soma é igual a: {soma}')
print(f'A subtracao é igual a: {subtracao}')
print(f'A multiplicacao é igual a: {multiplicacao}')
print(f'A divisao é igual a: {divisao:.2f}')