import pandas as pd
import streamlit as st
from datetime import datetime

# Gerando a tabela calendário
date_range = pd.date_range(start='2023-01-01', end='2024-12-31')
calendar_df = pd.DataFrame({'Data': date_range})
calendar_df['Ano'] = calendar_df['Data'].dt.year
calendar_df['Mês'] = calendar_df['Data'].dt.month
calendar_df['Dia'] = calendar_df['Data'].dt.day
calendar_df['Dia da Semana'] = calendar_df['Data'].dt.day_name()

# Seleção de intervalo de datas
intervalo_datas = st.date_input(
    "Escolha um intervalo de datas",
    value=(datetime(2023, 1, 1), datetime(2023, 12, 31))
)

# Verifica se o usuário selecionou um intervalo ou uma única data
if isinstance(intervalo_datas, tuple):
    data_inicial = pd.to_datetime(intervalo_datas[0])
    data_final = pd.to_datetime(intervalo_datas[1])
else:
    data_inicial = pd.to_datetime(intervalo_datas)
    data_final = data_inicial

# Filtra o DataFrame com base na seleção de datas
filtro_df = calendar_df[(calendar_df['Data'] >= data_inicial) & (calendar_df['Data'] <= data_final)]

# Exibe o DataFrame filtrado
st.write("Calendário Filtrado")
st.dataframe(filtro_df)