import streamlit as st

# Configurar a página
st.set_page_config(page_title="Chatbot Amigão", page_icon="🤖")
st.title("👋 Olá, eu sou o Chatbot Amigão!")

# Inicializar o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Função para gerar resposta personalizada
def gerar_resposta(user_text):
    texto = user_text.lower()
    if "oi" in texto or "olá" in texto:
        return "Olá! Como posso te ajudar hoje?"
    elif "como vai" in texto:
        return "Estou bem, obrigado por perguntar! E você?"
    elif "tchau" in texto or "adeus" in texto:
        return "Até logo! Foi ótimo conversar com você."
    else:
        return "Interessante! Pode me contar mais sobre isso?"

# Entrada do usuário
user_input = st.chat_input("Digite sua mensagem aqui...")

if user_input:
    # Adicionar a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Gerar resposta com base no input do usuário
    resposta = gerar_resposta(user_input)
    
    # Adicionar a resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    
    # Exibir a resposta
    with st.chat_message("assistant"):
        st.markdown(resposta)