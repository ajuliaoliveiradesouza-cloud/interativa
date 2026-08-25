import streamlit as st

st.set_page_config(page_title="Simulador de Inteligencia Emocional", page_icon="💼", layout="centered")
st.title("💼 Simulador de Inteligencia Emocional")

if "passo" not in st.session_state:
    st.session_state.passo = "inicio"

historias = {
    "inicio": {
        "titulo": "📅 O ULTIMO DIA DO MES",
        "texto": "O relogio corre contra voce. E o ultimo dia do mes e o clima na empresa esta puro desespero. Voce passa horas grudado ao telefone, com o suor frio escorrendo, sabendo que falta apenas uma unica venda para bater a meta e garantir aquela bonificacao que vai salvar as suas contas.\n\nApos dias de uma negociacao exaustiva e cheia de idas e vindas, o cliente finalmente cede. 'Vamos fechar', ele diz. Um alivio gigantesco toma conta do seu peito.\n\nVoce abre o sistema com as manos tremulas para registrar o pedido, mas, no pior momento possivel, a tela congela. O computador travou completamente. Voce aperta loucamente o teclado, tenta reiniciar, mexe nos cabos, mas a maquina simplesmente nao responde.\n\nEnquanto voce entra em panico tentando resolver o problema tecnico, nota que o colega da mesa ao lado que vinha acompanhando seu esforco de longe se levanta de fininho. Ele assume a ligacao com o seu cliente e, sem o menor pudor, fecha a venda no lugar dele.\n\nQuando o seu sistema finalmente volta a funcionar, o estomago embrulha: o painel mostra que a comissao ja foi registrada no nome dele. O expediente esta no fim, nao ha mais tempo para correr atras de outro cliente e a sua bonificacao acabou de escorrer pelos dedos.",
        "opcoes": {
            "Vou direto ate a mesa dele e tiro a limpo ali mesmo, na frente de todo mundo, exigindo que ele repasse a venda para o meu nome.": "confronto",
            "Respiro fundo para controlar a onda de raiva, pego o historico de conversas com o cliente e procuro o gerente em particular para relatar o ocorrido.": "gerente",
            "Engulo a seco, fecho a minha gaveta com forca, guardo minhas coisas e vou embora para casa sem falar com ninguem, remoendo o odio.": "silencio"
        }
    },
    "confronto": {
        "titulo": "🔥 O Confronto Publico",
        "texto": "Voce avanca ate a mesa dele com sangue nos olhos e grita que ele e um ladrao de metas. O escritorio inteiro fica em silencio. O colega se faz de vitima e diz que apenas 'salvou o cliente que estava esperando'. O gerente sai da sala dele furioso com o escandalo. Por ter perdido o controle emocional em publico, voce e advertido e o gerente se recusa a ouvir sua versao naquele dia. Voce perdeu a razao e a bonificacao.",
        "opcoes": {
            "Pedir desculpas pelo tom de voz e solicitar uma reuniao formal amanha.": "confronto_reparar",
            "Continuar batendo boca e ameacar processar a empresa.": "confronto_demissao"
        }
    },
    "gerente": {
        "titulo": "📈 A Abordagem Profissional",
        "texto": "Na sala do gerente, voce apresenta os fatos friamente: o historico de e-mails, as mensagens e o horario do travamento. O gerente elogia sua postura controlada. Ele reconhece o seu esforco e decide dividir a comissao entre voce e o colega, garantindo que sua meta seja computada para a bonificacao. Alem disso, o colega fica com a reputacao manchada com a lideranca.",
        "opcoes": {
            "Agradecer ao gerente e propor uma melhoria no sistema de TI para evitar novos travamentos.": "fim_perfeito",
            "Aceitar, mas mandar uma indireta acida para o colega no grupo de WhatsApp da equipe.": "confronto"
        }
    },
    "silencio": {
        "titulo": "🌧️ O Ruminar Silencioso",
        "texto": "Voce chega em casa destruido e desconta a frustracao na sua familia. No dia seguinte, seu rendimento despenca e o clima fica insuportavel. O colega percebe que voce nao reagiu e comeca a montar em cima de voce, roubando novas ideias suas em reunioes, sabendo que voce aceita tudo calado.",
        "opcoes": {
            "Decidir engolir o orgulho e procurar o RH para relatar o historico de abusos.": "rh",
            "Continuar fingindo que nada aconteceu ate estourar de vez.": "confronto_demissao"
        }
    },
    "confronto_reparar": {
        "texto": "Voce reconhece o erro do estouro emocional. O gerente aceita conversar no dia seguinte e, vendo seu arrependimento, aceita analisar o caso da venda. Voce nao ganha a comissao toda, mas salva metade do bonus. Licao aprendida.",
        "opcoes": {"Jogar novamente 🔄": "inicio"}
    },
    "confronto_demissao": {
        "texto": "Sua falta de controle passa dos limites. A diretoria intervem e voce e demitido por justa causa por insubordinacao e ameacas. Sem bonus, sem emprego e com as portas fechadas no setor.",
        "opcoes": {"Jogar novamente 🔄": "inicio"}
    },
    "fim_perfeito": {
        "texto": "Sua maturidade foi alem de resolver o conflito: você ajudou a empresa. Tres meses depois, o gerente te promove a supervisor pela sua alta inteligencia emocional e capacidade de lideranca.",
        "opcoes": {"Jogar novamente 🔄": "inicio"}
    },
    "rh": {
        "texto": "O RH abre uma investigacao interna por conduta antietica contra o colega. Com as provas que voce guardou, ele e transferido de setor e voce recebe o estorno do seu bonus de forma retroativa.",
        "opcoes": {"Jogar novamente 🔄": "inicio"}
    }
}

no_atual = historias[st.session_state.passo]

if "titulo" in no_atual:
    st.markdown(f"### {no_atual['titulo']}")

st.write(no_atual["texto"])
st.markdown("---")

if "opcoes" in no_atual and no_atual["opcoes"]:
    st.markdown("#### 🧭 COMO VOCE REAGE?")
    for texto_opcao, proximo_passo in no_atual["opcoes"].items():
        if st.button(texto_opcao, key=texto_opcao):
            st.session_state.passo = proximo_passo
            st.rerun()

st.sidebar.markdown("### ⚙️ Painel")
if st.sidebar.button("🔄 Reiniciar História"):
    st.session_state.passo = "inicio"
    st.rerun()
