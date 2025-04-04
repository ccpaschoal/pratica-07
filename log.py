import re
import numpy as np

# Ler o arquivo de log
with open('log_treinamento.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# Encontrar tempos de execução (ex: "Tempo: 12.5 segundos")
tempos = []
for linha in linhas:
    match = re.search(r'Tempo:\s*(\d+\.?\d*)', linha)
    if match:
        tempos.append(float(match.group(1)))

# Calcular média e desvio padrão
media = np.mean(tempos)
desvio = np.std(tempos)

print(f"Média dos tempos: {media:.2f} segundos")
print(f"Desvio padrão dos tempos: {desvio:.2f} segundos")