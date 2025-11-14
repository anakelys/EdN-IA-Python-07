import json

dados = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "Rio de Janeiro"
}


with open("pessoa.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

print("Arquivo JSON criado!")

with open("pessoa.json", "r") as arquivo:
    conteudo = json.load(arquivo)

print("Dados no arquivo JSON:")
print(conteudo)
