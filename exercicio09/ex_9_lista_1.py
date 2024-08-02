''' Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício'''

def calculate_calories_burned():
    activity_hours_per_week = float(input('Insira o número de horas de atividade física \n que você faz por semana: '))
    calories_burned_per_week = (activity_hours_per_week * 60)*5
    print (f'Você queimou {(calories_burned_per_week * 4):.2f} calorias esse mês')

calculate_calories_burned()   