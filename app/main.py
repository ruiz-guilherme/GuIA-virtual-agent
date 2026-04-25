import streamlit as st

from app.data.loader import carregar_dados
from app.utils.formatter import montar_contexto
from app.prompts import montar_prompt
from app.services.ollama_client import perguntar_ollama

# Carregar dados
perfil, produtos, historico, transacoes = carregar_dados()
contexto = montar_contexto(perfil, produtos, historico, transacoes)

# UI
st.title("Oi, sou o GuIA, seu educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("Pensando..."):
        prompt = montar_prompt(contexto, pergunta)
        resposta = perguntar_ollama(prompt)

    st.chat_message("assistant").write(resposta)