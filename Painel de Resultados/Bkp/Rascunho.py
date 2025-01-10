import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template_string
import plotly_express as px
import chardet
import locale




##locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') TESTAR SEM ESSA LINHA

st.set_page_config(
    page_title="Gestão de Resultados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
#Brincando com a Side bar
st.sidebar.text("Lojas")

# opcao_multselect= st.sidebar.multiselect(
# "Seleciona a Loja - Multiseleção",
#     ("Loja 1", "Loja 2", "Loja 3")
# )

# if opcao_multselect =="Loja 1":
#     st.header("Loja 1 Matriz: Av.Mariza de Souza")
# elif opcao_multselect == "Loja 2":    
#     st.header ("Loja 2 Bairro 1º de Maio")
# elif opcao_multselect == "Loja 3":    
#     st.header ("Loja 3 Bairro Centro")

















opcao_select= st.sidebar.selectbox(
"Seleciona a Loja",
    ("Loja 1", "Loja 2", "Loja 3","Todas")
)

if opcao_select =="Loja 1":
    st.header("Loja 1 Matriz: Av.Mariza de Souza")
elif opcao_select == "Loja 2":    
    st.header ("Loja 2 Bairro 1º de Maio")
elif opcao_select == "Loja 3":    
    st.header ("Loja 3 Bairro Centro")
else:
    st.header ("Todas as lojas")






opcao= st.radio( 
    "Seleciona uma opção",
    ("Opção 1", "Opção 2")
    )
if opcao =="Opção 1":
    st.header("Selecionada a opção 1")
elif opcao == "Opção 2":    
    st.header ("Selecionada a opção 2")


Check= st.sidebar.checkbox("Aceitos")
if Check:
    st.sidebar.write('Marcado')


if st.sidebar.button("Escolha"):
    st.header("DEU CERTO")

#Brincando com a Side bar

#-----------------------------------------------------------------------------------------------
# Criar duas colunas: uma para a logomarca e outra para o título
col1, col2 = st.columns([1, 4])  # Proporção 1:4, ajustando o tamanho das colunas

# Exibir a logomarca na primeira coluna
with col1:
    st.image("painel.jpg", width=150)

# Exibir o título na segunda coluna
with col2:
    st.title("Painel de Resultados Mundo Moderno")
    
#-----------------------------------------------------------------------------------------------
##Importando a planilha
#antiga importação via csv
#df = pd.read_csv("esperanca.CSV", sep=",", decimal=".", encoding="cp1252")

df = pd.read_excel('esperanca2.XLSX',thousands=".")
df_filtrado =df[['descricao','Vendas','Compras',]]
#=============================================================
# Adicionando uma nova coluna 'grupo' com base em condições
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

df_filtrado['Grupo'] = df_filtrado['descricao'].apply(definir_grupo)
# Somar Vendas e Compras por grupo
df_agrupado = df_filtrado.groupby('Grupo')[['Vendas', 'Compras']].sum().reset_index()





#===========================================

#st.dataframe(df_filtrado)
 
# Calculando o total de Vendas e Compras e formatando como R$
total_vendas = df_filtrado['Vendas'].sum()
total_compras = df_filtrado['Compras'].sum()
# Subtração do total de Compras do total de Vendas
diferenca = total_vendas - total_compras
# Calculando o percentual de Compras sobre Vendas
percentual_compras_sobre_vendas = (total_compras / total_vendas) * 100 if total_vendas != 0 else 0
# Estilo CSS para caixas com  bordas
st.markdown("""
    <style>
    .caixa-borda {
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: #333;
        background-color: #f9f9f9;
    }
    </style>
    """, unsafe_allow_html=True)


## Criando colunas para colocar as métricas na mesma linha
col1, col2, col3, col4 = st.columns(4)


# # Exibindo os valores sem caixa e bordasformatados nas colunas
# col1.metric("Total de Vendas", locale.currency(round(total_vendas, 2), grouping=True))
# col2.metric("Total de Compras", locale.currency(round(total_compras, 2), grouping=True))
# col3.metric("Diferença (Vendas - Compras)", locale.currency(round(diferenca, 2), grouping=True))
# col4.metric("Percentual de Compras sobre Vendas", f"{round(percentual_compras_sobre_vendas, 2)}%")


# Exibindo valores em caixas com borda
col1.markdown(f'<div class="caixa-borda">Total de Vendas<br>{locale.currency(round(total_vendas, 2), grouping=True)}</div>', unsafe_allow_html=True)
col2.markdown(f'<div class="caixa-borda">Total de Compras<br>{locale.currency(round(total_compras, 2), grouping=True)}</div>', unsafe_allow_html=True)
col3.markdown(f'<div class="caixa-borda">Diferença (Vendas - Compras)<br>{locale.currency(round(diferenca, 2), grouping=True)}</div>', unsafe_allow_html=True)
col4.markdown(f'<div class="caixa-borda">Percentual de Compras sobre Vendas<br>{round(percentual_compras_sobre_vendas, 2)}%</div>', unsafe_allow_html=True)
#exibindo total por grupo
#df_agrupado

##Título do Gráfico
st.subheader("Comparação de Vendas e Compras")

#=============================================================
#Grafico de barras
fig = px.bar(df_agrupado,
     x='Grupo',
     y=['Vendas', 'Compras'],
     barmode='group',
     labels={'value': 'Total', 'variable': 'Categoria'},
     title="Vendas e Compras por Produto",
     #text_auto='.2s'  # Formata os valores com separação de milhar
 )
st.plotly_chart(fig)

#=============================================================



#=============================================================

# Criar o segundo gráfico de pizza para Compras
fig_pizza_compras = px.pie(df_agrupado, 
                           names='Grupo', 
                           values='Compras', 
                           title="Compras por Seção")
#st.plotly_chart(fig_pizza_compras)


# Exibir os gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_pizza, use_container_width=True)

with col2:
    st.plotly_chart(fig_pizza_compras, use_container_width=True)

#=============================================================

# Agrupar por categoria e calcular os totais
df_gr = df_filtrado.groupby('Grupo').agg(
    total_vendas=('Vendas', 'sum'),
    total_compras=('Compras', 'sum')
).reset_index()

df_gr['diferenca'] = df_gr['total_vendas'] - df_gr['total_compras']
df_gr['percentual_compras'] = (df_gr['total_compras'] / df_gr['total_vendas']) * 100

# Exibindo os resultados no Streamlit
st.title("Resultados por Categoria")
#st.dataframe(df_descricao)

# Para cada categoria, exibir as métricas
for index, row in df_gr.iterrows():
    st.subheader(f"Categoria: {row['Grupo']}")

    # Criando as colunas para colocar as métricas na mesma linha
    col9, col10, col11, col12 = st.columns(4)

    # Exibindo os valores formatados nas colunas
    col9.metric("Total de Vendas", locale.currency(round(row['total_vendas'], 2), grouping=True))
    col10.metric("Total de Compras", locale.currency(round(row['total_compras'], 2), grouping=True))
    col11.metric("Diferença (Vendas - Compras)", locale.currency(round(row['diferenca'], 2), grouping=True))
    col12.metric("Percentual de Compras sobre Vendas", f"{round(row['percentual_compras'], 2)}%")


#=============================================================




#para mostrar no browser tive que executa o comando
#streamlit run Dash.py direto no terminal
#ele me gerou dois endereços

#Local URL: http://localhost:8501
#Network URL: http://192.168.0.93:8501



