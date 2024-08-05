from datetime import date

'''Peça ao usuário para informar o ano de nascimento. Em seguida, 
calcule e imprima a idade atual'''

anoNascimento = int(input("Informe o ano em que nasceu: "))
today = date.today().year
idade = today - anoNascimento
print(f"Você nasceu em {anoNascimento} e tem/irá completar {idade} anos.")