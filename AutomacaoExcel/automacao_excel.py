import pandas as pd

# Lê a planilha
df = pd.read_excel("vendas.xlsx")

# Soma todos os valores da coluna "Valor"
total = df["Valor"].sum()

# Mostra o total no terminal
print(f"Total de vendas: R${total:.2f}")

# Cria uma nova planilha com o total
resumo = pd.DataFrame({"Total de Vendas": [total]})
resumo.to_excel("resumo_vendas.xlsx", index=False)
