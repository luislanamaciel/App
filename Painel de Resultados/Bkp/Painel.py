import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template_string
import plotly_express as px
#import chardet
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # Configure o locale para seu idioma e região (por exemplo, "pt_BR.UTF-8" para Brasil)
#streamlit run Painel.py direto no terminal




#-----------------------------------------CONFIGURAR PAGINA------------------------
st.set_page_config(
    page_title="Gestão de Resultados",
    page_icon="📊",
    layout="wide",
    #initial_sidebar_state="expanded"
)

#-----------------------------------------FIM CONFIGURAR PAGINA------------------------





#-----------Importa base apenas para pegar a primeira e ultima linha----------------------------


df_periodo = pd.read_excel(r'C:\Painel de Resultados\Bases\base1.xlsx',thousands=".")
#  # busca a primeira e utlima linha para monta mensagem de período 
primeira_linha = df_periodo.iloc[0]
ultima_linha = df_periodo.iloc[-1]
st.sidebar.text("Período")
st.sidebar.write("De:", primeira_linha['mes'],"a" ,ultima_linha['mes'],"2024")


#st.sidebar.text("MENU")
#-----------------------------------------FIM DA FOMRAÇÃO DE PERÍODO-----------------------------------




#---------------------------------------BLOCO PRINCIPAL DO PROGRAMa-------------------------------------




#----------------------------SELEÇÃO DE LOJA O PROGRAMA É DIVIDO EM TRÊS SEÇÕES-------------------------
#-----------------------------------------ESTRUTURA DE SELEÇÃO-----------------------------------------

opcao_select= st.sidebar.selectbox(
"Seleciona a Loja",
    ("Loja 1", "Loja 2", "Loja 3","Todas")
)

