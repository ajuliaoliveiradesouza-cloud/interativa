import streamlit as st

st.set_page_config(page_title="Simulador de Inteligência Emocional", page_icon="💼", layout="centered")

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
        white-space: normal !important;
        text-align: left !important;
        display: block !important;
        margin-bottom: 12px !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #a855f7 0%, #9333ea 100%) !important;
        color: #fde047 !important;
        border-color: #ec4899 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.5) !important;
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

historias = {
    "inicio": {
        "titulo": "✨ 📅 O ÚLTIMO DIA DO MÊS ✨",
        "texto": "O relógio corre contra você. É o último dia do mês e o clima na empresa está puro desespero. Você passa horas grudado ao telefone, com o suor frio escorrendo, sabendo que falta apenas uma única venda para bater a meta e garantir aquela bonificação que vai salvar as suas contas.\n\nApós dias de uma negociação exaustiva e cheia de idas e vindas, o cliente finalmente cede. 'Vamos fechar', ele diz. Um alívio gigantesco toma conta do seu peito.\n\nVocê abre o sistema com as mãos trêmulas para registrar o pedido, mas, no pior momento possível, a tela congela. O computador travou completamente. Você aperta loucamente o teclado, tenta reiniciar, mexe nos cabos, mas a máquina simplesmente não responde.\n\nEnquanto você entra em pânico tentando resolver o problema técnico, nota que o colega da mesa ao lado — que vinha acompanhando seu esforço de longe — se levanta de fininho. Ele assume a ligação com o seu cliente e, sem o menor pudor, fecha a venda no lugar dele.\n\nQuando o seu sistema finalmente volta a funcionar, o estômago embrulha: o painel mostra que a comissão já foi registrada no nome dele. O expediente está no fim, não há mais tempo para correr atrás de outro cliente e a sua bonificação acabou de escorrer pelos dedos.",
        "opcoes": {
            "Vou direto até a mesa dele e tiro a limpo ali mesmo, na frente de todo mundo, exigindo que ele repasse a venda para o meu nome.": "confronto",
            "Respiro fundo para controlar a onda de raiva, pego o histórico de conversas com o cliente e procuro o gerente em particular para relatar o ocorrido.": "gerente",
            "Engulo a seco, fecho a minha gaveta com força, guardo minhas coisas e vou embora para casa sem falar com ninguém, remoendo o ódio.": "silencio"
        }
    },
    "confronto": {
        "titulo": "💥 🔥 O Confronto Público ✨",
        "texto": "Você avança até a mesa dele com sangue nos olhos e grita que ele é um ladrão de metas. O escritório inteiro fica em silêncio. O colega se faz de vítima e diz que apenas 'salvou o cliente que estava esperando'. O gerente sai da sala dele furioso com o escândalo. Por ter perdido o controle emocional em público, você é advertido e o gerente se recusa a ouvir sua versão naquele dia. Você pediu a razão e a bonificação.",
        "opcoes": {
            "Pedir desculpas pelo tom de voz e solicitar uma reunião formal amanhã.": "confronto_reparar",
            "Continuar batendo boca e ameaçar processar a empresa.": "confronto_demissao"
        }
    },
    "gerente": {
        "titulo": "📈 ✨ A Abordagem Profissional ✨",
        "texto": "Na sala do gerente, você apresenta os fatos friamente: o histórico de e-mails, as mensagens e o horário do travamento. O gerente elogia sua postura controlada. Ele reconhece o seu esforço e decide dividir a comissão entre você e o colega, garantindo que sua meta seja computada para a bonificação. Além disso, o colega fica com a reputação manchada com a liderança.",
        "opcoes": {
            "Agradecer ao gerente e propor uma melhoria no sistema de TI para evitar novos travamentos.": "fim_perfeito",
            "Aceitar, mas mandar uma indireta ácida para o colega no grupo de WhatsApp da equipe.": "confronto"
        }
    },
    "silencio": {
        "titulo": "🌧️ ✨ O Ruminar Silencioso ✨",
        "texto": "Você chega em casa destruído e desconta a frustração na sua família. No dia seguinte, seu rendimento despenca e o clima fica insuportável. O colega percebe que você não reagiu e começa a montar em cima de você, roubando novas ideias suas em reuniões, sabendo que você aceita tudo calado.",
        "opcoes": {
            "Decidir engolir o orgulho e procurar o RH para relatar o histórico de abusos.": "rh",
            "Continuar fingindo que nada aconteceu até estourar de vez.": "confronto_demissao"
        }
    },
    "confronto_reparar": {
        "titulo": "✨ Conclusão do Cenário ✨",
        "texto": "Você reconhece o erro do estouro emocional. O gerente aceita conversar no dia seguinte e, vendo seu arrependimento, aceita analisar o caso da venda. Você não ganha a comissão toda, mas salva metade do bônus. Lição aprendida. ✨",
        "opcoes": {}
    },
    "confronto_demissao": {
        "titulo": "❌ Fim de Jogo ❌",
        "texto": "Sua falta de controle passa dos limites. A diretoria intervém e você é demitido por justa causa por insubordinação e ameaças. Sem bônus, sem emprego e com as portas fechadas no setor.",
        "opcoes": {}
    },
    "fim_perfeito": {
        "titulo": "⭐ Sucesso Absoluto ⭐",
        "texto": "Sua maturidade foi além de resolver o conflito: você ajudou a empresa. Três meses depois, o gerente te promove a supervisor pela sua alta inteligência emocional e capacidade de liderança. 🎉",
        "opcoes": {}
    },
    "rh": {
        "titulo": "✨ Justiça Feita ✨",
        "texto": "O RH abre uma investigação interna por conduta antiética contra o colega. Com as provas que você guardou, ele é transferido de setor e você recebe o estorno do seu bônus de forma retroativa. ⚖️",
        "opcoes": {}
    }
}

