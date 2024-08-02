

def calcular_tempo_viagem():
    # Solicita a distância do percurso ao usuário
    distancia = float(input("Digite a distância do percurso em km: "))

    # Calcula o tempo de viagem para cada meio de transporte
    tempo_aviao = distancia / 600
    tempo_carro = distancia / 100
    tempo_onibus = distancia / 80

    # Exibe os tempos de viagem
    print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
    print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
    print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")

calcular_tempo_viagem()
