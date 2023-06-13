import streamlit as st
## Configuração das paginas
st.set_page_config(
    page_title="Fynance",
    page_icon="📈"
)
##criacao das pastas e download de arquivos
import fynance
from fynance import situacao

if situacao == True:
    st.sidebar.success("Tudo certo")
else:
    st.sidebar.error("Ao está errado")

st.title("Bem-vindo a Fynance")
st.write("""
    O Fynance é um site focado na área de estatística e análise de mercado
""")