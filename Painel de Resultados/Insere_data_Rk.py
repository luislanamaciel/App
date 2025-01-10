import pandas as pd



#file_path4 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_04_2024.xlsx'
#file_path5 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_05_2024.xlsx'
#file_path6 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_06_2024.xlsx'
#file_path7 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_07_2024.xlsx'
#file_path8 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_08_2024.xlsx'
#file_path9 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_09_2024.xlsx'
#file_path10 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_10_2024.xlsx'
file_path11 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_11_2024.xlsx'

try:
    #df4 = pd.read_excel(file_path4, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df5 = pd.read_excel(file_path5, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df6 = pd.read_excel(file_path6, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df7 = pd.read_excel(file_path7, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df8 = pd.read_excel(file_path8, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df9 = pd.read_excel(file_path9, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df10 = pd.read_excel(file_path10, engine='openpyxl')  # Especifica o engine 'openpyxl'
    df11 = pd.read_excel(file_path11, engine='openpyxl')  # Especifica o engine 'openpyxl'
    
    
    
    
    
    
    
    
    print("Arquivo carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")




# #print(df4.head())
##df4.loc[:, 'mes_resumido'] = 'Abr'
##df4.loc[:,'mes']='Abril'
##df4.loc[:,'mes_num']='4'
##df4.loc[:,'ano']='2024'
##print(df4.head())

# #print(df6.head())
##df5.loc[:, 'mes_resumido'] = 'Mai'
##df5.loc[:,'mes']='Maio'
##df5.loc[:,'mes_num']='5'
##df5.loc[:,'ano']='2024'
##print(df5.head())


##df6.loc[:, 'mes_resumido'] = 'Jun'
##df6.loc[:,'mes']='Junho'
##df6.loc[:,'mes_num']='6'
##df6.loc[:,'ano']='2024'
##print(df6.head())

##df7.loc[:, 'mes_resumido'] = 'Jul'
##df7.loc[:,'mes']='Julho'
##df7.loc[:,'mes_num']='7'
##df7.loc[:,'ano']='2024'
##print(df7.head())

##df8.loc[:, 'mes_resumido'] = 'Ago'
##df8.loc[:,'mes']='Agosto'
##df8.loc[:,'mes_num']='8'
##df8.loc[:,'ano']='2024'
##print(df8.head())

##df9.loc[:, 'mes_resumido'] = 'Set'
##df9.loc[:,'mes']='Setembro'
##df9.loc[:,'mes_num']='9'
##df9.loc[:,'ano']='2024'
##print(df9.head())

##df10.loc[:, 'mes_resumido'] = 'Out'
##df10.loc[:,'mes']='Outubro'
##df10.loc[:,'mes_num']='10'
##df10.loc[:,'ano']='2024'
#print(df10.head())


df11.loc[:, 'mes_resumido'] = 'Nov'
df11.loc[:,'mes']='Novembro'
df11.loc[:,'mes_num']='11'
df11.loc[:,'ano']='2024'
print(df11.head())









# Salvar o DataFrame modificado de volta no Excel
#output_path4 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_04_2024.xlsx'  # Caminho para salvar o novo arquivo
#output_path5 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_05_2024.xlsx'  # Caminho para salvar o novo arquivo
#output_path6 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_06_2024.xlsx'  # Caminho para salvar o novo arquivo
#output_path7 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_07_2024.xlsx'  # Caminho para salvar o novo arquivo
#output_path8 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_08_2024.xlsx'  # Caminho para salvar o novo arquivo
#output_path9 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_09_2024.xlsx'  # Caminho para salvar o novo arquivo
#output_path10 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_10_2024.xlsx'  # Caminho para salvar o novo arquivo
output_path11 = 'C:/Painel de Resultados/Bases/Ranking/Rk_Lj01_11_2024.xlsx'  # Caminho para salvar o novo arquivo













