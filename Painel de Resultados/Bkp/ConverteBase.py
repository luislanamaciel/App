import pandas as pd

try:
 planilha1 = pd.read_excel(r'C:\Painel de Resultados\Bases\lj010424.xlsx')
 planilha2 = pd.read_excel(r'C:\Painel de Resultados\Bases\lj010524.xlsx')
 planilha3 = pd.read_excel(r'C:\Painel de Resultados\Bases\lj010624.xlsx')
 planilha4 = pd.read_excel(r'C:\Painel de Resultados\Bases\lj010724.xlsx')
 planilha5 = pd.read_excel(r'C:\Painel de Resultados\Bases\lj010824.xlsx')
 planilha6 = pd.read_excel(r'C:\Painel de Resultados\Bases\lj010924.xlsx')
 planilha7 = pd.read_excel(r'C:\Painel de Resultados\Bases\lj011024.xlsx')
except Exception as e:
    print("Erro ao carregar as planilhas:", e)


# Verifica e imprime o número de linhas de cada planilha
print(f"Linhas na planilha 1: {len(planilha1)}")
print(f"Linhas na planilha 2: {len(planilha2)}")
print(f"Linhas na planilha 3: {len(planilha3)}")
print(f"Linhas na planilha 4: {len(planilha4)}")
print(f"Linhas na planilha 5: {len(planilha5)}")
print(f"Linhas na planilha 6: {len(planilha6)}")
print(f"Linhas na planilha 7: {len(planilha7)}")
base1 = pd.concat([planilha1, planilha2,planilha3,planilha4,planilha5,planilha6,planilha7], ignore_index=True)
# Verifica o número total de linhas após a concatenação
total_linhas = len(base1)
print(f"Total de linhas combinadas: {total_linhas}")

base1.to_excel(r'C:\Painel de Resultados\Bases\base1.xlsx', index=False)