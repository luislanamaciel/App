import pandas as pd


#file_path4 = 'C:/Painel de Resultados/Bases/lj010424.XLSX'
#file_path5 = 'C:/Painel de Resultados/Bases/lj010524.XLSX'
#file_path6 = 'C:/Painel de Resultados/Bases/lj010624.XLSX'
#file_path7 = 'C:/Painel de Resultados/Bases/lj010724.XLSX'
#file_path8 = 'C:/Painel de Resultados/Bases/lj010824.XLSX'
#file_path9 = 'C:/Painel de Resultados/Bases/lj010924.XLSX'
#file_path10 = 'C:/Painel de Resultados/Bases/lj011024.XLSX'
#file_path11 = 'C:/Painel de Resultados/Bases/lj011124.XLSX'
file_path12 = 'C:/Painel de Resultados/Bases/lj011224.XLSX'



try:
    #df4 = pd.read_excel(file_path4, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df5 = pd.read_excel(file_path5, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df6 = pd.read_excel(file_path6, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df7 = pd.read_excel(file_path7, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df8 = pd.read_excel(file_path8, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df9 = pd.read_excel(file_path9, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df10 = pd.read_excel(file_path10, engine='openpyxl')  # Especifica o engine 'openpyxl'
    #df11 = pd.read_excel(file_path11, engine='openpyxl')  # Especifica o engine 'openpyxl'
    df12 = pd.read_excel(file_path12, engine='openpyxl')  # Especifica o engine 'openpyxl'
    
    
    
    
    
    
    
    
    print("Arquivo carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")




# #print(df4.head())
#df4.loc[:, 'mes_resumido'] = 'Abr'
#f4.loc[:,'mes']='Abril'
#df4.loc[:,'mes_num']='4'
#df4.loc[:,'ano']='2024'
#print(df4.head())

# #print(df6.head())
#df5.loc[:, 'mes_resumido'] = 'Mai'
#df5.loc[:,'mes']='Maio'
#df5.loc[:,'mes_num']='5'
#df5.loc[:,'ano']='2024'
#print(df5.head())


#df6.loc[:, 'mes_resumido'] = 'Jun'
#df6.loc[:,'mes']='Junho'
#df6.loc[:,'mes_num']='6'
#df6.loc[:,'ano']='2024'
#print(df6.head())

#df7.loc[:, 'mes_resumido'] = 'Jul'
#df7.loc[:,'mes']='Julho'
#df7.loc[:,'mes_num']='7'
#df7.loc[:,'ano']='2024'
#print(df7.head())

#df8.loc[:, 'mes_resumido'] = 'Ago'
#df8.loc[:,'mes']='Agosto'
#df8.loc[:,'mes_num']='8'
#df8.loc[:,'ano']='2024'
#print(df8.head())

#df9.loc[:, 'mes_resumido'] = 'Set'
#df9.loc[:,'mes']='Setembro'
#df9.loc[:,'mes_num']='9'
#df9.loc[:,'ano']='2024'
#print(df9.head())

#df10.loc[:, 'mes_resumido'] = 'Out'
#df10.loc[:,'mes']='Outubro'
#df10.loc[:,'mes_num']='10'
#df10.loc[:,'ano']='2024'
#print(df10.head())

#df11.loc[:, 'mes_resumido'] = 'Nov'
#df11.loc[:,'mes']='Novembro'
#df11.loc[:,'mes_num']='11'
#df11.loc[:,'ano']='2024'
#print(df11.head())

df12.loc[:, 'mes_resumido'] = 'Dez'
df12.loc[:,'mes']='Dezembro'
df12.loc[:,'mes_num']='12'
df12.loc[:,'ano']='2024'
print(df12.head())








# Salvar o DataFrame modificado de volta no Excel
#output_path4 = 'C:/Painel de Resultados/Bases/lj010424_modificado.xlsx'  # Caminho para salvar o novo arquivo
#output_path5 = 'C:/Painel de Resultados/Bases/lj010524_modificado.xlsx'  # Caminho para salvar o novo arquivo
#output_path6 = 'C:/Painel de Resultados/Bases/lj010624_modificado.xlsx'  # Caminho para salvar o novo arquivo
#output_path7 = 'C:/Painel de Resultados/Bases/lj010724_modificado.xlsx'  # Caminho para salvar o novo arquivo
#output_path8 = 'C:/Painel de Resultados/Bases/lj010824_modificado.xlsx'  # Caminho para salvar o novo arquivo
#output_path10 = 'C:/Painel de Resultados/Bases/lj011024_modificado.xlsx'  # Caminho para salvar o novo arquivo
#utput_path11 = 'C:/Painel de Resultados/Bases/lj011124_modificado.xlsx'  # Caminho para salvar o novo arquivo
output_path12 = 'C:/Painel de Resultados/Bases/lj011224_modificado.xlsx'  # Caminho para salvar o novo arquivo














try:
     #df4.to_excel(output_path4, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     #df5.to_excel(output_path5, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     #df6.to_excel(output_path6, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     #df7.to_excel(output_path7, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     #df8.to_excel(output_path8, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     #df9.to_excel(output_path9, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     #df10.to_excel(output_path10, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     #df11.to_excel(output_path11, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     df12.to_excel(output_path12, index=False, engine='openpyxl')  # Especifica o engine 'openpyxl'
     
    
    
    
    
    
    
    
    
     #print(f"Arquivo salvo com sucesso em: {output_path4}")
     #print(f"Arquivo salvo com sucesso em: {output_path5}")
     #print(f"Arquivo salvo com sucesso em: {output_path6}")
     #print(f"Arquivo salvo com sucesso em: {output_path7}")
     #print(f"Arquivo salvo com sucesso em: {output_path8}")
     #print(f"Arquivo salvo com sucesso em: {output_path9}")
     #print(f"Arquivo salvo com sucesso em: {output_path10}")
     #print(f"Arquivo salvo com sucesso em: {output_path11}")
     print(f"Arquivo salvo com sucesso em: {output_path12}")
     
     
    
    
    
    
    
    
    
    
    
    
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")

