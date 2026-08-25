import streamlit as st

st.set_page_config(page_title="Simulador de Inteligencia Emocional", page_icon="💼", layout="centered")

# --- BANCO DE DADOS LOCAL DE RESPOSTAS (Sessão Segura) ---
if "respostas_usuarios" not in st.session_state:
    st.session_state.respostas_usuarios = []

# --- INJEÇÃO DE DESIGN CUSTOMIZADO (CSS) ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    h1 {
        color: #fde047 !important;
        text-shadow: 2px 2px 8px rgba(253, 224, 71, 0.4);
        text-align: center;
        font-weight: 800 !important;
        padding-bottom: 20px;
    }
    h3 {
        color: #f472b6 !important;
        font-weight: 700 !important;
        margin-top: 10px;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #ec4899 0%, #db2777 100%) !important;
        color: #ffffff !important;
        border: 2px solid #fde047 !important;
        border-radius: 4px 15px 5px 20px !important;
        padding: 14px 20px !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3) !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #a855f7 0%, #9333ea 100%) !important;
        color: #fde047 !important;
        border-color: #ec4899 !important;
        transform: translateY(-2px);
    }
    .stTextInput textarea, .stTextInput input {
        background-color: #1e1b4b !important;
        color: #f8fafc !important;
        border: 2px solid #a855f7 !important;
        border-radius: 10px !important;
    }
    [data-testid="stSidebar"] {
        background-color: #1e1b4b !important;
        border-right: 2px solid #a855f7;
    }
    hr {
        border-top: 2px dashed #a855f7 !important;
        margin: 25px 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "passo" not in st.session_state:
    st.session_state.passo = "inicio"

# Fluxo da História Fixa
if st.session_state.passo == "inicio":
    st.title("💼 Simulador de Inteligencia Emocional")
    st.markdown("### ✨ 📅 O ULTIMO DIA DO MES ✨")
    
    texto_historia = (
        "O relogio corre contra voce. E o ultimo dia do mes e o clima na empresa esta puro desespero. "
        "Voce passa horas grudado ao telefone, com o suor frio escorrendo, sabendo que falta apenas uma unica venda "
        "para bater a meta e garantir aquela bonificacao que vai salvar as suas contas.\n\n"
        "Apos dias de uma negociacao exaustiva e cheia de idas e vindas, o cliente finalmente cede. 'Vamos fechar', "
        "ele diz. Um alivio gigantesco toma conta do seu peito.\n\n"
        "Voce abre o sistema com as manos tremulas para registrar o pedido, mas, no pior momento possivel, a tela congela. "
        "O computador travou completamente. Voce aperta loucamente o teclado, tenta reiniciar, mexe nos cabos, mas a maquina simplesmente nao responde.\n\n"
        "Enquanto voce entra em panico tentando resolver o problema tecnico, nota que o colega da mesa ao lado que vinha acompanhando seu esforco de longe se levanta de fininho. Ele assume a ligacao com o seu cliente e, sem o menor pudor, fecha a venda no lugar dele.\n\n"
        "Quando o seu sistema finalmente volta a funcionar, o estomago embrulha: o painel mostra que a comissao ja foi registrada no nome dele. O expediente esta no fim, nao ha mais tempo para correr atras de outro cliente e a sua bonificacao acabou de escorrer pelos dedos."
    )
    
    st.markdown(f"<div style='background-color: #3b0764; padding: 22px; border-radius: 20px 4px 15px 5px; border-left: 5px solid #fde047; margin-bottom: 25px;'>{texto_historia}</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='color: #fde047; margin-bottom: 15px;'>🧭 ESCREVA O QUE VOCE FAZ?</h4>", unsafe_allow_html=True)
    
    resposta_usuario = st.text_area("Digite sua atitude com inteligencia emocional aqui:", placeholder="Ex: Eu respiraria fundo, pegaria as provas e falaria com o gerente...", height=120)
    
    if st.button("Enviar Resposta Final 🚀"):
        if resposta_usuario.strip() != "":
            st.session_state.respostas_usuarios.append(resposta_usuario)
            st.session_state.passo = "fim"
            st.rerun()
        else:
            st.warning("Por favor, digite alguma resposta antes de enviar!")

elif st.session_state.passo == "fim":
    st.title("💼 Simulador de Inteligencia Emocional")
    st.markdown("### ✨ Resposta Enviada com Sucesso! ✨")
    st.write("Sua atitude foi registrada no sistema. O administrador da simulacao podera ler e avaliar sua inteligencia emocional em breve.")
    
    if st.button("Jogar novamente 🔄"):
        st.session_state.passo = "inicio"
        st.rerun()

# --- PAINEL SEGRETO DO ADMINISTRADOR (SIDEBAR) ---
st.sidebar.markdown("<h3 style='text-align: center; color: #fde047 !important;'>⭐ CONTROLE ⭐</h3>", unsafe_allow_html=True)

# Adicionado o st.rerun() aqui para forçar a tela a recarregar na hora do clique
if st.sidebar.button("🔄 Reiniciar Jogo"):
    st.session_state.passo = "inicio"
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("#### 🔐 Painel do Professor / Criador")
senha = st.sidebar.text_input("Digite a senha para ver as respostas:", type="password")

if senha == "1234":
    st.sidebar.success("Acesso Liberado!")
    st.sidebar.markdown("### 📜 Respostas Coletadas:")
    if st.session_state.respostas_usuarios:
        for idx, resp in enumerate(st.session_state.respostas_usuarios):
            st.sidebar.info(f"**Jogador {idx+1}:** {resp}")
    else:
        st.sidebar.write("Nenhuma resposta enviada ainda.")
