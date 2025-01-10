import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template_string
import plotly_express as px
import chardet
import locale
import requests




#Brincando com a Side bar
st.sidebar.text("Lojas")

#1. Botão (st.button)
if st.button('Clique aqui!'):
    st.write('Você clicou no botão!')
else:
    st.write('Aguardando clique...')
    
 
#2. Caixa de seleção (st.checkbox)    
exibir_texto = st.checkbox('Exibir mensagem')

if exibir_texto:
    st.write('Você marcou a caixa de seleção!')
    


#3. Entrada de texto (st.text_input)   
nome = st.text_input('Digite seu nome', '')
st.write(f'Olá, {nome}!')


#4. Slider (st.slider)
idade = st.slider('Qual a sua idade?', 0, 100, 25)
st.write(f'Sua idade é {idade}')


#5. Caixas de seleção múltipla (st.multiselect)

opcoes = ['Python', 'Streamlit', 'Machine Learning', 'Data Science']
escolhas = st.multiselect('Quais tópicos você gosta?', opcoes)

st.write(f'Você gosta de: {", ".join(escolhas)}')


#6. Seleção única (st.selectbox)

linguagem = st.selectbox('Escolha uma linguagem de programação:', 
                         ['Python', 'JavaScript', 'C++', 'Java'])

st.write(f'Você escolheu: {linguagem}')


#7. Entrada de números (st.number_input)

numero = st.sidebar.number_input('Insira um número:', min_value=0, max_value=100, value=10)
st.write(f'O número escolhido foi: {numero}')
#===============================================================================================
st.title("Calculadora Simples")

# Entrada de números
numero1 = st.number_input("Insira o primeiro número:", value=0)
numero2 = st.number_input("Insira o segundo número:", value=0)

# Seleção de operação
operacao = st.selectbox("Escolha uma operação:", ["Soma", "Subtração", "Multiplicação", "Divisão"])

# Botão para calcular
if st.button("Calcular"):
    if operacao == "Soma":
        resultado = numero1 + numero2
    elif operacao == "Subtração":
        resultado = numero1 - numero2
    elif operacao == "Multiplicação":
        resultado = numero1 * numero2
    elif operacao == "Divisão":
        resultado = numero1 / numero2 if numero2 != 0 else "Erro: Divisão por zero"

    st.write(f"Resultado: {resultado}")
    
    #-------------------------------------------------------------------------------------------
    # Dados fictícios
dados = {
    "Produto": ["Cerveja", "Refrigerante", "Água"],
    "Quantidade": [120, 85, 200],
    "Preço Unitário (R$)": [5.50, 3.00, 2.00],
}

# Criando DataFrame
df = pd.DataFrame(dados)

st.title("Tabela sem indice")
st.table(df)

#Organizando com Expansíveis
st.title("Exemplo com Expansíveis")

with st.expander("Configurações Avançadas"):
    st.write("Aqui você pode configurar opções adicionais.")
    st.checkbox("Habilitar modo avançado")
    
st.title("Exemplo com Abas")

aba1, aba2 = st.tabs(["Resumo", "Configurações"])

with aba1:
    st.header("Resumo")
    st.metric("Total de Vendas", "R$ 12.450")

with aba2:
    st.header("Configurações")
    st.text_input("Nome do Usuário")
    st.slider("Idade:", 0, 100, 25)
    
#Espaçamento e Títulos
#Use st.markdown ou st.write para criar seções com títulos e espaçamentos personalizados.

st.title("Painel de Controle")

st.subheader("Seção 1: Informações Gerais")
st.write("Aqui você pode acessar informações gerais sobre o sistema.")

st.subheader("Seção 2: Configurações")
st.write("Ajuste as configurações conforme necessário.")

# Espaçamento
st.write("---")  # Linha divisória
st.write("Texto abaixo de uma linha divisória.")

#Alinhamento e Layout Customizado
#Você pode combinar colunas, expansíveis e abas para layouts mais avançados.
st.title("Dashboard Organizado")

# Dividindo o topo em três colunas
col1, col2, col3 = st.columns(3)
col1.metric("Vendas", "R$ 12.450","+5%")
col2.metric("Clientes", 145, "-3%")
col3.metric("Itens Vendidos", 320)

# Adicionando seções com expansíveis
with st.expander("Detalhes das Vendas"):
    st.write("Aqui estão os dados detalhados das vendas.")

# Abas para dividir conteúdo
aba1, aba2, aba3 = st.tabs(["Resumo", "Gráficos", "Configurações"])

with aba1:
    st.write("Resumo geral do sistema.")

with aba2:
    st.write("Gráficos interativos serão exibidos aqui.")

with aba3:
    st.text_input("Configuração de nome")
    
    
#--------------------------------------------------------------------------------------------------------
st.title("Upload e Processamento de Arquivos")

# Carregar arquivo CSV
arquivo = st.file_uploader("Escolha um arquivo CSV", type="CSV")

if arquivo is not None:
    df = pd.read_csv(arquivo)
    st.write("Dados carregados:")
    st.dataframe(df)
    st.write(f"Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")

#==========================================================================================================
# CARREGANDO IMAGEM
import streamlit as st
from PIL import Image

st.title("Upload de Imagem")

imagem = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

if imagem is not None:
    img = Image.open(imagem)
    st.image(img, caption="Imagem Carregada", use_column_width=True)
    
#-------------------------------------------------------------------------------------------------------
#import requests

st.title("Consumo de API Pública")

# URL de exemplo
url = "https://api.agify.io?name=michael"

# Chamando a API
response = requests.get(url)
data = response.json()

# Exibindo os dados retornados
st.write("Resposta da API:")
st.json(data)
st.write(f"Idade estimada para o nome Michael: {data['age']}")

#========================================================================================================
# Exemplo: Conexão com SQLite

# import streamlit as st
# import sqlite3

# st.title("Conexão com Banco de Dados")

# # Criando ou conectando ao banco de dados SQLite
# conn = sqlite3.connect("meu_banco.db")
# cursor = conn.cursor()

# # Criando uma tabela (apenas uma vez)
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS vendas (
#         id INTEGER PRIMARY KEY,
#         produto TEXT,
#         quantidade INTEGER,
#         valor REAL
#     )
# """)
# conn.commit()

# # Inserindo dados
# cursor.execute("INSERT INTO vendas (produto, quantidade, valor) VALUES (?, ?, ?)", ("Cerveja", 20, 5.5))
# conn.commit()

# # Exibindo os dados
# cursor.execute("SELECT * FROM vendas")
# dados = cursor.fetchall()
# st.write("Dados no Banco:")
# st.write(dados)

# conn.close()
#-----------------------------------------------------------------------------------------------------------------
import altair as alt

# Dados fictícios
dados = {
    "Produto": ["Cerveja", "Refrigerante", "Água"],
    "Vendas": [120, 85, 200],
}
df = pd.DataFrame(dados)

# Gráfico
grafico = alt.Chart(df).mark_bar().encode(
    x="Produto",
    y="Vendas",
    tooltip=["Produto", "Vendas"]
)

st.title("Dashboard com Gráfico")
st.altair_chart(grafico, use_container_width=True)