if opcao_select =="Loja 1":  ##### INICIO DA SEÇÃO 01################ 
    
    
    #----------------- BLOCO 01 Criar duas colunas: uma para a logomarca e outra para o título-----------------------
    col1, col2 = st.columns([1, 4])  # Proporção 1:4, ajustando o tamanho das colunas
    
    with col1: # Exibir a logomarca na primeira coluna
     st.image("logo.png", width=180)

    with col2: # Exibir o título na segunda coluna
     #st.title("Loja 1 Matriz")
     st.header("Matriz - Av.Mariza de Souza")
     #------------------------------------- FIM DA BLOCO 1--------------------------------------------------
     
     
     
     #---------------------------BLOCO 2 IMPORTAÇÃO DA BASE1------------------------------------------------
     df = pd.read_excel(r'C:\Painel de Resultados\Bases\base1.xlsx',thousands=".")
     df_filtrado =df[['descricao','totvendas','totcompras','mes_resumido','mes_num']]     


     #---------------------------FIM DA BLOCO 2 ------------------------------------------------------------  
     
      
     
     #---------------------------BLOCO 3 ADICIONANDO NOVA COLUNA'GRUPO' NA BASE1-----------------------------
     def definir_grupo(descricao):
       if 'AÇOUGUE' in descricao:
         return 'AÇOUGUE'
       elif 'FRIOS E CONGELADOS' in descricao:
         return 'FRIOS'
       elif 'LATICINIOS' in descricao:
         return 'FRIOS'
       elif 'EMBUTIDOS' in descricao:
         return 'FRIOS'
       elif 'PADARIA' in descricao:
         return 'PADARIA'
       elif 'HORTIFRUTi' in descricao:
         return 'HORTIFRUTi'
       elif 'RESTAURANTE' in descricao:
         return 'RESTAURANTE'
       elif 'USO INTERNO' in descricao:
         return 'USO'       
       else:
         return 'LOJA'
     df_filtrado['Grupo'] = df_filtrado['descricao'].apply(definir_grupo) #criando a nova coluna Grupo
    #--------------------------------------------FIM BLOCO 3-----------------------------------------------------
    
  
    #--------------------------------------BLOCO 4 AGRUPAMENTO MÊS GRUPO E SOMENTE MÊS----------------------------
     #df_agrupado_mes_grupo agrupa as vendas por mes e por grupo
    df_agrupado_mes_grupo = df_filtrado.groupby(['Grupo', 'mes_resumido'])[['totvendas', 'totcompras']].sum().reset_index()
    
    #df_agupado_mes agrupa venda e compra somente por mês para grafico de linhas
    df_agrupado_mes = df_filtrado.groupby(['mes_num'])[['totvendas', 'totcompras']].sum().reset_index() 
    
    #df_agupado_mes2 agrupa venda e compra somente por mês para totalizadores do mês
    df_agrupado_mes2 = df_filtrado.groupby(['mes_resumido'])[['totvendas', 'totcompras']].sum().reset_index() 
      
    #st.dataframe(df_agrupado_mes)
    #--------------------------------------FIM DA BLOCO 4---------------------------------------------------------
    
    
    
    #---------------------------------------BLOCO 5 CÁLCULO DE TOTALIZADORES DO PERÍODO------------------------------------
    total_vendas = df_filtrado['totvendas'].sum()
    total_compras = df_filtrado['totcompras'].sum()
    diferenca = total_vendas - total_compras # Subtração do total de Compras do total de Vendas
    percentual_compras_sobre_vendas = (total_compras / total_vendas) * 100 if total_vendas != 0 else 0  #Calculando o percentual de Compras sobre Vendas
    
    st.subheader(f"Totalizadores") # título de totalizadores
    #-----------------------------------------FIM DA BLOCO 5----------------------------------------------------------------
    
    
    
    #---------------------------------------BLOCO 6 ESTILO CSS PARA CAIXAS COM BORDAS---------------------------------------
    st.markdown("""
    <style>
       
     .metric-small-font {
        font-size: 0.9em;
        font-weight: bold;
        color: #333; /* Ajuste a cor como preferir */
    }
    .metric-container {
        text-align: center;
        padding: 10px;
        background-color: #f0f0f5; /* Ajuste o fundo se desejar */
        border-radius: 8px;
        margin: 5px;
    }  
           
    .caixa-borda {
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: #333;
        background-color: #f9f9f9;
    }
    </style>
    """, unsafe_allow_html=True)
    #--------------------------------------------FIM BLOCO 6------------------------------------------------------------------
    
    #-----------------------------------BLOBO 7 CRIANDO COLUNAS PARA TOTALIZADORES---------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)
    #-----------------------------------FIM BLOCO 7 DA CRIAÇÃO DE COLUNAS-----------------------------------------------------------
    
    
    
    #-----------------------------------BLOCO 8 Inserido Totalizadores Gerais nas caixas------------------------------------------------------------------
    col1.markdown(f'<div class="caixa-borda">Total de Vendas<br>{locale.currency(round(total_vendas, 2), grouping=True)}</div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="caixa-borda">Total de Compras<br>{locale.currency(round(total_compras, 2), grouping=True)}</div>', unsafe_allow_html=True)
    col3.markdown(f'<div class="caixa-borda">Diferença)<br>{locale.currency(round(diferenca, 2), grouping=True)}</div>', unsafe_allow_html=True)
    col4.markdown(f'<div class="caixa-borda">%Compras sobre Vendas<br>{round(percentual_compras_sobre_vendas, 2)}%</div>', unsafe_allow_html=True)
    #-------------------------------------------FIM BLOCO 8----------------------------------------------------------------------------------------------
    
    
    #-------------------------------------------BLOCO 9 Gráfico de Linhas do Período---------------------------------------------------------------------------------------
    
    # Formatar os valores para duas casas decimais
    #   df_agrupado_mes['totvendas'] = df_agrupado_mes['totvendas'].round(2)
    #   df_agrupado_mes['totcompras'] = df_agrupado_mes['totcompras'].round(2)
    
    
    
    #   # Criar o gráfico de linhas
    #   fig5 = px.line(df_agrupado_mes, x='mes', y=['totvendas', 'totcompras'], 
    #             labels={'value': 'Total', 'variable': 'Categoria', 'mes': 'Mês'},
    #             title='Vendas e Compras Mensais')
    
    #  # Adicionar valores formatados nos pontos para cada linha individualmente
    #   for i, coluna in enumerate(['totvendas', 'totcompras']):
    #    fig5.data[i].text = df_agrupado_mes[coluna].apply(lambda x: f'R${x:.2f}')
    #    fig5.data[i].textposition = "top center"
    #    fig5.data[i].mode = "lines+markers+text"
  # Dividir os valores por 1000 e formatar para duas casas decimais
    df_agrupado_mes['totvendas'] = (df_agrupado_mes['totvendas'] / 1000).round(2)
    df_agrupado_mes['totcompras'] = (df_agrupado_mes['totcompras'] / 1000).round(2)
    
    
    
    
    
    # Função para formatar os números no padrão brasileiro (ponto para milhar, vírgula para decimal)
    def formatar_numero_brasil(valor):
      return f"{valor:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")

    
  # # Criar o gráfico de linhas
    fig5 = px.line(
        df_agrupado_mes, 
        x='mes_num', 
        y=['totvendas', 'totcompras'], 
        labels={'value': 'Total (milhares de R$)', 'variable': 'Categoria', 'mes_num': 'Mês'},
        title='Vendas e Compras no Período'
      )

  # # Adicionar valores formatados com "R$" e "K" nos pontos para cada linha individualmente
    for i, coluna in enumerate(['totvendas', 'totcompras']):
       #fig5.data[i].text = df_agrupado_mes[coluna].apply(lambda x: f'<span style="color: black;"><b>R$ {x:,.2f}K</b>')
       fig5.data[i].text = df_agrupado_mes[coluna].apply(lambda x: f'<span style="color: black;"><b>R$ {formatar_numero_brasil(x)}K</b></span>')
       fig5.data[i].textposition = "top center"
       fig5.data[i].mode = "lines+markers+text"
    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig5)
    
