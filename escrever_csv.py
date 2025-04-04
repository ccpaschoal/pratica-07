import csv

# Dados das pessoas
pessoas = [
    {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
    {"Nome": "João", "Idade": 35, "Cidade": "Rio de Janeiro"},
    {"Nome": "Maria", "Idade": 22, "Cidade": "Belo Horizonte"},
]

# Escrever em CSV
with open('pessoas.csv', 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.DictWriter(arquivo, fieldnames=["Nome", "Idade", "Cidade"])
    writer.writeheader()
    writer.writerows(pessoas)

print("Dados escritos com sucesso no arquivo pessoas.csv!")
