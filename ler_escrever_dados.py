# programa_4.py
# Lê e escreve dados em JSON

import json

dados = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "Rio de Janeiro"
}

# Salvando em JSON
with open("pessoa.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

print("Arquivo JSON criado!")

# Lendo JSON
with open("pessoa.json", "r") as arquivo:
    conteudo = json.load(arquivo)

print("Dados no arquivo JSON:")
print(conteudo)