#-------------------------------------------FIM BLOCO 9----------------------------------------------------------------------------------------------    
    
    
    
    
#-BLOCO 10 Crias colunas Para Movimentação Mensal---------------------------------------------------------------------------------
   
    st.text(f"Movimentação Mensal")
    col5, col6, col7, col8 = st.columns(4) #CRIA COLUNAS PARA OS TOTALIZADORES POR MÊS
   
   #Antiga forma de apurar os valoes mensais
    #df_agrupado_mes.groupby('mes')[['totvendas', 'totcompras']].sum().reset_index() #FILTRA POR MES
    #totais_por_mes = df_filtrado.groupby('mes')[['totvendas', 'totcompras']].sum().reset_index() #FILTRA POR MES
    
#-FIM BLOCO 10---------------------------------------------------------------------------------------------------------
   
    
    

    
######### ESTRUTURA DE SELEÇÃO DO MÊS-------------------------------------------------------------------------------------------
    
    opcao_select1= st.sidebar.selectbox( # cria caixa de seleção por mês na sidebar
     "Seleciona o Período",
    ("Janeiro", "Fevereiro", "Março","Abril","Maio","Junho","Julho","Agosto","Setembro",
     "Outubro","Novembro","Dezembro"))
     
    if opcao_select1 =="Abril":
