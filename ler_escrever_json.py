import json

# Dados da pessoa
pessoa = {
    "Nome": "Pedro",
    "Idade": 30,
    "Cidade": "Curitiba"
}

# Escrever JSON
with open('pessoa.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

print("Dados escritos com sucesso no arquivo pessoa.json!")

# Ler JSON
with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    print("\nDados lidos do arquivo JSON:")
    print(f"Nome: {dados['Nome']}, Idade: {dados['Idade']}, Cidade: {dados['Cidade']}")
