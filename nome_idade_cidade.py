import csv

with open("dados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    
    escritor.writerow(["Nome", "Idade", "Cidade"])
    escritor.writerow(["Ana", 30, "Rio de Janeiro"])
    escritor.writerow(["Carlos", 25, "São Paulo"])
    escritor.writerow(["Mariana", 22, "Belo Horizonte"])

print("Arquivo CSV criado com sucesso!")