try:
#     df4.to_excel(output_path4, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
#     df5.to_excel(output_path5, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
#     df6.to_excel(output_path6, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
#     df7.to_excel(output_path7, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
#     df8.to_excel(output_path8, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
#     df9.to_excel(output_path9, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
#     df10.to_excel(output_path10, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     df11.to_excel(output_path11, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     
    
    
    
    
    
    
    
    
     #print(f"Arquivo salvo com sucesso em: {output_path4}")
     #print(f"Arquivo salvo com sucesso em: {output_path5}")
     #print(f"Arquivo salvo com sucesso em: {output_path6}")
     #print(f"Arquivo salvo com sucesso em: {output_path7}")
     #print(f"Arquivo salvo com sucesso em: {output_path8}")
     #print(f"Arquivo salvo com sucesso em: {output_path9}")
     #print(f"Arquivo salvo com sucesso em: {output_path10}")
     
    
    
    
    
    
    
    
    
    
    
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")


#Cria um unico arquivo
try:
 planilha1 = pd.read_excel(r'C:\Painel de Resultados\Bases\Ranking\Rk_Lj01_04_2024.xlsx')
 planilha2 = pd.read_excel(r'C:\Painel de Resultados\Bases\Ranking\Rk_Lj01_05_2024.xlsx')
 planilha3 = pd.read_excel(r'C:\Painel de Resultados\Bases\Ranking\Rk_Lj01_06_2024.xlsx')
 planilha4 = pd.read_excel(r'C:\Painel de Resultados\Bases\Ranking\Rk_Lj01_07_2024.xlsx')
 planilha5 = pd.read_excel(r'C:\Painel de Resultados\Bases\Ranking\Rk_Lj01_08_2024.xlsx')
 planilha6 = pd.read_excel(r'C:\Painel de Resultados\Bases\Ranking\Rk_Lj01_09_2024.xlsx')
 planilha7 = pd.read_excel(r'C:\Painel de Resultados\Bases\Ranking\Rk_Lj01_10_2024.xlsx')
 planilha8 = pd.read_excel(r'C:\Painel de Resultados\Bases\Ranking\Rk_Lj01_11_2024.xlsx')
except Exception as e:
    print("Erro ao carregar as planilhas:", e)

else:
# Verifica e imprime o número de linhas de cada planilha
 print(f"Linhas na planilha 1: {len(planilha1)}")
 print(f"Linhas na planilha 2: {len(planilha2)}")
 print(f"Linhas na planilha 3: {len(planilha3)}")
 print(f"Linhas na planilha 4: {len(planilha4)}")
 print(f"Linhas na planilha 5: {len(planilha5)}")
 print(f"Linhas na planilha 6: {len(planilha6)}")
 print(f"Linhas na planilha 7: {len(planilha7)}")
 print(f"Linhas na planilha 7: {len(planilha8)}")
 
baseRk01 = pd.concat([planilha1, planilha2,planilha3,planilha4,planilha5,planilha6,planilha7,planilha8], ignore_index=True)

# Verifica o número total de linhas após a concatenação
total_linhas = len(baseRk01)
print(f"Total de linhas combinadas: {total_linhas}")

# Tenta salvar a planilha final
try:
   baseRk01.to_excel(r'C:\Painel de Resultados\Bases\Ranking\baseRk01.xlsx', index=False)
   print("Planilha 'baseRk01.xlsx' salva com sucesso!")
except Exception as e:
        print("Erro ao salvar a planilha:", e)



#---------------------extrais os cem mais vendidos------------------------------------------
# Carregar o arquivo Excel
def processar_excel(caminho_entrada, caminho_saida):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_entrada)


    # Ordenar pelo "Valor da Venda" em ordem decrescente
    df_sorted = df.sort_values(by="Valor da Venda", ascending=False)

    # Selecionar os 100 itens mais vendidos
    top_100 = df_sorted.head(100)

    # Salvar o resultado em um novo arquivo Excel
    top_100.to_excel(caminho_saida, index=False)
    print(f"Arquivo processado e salvo em: {caminho_saida}")

# Caminhos de entrada e saída
caminho_entrada = (r"C:\Painel de Resultados\Bases\Ranking\baseRk01.xlsx")  # Substitua pelo nome do seu arquivo
caminho_saida = (r"C:\Painel de Resultados\Bases\Ranking\top_100_itens.xlsx")

# Chamar a função
processar_excel(caminho_entrada, caminho_saida)