no_atual = historias[st.session_state.passo]

st.title("💼 Simulador de Inteligência Emocional")

if "titulo" in no_atual:
    st.markdown(f"### {no_atual['titulo']}")

st.markdown(f"<div style='background-color: #3b0764; padding: 22px; border-radius: 20px 4px 15px 5px; border-left: 5px solid #fde047; margin-bottom: 25px;'>{no_atual['texto']}</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

if "opcoes" in no_atual and no_atual["opcoes"]:
    st.markdown("<h4 style='color: #fde047; margin-bottom: 15px;'>🧭 COMO VOCÊ REAGE?</h4>", unsafe_allow_html=True)
    for texto_opcao, proximo_passo in no_atual["opcoes"].items():
        if st.button(texto_opcao, key=texto_opcao):
            st.session_state.passo = proximo_passo
            st.rerun()
else:
    st.markdown("<h4 style='color: #fde047; margin-bottom: 15px;'>📝 CONSIDERAÇÕES FINAIS</h4>", unsafe_allow_html=True)
    resposta_usuario = st.text_area("Diante de todo esse desfecho, o que você faria de agora em diante ou qual lição você tira disso?", placeholder="Escreva sua reflexão ou atitude final aqui...", height=120)
    
    if st.button("Gravar Resposta Final 🚀"):
        if resposta_usuario.strip() != "":
            st.session_state.respostas_usuarios.append(f"Cenário [{st.session_state.passo}]: {resposta_usuario}")
            st.success("Sua reflexão final foi salva com sucesso no painel!")
        else:
            st.warning("Escreva algo na caixa de texto antes de salvar!")

st.sidebar.markdown("<h3 style='text-align: center; color: #fde047 !important;'>⭐ CONTROLE ⭐</h3>", unsafe_allow_html=True)

if st.sidebar.button("🔄 Reiniciar História"):
    st.session_state.passo = "inicio"
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("#### 🔐 Painel do Criador")
senha = st.sidebar.text_input("Digite a senha para ver as respostas:", type="password")

if senha == "1234":
    st.sidebar.success("Acesso Liberado!")
    st.sidebar.markdown("### 📜 Respostas Coletadas:")
    if st.session_state.respostas_usuarios:
        for idx, resp in enumerate(st.session_state.respostas_usuarios):
            st.sidebar.info(f"**Jogador {idx+1}:** {resp}")
    else:
        st.sidebar.write("Nenhuma resposta enviada ainda.")
