import matplotlib.pyplot as plt
import numpy as np

# Função que define a posição do objeto ao longo do tempo em MRU
def posicao_instantanea(velocidade, tempo, posicao_inicial=0):
    return posicao_inicial + velocidade * tempo

# Parâmetros do movimento
velocidade = 5  # Velocidade constante em metros por segundo
tempo_total = 10  # Tempo total da simulação em segundos
posicao_inicial = 0  # Posição inicial do objeto em metros

# Geração dos dados de tempo
tempos = np.linspace(0, tempo_total, num=100)  # 100 pontos de tempo entre 0 e tempo_total

# Cálculo da posição para cada instante de tempo
posicoes = posicao_instantanea(velocidade, tempos, posicao_inicial)

# Plotando o gráfico da posição ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(tempos, posicoes, label=f'v = {velocidade} m/s')
plt.title('Movimento Retilíneo Uniforme (MRU)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid(True)
plt.legend()
plt.show()