#-BLOCO 11 RECEBE TOTAL DO MÊS FILTRADO POR MÊS ESPECIFICO ABRIL-------------------------------------------------------------      
        mes_especifico = 'Abr'
        total_vendas_mes = df_agrupado_mes2.loc[df_agrupado_mes2['mes_resumido'] == mes_especifico, 'totvendas'].values[0]
        total_compras_mes = df_agrupado_mes2.loc[df_agrupado_mes2['mes_resumido'] == mes_especifico, 'totcompras'].values[0]
        diferenca_mes = total_vendas_mes - total_compras_mes
        percentual_compras_vendas_mes = (total_compras_mes / total_vendas_mes) * 100 if total_vendas != 0 else 0
        col5.markdown(f'<div class="caixa-borda">Vendas Abril<br>{locale.currency(round(total_vendas_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col6.markdown(f'<div class="caixa-borda">Compras Abril<br>{locale.currency(round(total_compras_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col7.markdown(f'<div class="caixa-borda">Diferença Abril<br>{locale.currency(round(diferenca_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col8.markdown(f'<div class="caixa-borda">% Compras/Vendas Abril <br>{round(percentual_compras_vendas_mes, 2)}%</div>', unsafe_allow_html=True)
#-FIM DO BLOCO 11-----------------------------------------------------------------------------------------------------------------------------  
       
#-BLOCO 12 df_mes Recebe df_agrupado de Acordo Com Mês do if---------------------------------------------------------------------------------------   
        df_mes= df_agrupado_mes_grupo[df_agrupado_mes_grupo['mes_resumido'] == mes_especifico] 
              
        # ACHANDO A DIFRENÇA E O PERCENTUAL  PARA CONSTRUÇÃO DOS GRÁFICOS 
        df_mes['dif'] = df_mes['totvendas'] - df_mes['totcompras'] #caluclo de indicadores mensais
        df_mes['percentual']= (df_mes['totcompras'] / df_mes['totvendas'])*100 #calculo de indicadores mensais
#-FIM BLOCO 12-----------------------------------------------------------------------------------------------------------
        
#-BLOCO 13 CONSTRUÇÃO DOS GRÁFICOS POR MÊS-----------------------------------------------------------------------------------------------   
        #Grafico de barras
        fig = px.bar(df_mes,
        x='Grupo',
        y=['totvendas', 'totcompras',],
        barmode='group',
        labels={'value': 'Total', 'variable': 'Categoria'},
        title=f"Vendas e Compras por Grupo - Mês {mes_especifico}"
        #text_auto='.2s'  # Formata os valores com separação de milhar
        )
        st.plotly_chart(fig)
       
        
        
        
        # Criando o gráfico de barras horzontais
        # Transformando o DataFrame para a estrutura adequada importante para formatação
        #ficar correta (barras proporcionais e somente um valor de percentutal)
        df_mes_melted = df_mes.melt(id_vars=['Grupo', 'percentual'], 
                                    value_vars=['totcompras', 'totvendas'],
                                    var_name='Categoria', 
                                    value_name='Total')
        
        
        fig2 = px.bar(
           df_mes_melted,
           y='Grupo',  # Para barras horizontais, 'y' será o eixo vertical
           x='Total',
           color='Categoria',
           orientation='h',
           barmode='group',  # Agrupamento
           labels={'Total': 'Total', 'Categoria': 'Categoria'},
           title=f"Percentual Compra - Venda {mes_especifico}",
           text=df_mes_melted.apply(
              lambda row: f"{row['percentual']:.2f}%" if row['Categoria'] == 'totcompras' else '', axis=1
           )  # Adiciona o percentual apenas às barras de 'totcompras'
        )
          
         # Atualizando a posição do texto para dentro ou fora das barras
        fig2.update_traces(textposition='outside')  # Você pode usar 'outside' se preferir o texto fora da barra

         # Exibindo o gráfico
        st.plotly_chart(fig2)    
        
    
        
        
        # Criar o segundo gráfico de pizza para Compras
        fig_pizza_compras = px.pie(df_mes, 
                           names='Grupo', 
                           values='totcompras', 
                           title="Compras por Divisão")
        #st.plotly_chart(fig_pizza_compras)
        
        
        # Criar o segundo gráfico de pizza para vendas
        fig_pizza_vendas = px.pie(df_mes, 
                           names='Grupo', 
                           values='totvendas', 
                           title="Vendas por Divisão")
        #st.plotly_chart(fig_pizza_compras)
        
        
        # Exibir os gráficos lado a lado
        col9, col10 = st.columns(2)
        
        with col9:
         st.plotly_chart(fig_pizza_compras, use_container_width=True)

        with col10:
         st.plotly_chart(fig_pizza_vendas, use_container_width=True)
         
         
         
#-FIM BLOCO 13 GRÁFICOS -----------------------------------------------------------------------------------------------------                 
 
        
#-BLOCO 14- EXIBINDO TOTAIS POR GRUPO DENTRO DO MES ESCOLHIDO------------------------------------------------------------------- 
       # Agrupar por categoria e calcular os totais
        #df_mes['dif'] = df_mes['totvendas'] - df_mes['totcompras']
        #df_mes['percentual']= (df_mes['totcompras'] / df_mes['totvendas'])*100
            
             
        

        # Para cada categoria, exibir as métricas
        for index, row in df_mes.iterrows():
         
         st.markdown(f"""
         <h3 style='font-size:18px;'>{row['Grupo']}:</h3>
         """, unsafe_allow_html=True)       
         
         col11, col12, col13, col14  = st.columns(4)
         
         with col11:
          col11.markdown(f"""
          <div class="metric-container">
          <div class="metric-small-font">Total de Vendas</div>
          <div class="metric-small-font">{locale.currency(round(row['totvendas'], 2), grouping=True)}</div>
          </div>
         """, unsafe_allow_html=True)
         
         with col12: 
          col12.markdown(f"""
          <div class="metric-container">
          <div class="metric-small-font">Total de Compras</div>
          <div class="metric-small-font">{locale.currency(round(row['totcompras'], 2), grouping=True)}</div>
          </div>
         """, unsafe_allow_html=True)
          
         with col13: 
          col13.markdown(f"""
          <div class="metric-container">
          <div class="metric-small-font">Diferença</div>
          <div class="metric-small-font">{locale.currency(round(row['dif'], 2), grouping=True)}</div>
          </div>
         """, unsafe_allow_html=True) 
          
         with col14: 
          col14.markdown(f"""
          <div class="metric-container">
          <div class="metric-small-font">% Compra/Venda</div>
          <div class="metric-small-font">{row['percentual']:.2f}%</div>
          </div>
         """, unsafe_allow_html=True) 
           
         
         #Maneira anterior de apresentar os dados sem caixa de texto
         #col9.metric("Total de Vendas", locale.currency(round(row['totvendas'], 2), grouping=True))           
         #col10.metric("Total de Compras", locale.currency(round(row['totcompras'], 2), grouping=True)) 
         #col11.metric("Diferença", locale.currency(round(row['dif'], 2), grouping=True)) 
         #col12.metric("% Compra sobre Venda", f"{row['percentual']:.2f}%")    
         #st.dataframe(df_mes)
#-FIM BLOCO 14------------------------------------------------------------------------------------------------------------------------
        
        
        
    elif opcao_select1 == "maio":
        mes_especifico = 'maio'    
        total_vendas_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totvendas'].values[0]
        total_compras_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totcompras'].values[0]
        diferenca_mes = total_vendas_mes - total_compras_mes
        percentual_compras_vendas_mes = (total_compras_mes / total_vendas_mes) * 100 if total_vendas != 0 else 0
        col5.markdown(f'<div class="caixa-borda">Vendas Maio<br>{locale.currency(round(total_vendas_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col6.markdown(f'<div class="caixa-borda">Compras Maio<br>{locale.currency(round(total_compras_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col7.markdown(f'<div class="caixa-borda">Diferença Maio<br>{locale.currency(round(diferenca_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col8.markdown(f'<div class="caixa-borda">%Compras/Vendas Maio<br>{round(percentual_compras_vendas_mes, 2)}%</div>', unsafe_allow_html=True)
       
       
        
        
    elif opcao_select1 == "junho":
        mes_especifico = 'junho'    
        total_vendas_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totvendas'].values[0]
        total_compras_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totcompras'].values[0]
        diferenca_mes = total_vendas_mes - total_compras_mes
        percentual_compras_vendas_mes = (total_compras_mes / total_vendas_mes) * 100 if total_vendas != 0 else 0
        col5.markdown(f'<div class="caixa-borda">Vendas Junho<br>{locale.currency(round(total_vendas_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col6.markdown(f'<div class="caixa-borda">Compras Junho<br>{locale.currency(round(total_compras_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col7.markdown(f'<div class="caixa-borda">Diferença Junho<br>{locale.currency(round(diferenca_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col8.markdown(f'<div class="caixa-borda">%Compras/Vendas Junho<br>{round(percentual_compras_vendas_mes, 2)}%</div>', unsafe_allow_html=True)
       
       
       
       
       
       
        
    elif opcao_select1 == "julho":
        mes_especifico = 'julho'    
        total_vendas_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totvendas'].values[0]
        total_compras_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totcompras'].values[0]
        diferenca_mes = total_vendas_mes - total_compras_mes
        percentual_compras_vendas_mes = (total_compras_mes / total_vendas_mes) * 100 if total_vendas != 0 else 0
        col5.markdown(f'<div class="caixa-borda">Vendas Julho<br>{locale.currency(round(total_vendas_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col6.markdown(f'<div class="caixa-borda">Compras Julho<br>{locale.currency(round(total_compras_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col7.markdown(f'<div class="caixa-borda">Diferença Julho<br>{locale.currency(round(diferenca_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col8.markdown(f'<div class="caixa-borda">% Compras/Vendas Julho<br>{round(percentual_compras_vendas_mes, 2)}%</div>', unsafe_allow_html=True)
        
    elif opcao_select1 == "agosto":
        mes_especifico = 'agosto'    
        total_vendas_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totvendas'].values[0]
        total_compras_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totcompras'].values[0]
        diferenca_mes = total_vendas_mes - total_compras_mes
        percentual_compras_vendas_mes = (total_compras_mes / total_vendas_mes) * 100 if total_vendas != 0 else 0
        col5.markdown(f'<div class="caixa-borda">Vendas Agosto<br>{locale.currency(round(total_vendas_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col6.markdown(f'<div class="caixa-borda">Compras Agosto<br>{locale.currency(round(total_compras_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col7.markdown(f'<div class="caixa-borda">Diferença Agosto<br>{locale.currency(round(diferenca_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col8.markdown(f'<div class="caixa-borda">% Compras/Vendas Agosto<br>{round(percentual_compras_vendas_mes, 2)}%</div>', unsafe_allow_html=True)     
    
    elif opcao_select1 == "setembro":
        mes_especifico = 'setembro'    
        total_vendas_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totvendas'].values[0]
        total_compras_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totcompras'].values[0]
        diferenca_mes = total_vendas_mes - total_compras_mes
        percentual_compras_vendas_mes = (total_compras_mes / total_vendas_mes) * 100 if total_vendas != 0 else 0
        col5.markdown(f'<div class="caixa-borda">Vendas Setembro<br>{locale.currency(round(total_vendas_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col6.markdown(f'<div class="caixa-borda">Compras Setembro<br>{locale.currency(round(total_compras_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col7.markdown(f'<div class="caixa-borda">Diferença Setembro<br>{locale.currency(round(diferenca_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col8.markdown(f'<div class="caixa-borda">% Compras/Vendas SEtembro<br>{round(percentual_compras_vendas_mes, 2)}%</div>', unsafe_allow_html=True)  
    
    elif opcao_select1 == "outubro":
        mes_especifico = 'outubro'    
        total_vendas_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totvendas'].values[0]
        total_compras_mes = df_agrupado_mes.loc[df_agrupado_mes['mes'] == mes_especifico, 'totcompras'].values[0]
        diferenca_mes = total_vendas_mes - total_compras_mes
        percentual_compras_vendas_mes = (total_compras_mes / total_vendas_mes) * 100 if total_vendas != 0 else 0
        col5.markdown(f'<div class="caixa-borda">Vendas Outubro<br>{locale.currency(round(total_vendas_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col6.markdown(f'<div class="caixa-borda">Compras Outubro<br>{locale.currency(round(total_compras_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col7.markdown(f'<div class="caixa-borda">Diferença Outubro<br>{locale.currency(round(diferenca_mes, 2), grouping=True)}</div>', unsafe_allow_html=True)
        col8.markdown(f'<div class="caixa-borda">% Compras/Vendas Outubro<br>{round(percentual_compras_vendas_mes, 2)}%</div>', unsafe_allow_html=True)   
        
    elif opcao_select1 == "novembro":
        mes_especifico = 'novembro'    
        #total_vendas_mes = totais_por_mes.loc[totais_por_mes['mes'] == mes_especifico, 'totvendas'].values[0]
        #total_compras_mes = totais_por_mes.loc[totais_por_mes['mes'] == mes_especifico, 'totcompras'].values[0]
        #st.write("Totais por mês:", total_vendas_mes)     
    
    elif opcao_select1 == "dezembro":
        mes_especifico = 'dezembro'    
        #total_vendas_mes = totais_por_mes.loc[totais_por_mes['mes'] == mes_especifico, 'totvendas'].values[0]
        #total_compras_mes = totais_por_mes.loc[totais_por_mes['mes'] == mes_especifico, 'totcompras'].values[0]
        #st.write("Totais por mês:", total_vendas_mes)     
       
    else:
        st.header ("ESCOLHA UM MÊS")
   
    
    
   
    #***********************************FIM DA CRIAÇÃO DE COLUNAS**************************************************

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
elif opcao_select == "Loja 2":    
    st.header ("Loja 2 Bairro 1º de Maio")
elif opcao_select == "Loja 3":    
    st.header ("Loja 3 Bairro Centro")
else:
    st.header ("--  --")
#-------------------CRIAS CAIXA DE SELEÇÃO DE LOJAS FIM--------------


