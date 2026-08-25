import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="História com IA", page_icon="📖")
st.title("📖 Sua História Interativa")

# Puxa a chave de forma segura das configurações do Streamlit
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "historico" not in st.session_state:
    st.session_state.historico = []
if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False
if "opcoes" not in st.session_state:
    st.session_state.opcoes = []
if "texto_atual" not in st.session_state:
    st.session_state.texto_atual = ""

def gerar_continuacao(prompt_usuario):
    system_prompt = (
        "Você é um mestre de RPG. Continue a história com base na escolha do usuário. "
        "Mantenha o texto curto (máximo 2 parágrafos). "
        "No final, você DEVE fornecer exatamente 3 opções de escolha para o jogador usando este formato estrito:\n"
        "[OPCOES]\n"
        "1. Opção um\n"
        "2. Opção dois\n"
        "3. Opção três"
    )
    
    mensagens = [{"role": "system", "content": system_prompt}]
    for turno in st.session_state.historico:
        mensagens.append({"role": "user", "content": turno["escolha"]})
        mensagens.append({"role": "assistant", "content": turno["narracao"]})
    
    mensagens.append({"role": "user", "content": prompt_usuario})
    
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=mensagens,
        temperature=0.7
    )
    
    conteudo = response = resposta.choices.message.content
    
    if "[OPCOES]" in conteudo:
        partes = conteudo.split("[OPCOES]")
        texto = partes[0].strip()
        linhas_opcoes = partes[1].strip().split("\n")
        opcoes = [opt.split(".", 1)[-1].strip() for opt in linhas_opcoes if opt.strip()]
    else:
        texto = conteudo
        opcoes = ["Começar de novo", "Explorar outro caminho"]
        
    return texto, opcoes

if not st.session_state.jogo_iniciado:
    st.subheader("Escolha o tema da sua aventura:")
    tema = st.text_input("Ex: Apocalipse Zumbi, Escola de Magia...", "Uma masmorra medieval")
    
    if st.button("Iniciar Aventura 🚀"):
        st.session_state.jogo_iniciado = True
        with st.spinner("Criando o início..."):
            texto, opcoes = gerar_continuacao(f"Comece uma história com o tema: {tema}")
            st.session_state.texto_atual = texto
            st.session_state.opcoes = opcoes
        st.rerun()
else:
    st.markdown("### 📖 O que acontece agora:")
    st.write(st.session_state.texto_atual)
    
    st.markdown("### 🧭 Sua Escolha:")
    for opcao in st.session_state.opcoes:
        if st.button(opcao, key=opcao):
            st.session_state.historico.append({
                "escolha": opcao,
                "narracao": st.session_state.texto_atual
            })
            with st.spinner("A IA está pensando..."):
                texto, opcoes = gerar_continuacao(f"Eu escolho: {opcao}")
                st.session_state.texto_atual = texto
                st.session_state.opcoes = opcoes
            st.rerun()

    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 Reiniciar Jogo"):
        st.session_state.historico = []
        st.session_state.jogo_iniciado = False
        st.session_state.opcoes = []
        st.session_state.texto_atual = ""
        st.rerun()
