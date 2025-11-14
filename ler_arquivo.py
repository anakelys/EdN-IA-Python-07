# programa_1.py
# Lê um arquivo de log de tempos de execução e calcula a média e o desvio padrão

import math

def calcular_estatisticas(arquivo):
    tempos = []

    with open(arquivo, "r") as f:
        for linha in f:
            tempo = float(linha.strip())
            tempos.append(tempo)

    media = sum(tempos) / len(tempos)

    soma_quadrados = sum((t - media) ** 2 for t in tempos)
    desvio_padrao = math.sqrt(soma_quadrados / len(tempos))

    print("Média dos tempos:", round(media, 4))
    print("Desvio padrão:", round(desvio_padrao, 4))

arquivo = "logs.txt"
calcular_estatisticas(arquivo)
