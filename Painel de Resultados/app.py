import streamlit as st
import base64




# Configuração da página
st.set_page_config(page_title="Capa do Trabalho", page_icon="📘", layout="centered")


# Definir o caminho da imagem de fundo
background_image_path = 'Painel.jpg'  # Altere o caminho, se necessário

# Usar CSS para aplicar a imagem de fundo
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_path}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }}
    </style>
    """,
    unsafe_allow_html=True
)













def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

logo_base64 = image_to_base64("logo.png")




# Título principal
#st.title("Painel de Resultados")

col1, col2 = st.columns([2, 3])  # Proporção 1:4, ajustando o tamanho das colunas
with col1:
    st.markdown(
        f"""
        <div style="
            border: 3px solid blue; 
            padding: 10px; 
            border-radius: 5px; 
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            display: flex;
            justify-content: center;
            align-items: center;
        ">
            <img src="data:image/png;base64,{logo_base64}" style="width: 217px; height: auto;">
            
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="
            border: 3px solid blue; 
            padding: 16px; 
            border-radius: 5px; 
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            justify-content: center;
        ">
            <h2 style="text-align: center;">Painel de Resultados </h2>
           
            
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    """
    <br>
    <div style="text-align: justify;">
        <b>Dashboard Painel de Resultados uma ferramenta com indicadores comerciais e financeiros que permitem acompanhar as movimentações de compra e venda. 
        Apoia a tomada de decisões, apresenta insights que ajudam gestores a identificar tendências, problemas e oportunidades.</b>
    </div>
    """, 
    unsafe_allow_html=True
)








    
#elif pagina == "Painel de Resultados":
    
  #  st.write("Aqui você pode visualizar os resultados do seu projeto.")
    # Adicione o código específico do Painel de Resultados aqui