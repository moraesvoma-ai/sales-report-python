import csv

total_faturamento = 0
vendas_produtos = {}

with open("vendas.csv", newline='', encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        produto = linha["produto"]
        quantidade = int(linha["quantidade"])
        preco = float(linha["preco_unitario"])

        total_faturamento += quantidade * preco

        if produto not in vendas_produtos:
            vendas_produtos[produto] = 0

        vendas_produtos[produto] += quantidade

print("Faturamento total:", total_faturamento)
print("Vendas por produto:", vendas_produtos)
