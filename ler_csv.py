import csv

# Ler CSV
with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
    reader = csv.DictReader(arquivo)
    print("Dados do arquivo CSV:")
    for linha in reader:
        print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
