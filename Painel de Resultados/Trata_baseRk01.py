#Condiderações Gerais

#Para geração do Painel.py antes deve-se fazer o tratamento dos dados seguindo os passos a seguir
#Gerar as planilha para totalizadores e de valores mensais
 #  1- Para os totalizadores deve-se gerar planilhas mensais chamadas lj010424 rel 160133 e salva-las em
 #  C:\Painel de Resultados\Bases isso para todas as lojas 
 #  2- Na seqquecia rodar o script Insere_Data.py que vais inserir nas planinlhas a coluna mes e ano
 #  3- Rodar o script ConverteBase.py que vai unificar todas as planilhas em um unico arquivo Base1.xls  Base2.xls Base3.xls 
 #  Esse arquivo deverá ser copiado para pasta raiz do programa
 
 

#Gerar as planilhas de Ranking
 #Como na planilha  Base1 não é possível extrair o custo da compra é necessario fazer a importação
 #da planilha baseRka01 onde será possivel gerar informações relacionadas a margem e lucro
 #   1- Emitir relatorio 65 Rk_Lj01_04_2024 de todos os meses e todas as lojas
 #   2-executar o script Insere_data_Rk.py para inserir as datas naplanilha e criar o arquivo baseRk01.
 #   3- O passo 3 sera executado nesse arquivo onde tentaremos acrescentar a coluna custo da compra e
 #   e coluna lucro e margem
 # 

#Gerar as planilhas top 100
# Basicamente pegamos a planilha baseRK01 filtramso o sem mais vendidos e salvamos como top_100_itens


 