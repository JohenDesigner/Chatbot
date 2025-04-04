import streamlit as st

# Configurar a página do Chatbot Amigão
st.set_page_config(page_title="Chatbot Amigão", page_icon="🤖")

# Título do chatbot
st.title("👋 Olá, seja bem-vindo ao Chatbot Amigão!")

# Criar histórico de conversa (usando o estado da sessão)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada do usuário
user_input = st.chat_input("Digite sua mensagem aqui...")

if user_input:
    # Adicionar a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Gerar resposta amigável do chatbot
    response = f"Oi! Você disse: **{user_input}**. Que legal! 😊"

    # Adicionar a resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Exibir a resposta do chatbot
    with st.chat_message("assistant"):
        st.markdown(response)