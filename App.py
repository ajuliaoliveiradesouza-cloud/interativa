import streamlit as st

st.set_page_config(page_title="Simulador de Inteligência Emocional", page_icon="💼", layout="centered")

# --- BANCO DE DADOS LOCAL DE RESPOSTAS (Sessão Segura) ---
if "respostas_usuarios" not in st.session_state:
    st.session_state.respostas_usuarios = []
if "resposta_salva" not in st.session_state:
    st.session_state.resposta_salva = False
if "cenario_atual" not in st.session_state:
    st.session_state.cenario_atual = "h1_inicio"

# --- INJEÇÃO DE DESIGN AVANÇADO, MÚSICA AMBIENTE E SONS DE CLIQUE ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #070a13 0%, #0f172a 40%, #1e1b4b 100%) !important;
        color: #f8fafc;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    h1 {
        color: #fde047 !important;
        text-shadow: 3px 3px 12px rgba(253, 224, 71, 0.5);
        text-align: center;
        font-weight: 900 !important;
        padding-bottom: 10px;
        letter-spacing: -0.5px;
    }
    h3 {
        color: #f472b6 !important;
        font-weight: 800 !important;
        margin-top: 15px;
        text-shadow: 2px 2px 8px rgba(244, 114, 182, 0.3);
    }
    .custom-box {
        background: linear-gradient(145deg, #2e0854 0%, #4c1d95 100%);
        padding: 26px;
        border-radius: 40px 8px 35px 5px !important;
        border-left: 6px solid #fde047;
        border-right: 2px solid #ec4899;
        border-bottom: 4px solid #ec4899;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.1);
    }
    div.stButton > button {
        background: linear-gradient(135deg, #ec4899 0%, #be185d 100%) !important;
        color: #ffffff !important;
        border: 2px solid #fde047 !important;
        border-radius: 6px 20px 4px 25px !important;
        padding: 16px 22px !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 6px 20px rgba(236, 72, 153, 0.25) !important;
        width: 100% !important;
        white-space: normal !important;
        text-align: left !important;
        display: block !important;
        margin-bottom: 14px !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #a855f7 0%, #7c3aed 100%) !important;
        color: #fde047 !important;
        border-color: #ec4899 !important;
        transform: scale(1.02) translateY(-3px);
        box-shadow: 0 10px 25px rgba(168, 85, 247, 0.5) !important;
    }
    .stTextArea textarea {
        background-color: #0f1123 !important;
        color: #f8fafc !important;
        border: 2px solid #a855f7 !important;
        border-radius: 16px 4px 12px 4px !important;
        padding: 12px !important;
    }
    .thanks-box {
        background: linear-gradient(135deg, #065f46 0%, #047857 100%);
        padding: 20px;
        border-radius: 8px 30px 5px 35px;
        border: 2px solid #34d399;
        text-align: center;
        box-shadow: 0 8px 25px rgba(52, 211, 153, 0.2);
        margin-top: 20px;
    }
    [data-testid="stSidebar"] {
        background-color: #090d16 !important;
        border-right: 2px solid #a855f7;
    }
    hr {
        border-top: 2px dashed #a855f7 !important;
        margin: 25px 0 !important;
    }
    </style>
    <audio id="bg-music" loop autoplay src="https://mixkit.co" volume="0.2"></audio>
    <audio id="bubble-sound" src="https://mixkit.co"></audio>
    <script>
    document.addEventListener('click', function(e) {
        if (e.target.tagName === 'BUTTON') {
            var sound = document.getElementById('bubble-sound');
            if(sound) { sound.currentTime = 0; sound.play(); }
        }
        var bgMusic = document.getElementById('bg-music');
        if (bgMusic && bgMusic.paused) { bgMusic.play(); }
    });
    </script>
    """,
    unsafe_allow_html=True
)
historias = {
    "h1_inicio": {
        "titulo": "✨ 📅 O ÚLTIMO DIA DO MÊS ✨",
        "texto": "O relógio corre contra você. É o último dia do mês e o clima na empresa está puro desespero. Você passa horas grudado ao telefone, com o suor frio escorrendo, sabendo que falta apenas uma única venda para bater a meta e garantir aquela bonificação que vai salvar as suas contas.\\n\\nApós dias de uma negociação exaustiva e cheia de idas e vindas, o cliente finalmente cede. 'Vamos fechar', ele diz. Um alívio gigantesco toma conta do seu peito.\\n\\nVocê abre o sistema com as mãos trêmulas para registrar o pedido, mas, no pior momento possível, a tela congelou. O computador travou completamente. Você aperta loucamente o teclado, tenta reiniciar, mexe nos cabos, mas a máquina simplesmente não responde.\\n\\nEnquanto você entra em pânico tentando resolver o problema técnico, nota que o colega da mesa ao lado — que vinha acompanhando seu esforço de longe — se levanta de fininho. Ele assume a ligação com o seu cliente e, sem o menor pudor, fecha a venda em seu lugar.\\n\\nQuando o seu sistema finalmente volta a funcionar, o estômago embrulha: o painel mostra que a comissão já foi registrada no nome dele. O expediente está no fim, não há mais tempo para correr atrás de outro cliente e a sua bonificação acabou de escorrer pelos dedos.",
        "audio": "https://soundhelix.com",
        "opcoes": {
            "Vou direto até a mesa dele e tiro a limpo ali mesmo, na frente de todo mundo, exigindo que ele repasse a venda para o meu nome.": "h1_confronto",
            "Respiro fundo para controlar a onda de raiva, pego o histórico de conversas com o cliente e procuro o gerente em particular para relatar o ocorrido.": "h1_gerente",
            "Engulo a seco, fecho a minha gaveta com força, guardo minhas coisas e vou embora para casa sem falar com ninguém, remoendo o ódio.": "h1_silencio"
        }
    },
    "h1_confronto": {
        "titulo": "🔥 O Confronto Público ✨",
        "texto": "Você avança até a mesa dele com sangue nos olhos e grita que ele é um ladrão de metas. O escritório inteiro fica em silêncio. O colega se faz de vítima e diz que apenas 'salvou o cliente que estava esperando'. O gerente sai da sala dele furioso com o escândalo. Por ter perdido o controle emocional em público, você é advertido e o gerente se recusa a ouvir sua versão naquele dia. Você perdeu a razão e a bonificação.",
        "audio": None,
        "opcoes": {
            "Pedir desculpas pelo tom de voz e solicitar uma reunião formal amanhã.": "h1_confronto_reparar",
            "Continuar batendo boca e ameaçar processar a empresa.": "h1_confronto_demissao"
        }
    },
    "h1_gerente": {
        "titulo": "📈 ✨ A Abordagem Profissional ✨",
        "texto": "Na sala do gerente, você apresenta os fatos friamente: o histórico de e-mails, as mensagens e o horário do travamento. O gerente elogia sua postura controlada. Ele reconhece o seu esforço e decide dividir a comissão entre você e o colega, garantindo que sua meta seja computada para a bonificação. Além disso, o colega fica com a reputação manchada perante a liderança.",
        "audio": None,
        "opcoes": {
            "Agradecer ao gerente e propor uma melhoria no sistema de TI para evitar novos travamentos.": "h1_fim_perfeito",
            "Aceitar, mas mandar uma indireta ácida para o colega no grupo de WhatsApp da equipe.": "h1_confronto"
        }
    },
    "h1_silencio": {
        "titulo": "🌧️ ✨ O Ruminar Silencioso ✨",
        "texto": "Você chega em casa destruído e desconta a frustração na sua família. No dia seguinte, seu rendimento despenca e o clima fica insuportável. O colega percebe que você não reagiu e começa a montar em cima de você, roubando novas ideias suas em reuniões, sabendo que você aceita tudo calado.",
        "audio": None,
        "opcoes": {
            "Decidir engolir o orgulho e procurar o RH para relatar o histórico de abusos.": "h1_rh",
            "Continuar fingindo que nada aconteceu até estourar de vez.": "h1_confronto_demissao"
        }
    },
    "h1_confronto_reparar": {"titulo": "✨ Conclusão do Cenário ✨", "texto": "Você reconhece o erro do estouro emocional. O gerente aceita conversar no dia seguinte e, vendo seu arrependimento, aceita analisar o caso da venda. Você não ganha a comissão toda, mas salva metade do bônus. Lição aprendida. ✨", "audio": None, "opcoes": {}},
    "h1_confronto_demissao": {"titulo": "❌ Fim de Jogo ❌", "texto": "Sua falta de controle passa dos limites. A diretoria intervém e você é demitido por justa causa por insubordinação e ameaças. Sem bônus, sem emprego e com as portas fechadas no setor.", "audio": None, "opcoes": {}},
    "h1_fim_perfeito": {"titulo": "⭐ Sucesso Absoluto ⭐", "texto": "Sua maturidade foi além de resolver o conflito: você ajudou a empresa. Três meses depois, o gerente te promove a supervisor pela sua alta inteligência emocional e capacidade de liderança. 🎉", "audio": None, "opcoes": {}},
    "h1_rh": {"titulo": "✨ Justiça Feita ✨", "texto": "O RH abre uma investigação interna por conduta antiética contra o colega. Com as provas que você guardou, ele é transferido de setor e você recebe o estorno do seu bônus de forma retroativa. ⚖️", "audio": None, "opcoes": {}},
    "h2_inicio": {
        "titulo": "👔 DECEPÇÃO E MERITOCRACIA",
        "texto": "Você trabalha há 5 anos na empresa e é o melhor do seu setor. Você é referência absoluta e todo mundo te procura por ajuda e pede a sua opinião antes de tomar qualquer decisão importante.\\n\\nDepois de 5 anos dedicados, você sente que está estagnado e que já merecia ter sido promovido há muito tempo. Seu salário e suas demandas simplesmente não acompanham tudo o que você faz pela empresa no dia a dia.\\n\\nFinalmente, abriu uma vaga para a função que você quer faz muito tempo e que vai te permitir crescer ainda mais. A empresa abre o processo seletivo interno e você vai super confiante. Todo mundo nos corredores sabe e comenta que você é a escolha óbvia.\\n\\nMas no dia do resultado vem o choque de realidade: o sobrinho do gerente, que acabou de se formar na faculdade, nunca trabalhou na área e nem sequer fazia parte da empresa, é contratado diretamente em seu lugar.",
        "audio": "https://soundhelix.com",
        "opcoes": {
            "Entrar na sala do gerente exigindo uma explicação clara sobre os critérios da escolha, deixando claro que isso foi um ato de puro nepotismo.": "h2_confronto",
            "Aceito a situação externamente com profissionalismo, mas decido que a partir de hoje farei apenas o mínimo estrito do meu contrato enquanto procuro outro emprego secretamente.": "h2_quiet_quitting",
            "Procuro o novo contratado (o sobrinho) para me colocar à disposição, decidindo agir de forma estratégica para ganhar a confiança dele e do gerente enquanto avalio meus próximos passos.": "h2_estrategia"
        }
    },
    "h2_confronto": {
        "titulo": "⚡ Portas Fechadas",
        "texto": "O gerente se defende dizendo que o sobrinho trouxe uma 'visão moderna e acadêmica'. Sua acusação direta de nepotismo cria uma parede de gelo entre vocês. A partir desse dia, o gerente começa a te cortar de reuniões importantes e passa a monitorar cada minuto do seu dia para achar uma desculpa para te demitir.",
        "audio": None,
        "opcoes": {
            "Pedir demissão imediatamente para preservar seu orgulho, mesmo sem outra vaga garantida.": "h2_demissao_imediata",
            "Engolir o orgulho temporariamente e abrir uma denúncia formal no canal de ética confidencial da empresa.": "h2_canal_etica"
        }
    },
    "h2_quiet_quitting": {
        "titulo": "🐢 Operação Padrão",
        "texto": "Você para de resolver os problemas dos outros e passa a ignorar e-mails fora do horário. A equipe, que dependia de você, começa a bater cabeça e o setor desanda. O sobrinho do gerente, completamente perdido na função, percebe que você puxou o freio de mano e te dá uma advertência formal por falta de engajamento corporativo.",
        "audio": None,
        "opcoes": {
            "Usar a reunião de feedback para jogar as verdades na cara dele e dizer que ele não tem competência para estar ali.": "h2_confronto",
            "Ignorar a advertência, acelerar os processos seletivos em outras empresas e pedir as contas assim que passar em uma.": "h2_novo_emprego"
        }
    },
    "h2_estrategia": {
        "titulo": "🧠 Inteligência Estratégica",
        "texto": "Ao se mostrar prestativo, você vira o porto seguro do rapaz. Em poucas semanas, o sobrinho percebe que sem o seu apoio ele será desmascarado por incompetência. Grato pela sua ajuda, ele te promove a 'Coordenador Técnico' com um aumento salarial expressivo, repassando a autonomia do setor para as suas mãos na prática.",
        "audio": None,
        "opcoes": {
            "Ficar na empresa aproveitando o ótimo salário e a liderança real dos bastidores.": "h2_lider_sombra",
            "Usar o seu novo cargo de Coordenador e o salário atualizado para rechear seu currículo e aplicar para vagas de Gerente na concorrência.": "h2_concorrente_topo"
        }
    },
    "h2_demissao_imediata": {"titulo": "❌ Fim de Jogo ❌", "texto": "Seu impulso emocional te deixa desempregado e sem renda. O mercado de trabalho está difícil e você se arrepende de não ter planejado a sua transição com mais calma"h3_inicio": {
        "titulo": "🚨 ALERTA DE RISCO IMINENTE",
        "texto": "Você é o supervisor de turno em uma área operacional crítica. Faltam trinta minutos para encerrar o expediente e a equipe está exausta, louca para ir embora. De repente, você nota que uma das válvulas principais de pressão está operando no limite vermelho, apresentando um ruído anormal. Ignorar isso pode causar um acidente de trabalho grave nas próximas horas, mas interromper a produção agora vai estourar o prazo de entrega de um cliente vital para a empresa, e o gerente geral deixou claro que nenhuma parada seria tolerada hoje.",
        "audio": "https://soundhelix.com",
        "opcoes": {
            "Decido ignorar o alerta, torcendo para que a máquina aguente até o próximo turno assumir, evitando o conflito com a gerência.": "h3_ignorar",
            "Aperto o botão de parada de emergência imediatamente para garantir a segurança física de todos, mesmo sabendo que serei duramente cobrado pelo prejuízo.": "h3_parada",
            "Chamo o técnico de manutenção mais experiente para uma avaliação rápida em segredo, tentando achar uma solução sem parar a linha.": "h3_tecnico"
        }
    },
    "h3_ignorar": {"titulo": "💥 O Desastre Operacional", "texto": "A sua omissão custou caro. Dez minutos após a sua saída, a válvula explode, ferindo gravemente um operador do turno da noite e paralisando a fábrica por semanas. A perícia técnica abre uma investigação e descobre que você ignorou os alertas do sistema. A empresa te desliga por justa causa e você responde judicialmente por negligência, com sua reputação profissional totalmente destruída.", "audio": None, "opcoes": {}},
    "h3_parada": {
        "titulo": "⚡ O Confronto com a Chefia",
        "texto": "O gerente geral desce até a pista enfurecido com a parada e esbraveja na frente da equipe, acusando você de incompetência e de arruinar o contrato do mês. Você sente o sangue ferver diante do desrespeito.",
        "audio": None,
        "opcoes": {
            "Bato de frente com o gerente no mesmo tom de voz, afirmando que ele não se importa com a vida dos funcionários e que a culpa é da falta de manutenção.": "h3_briga",
            "Mantenho a calma, puxo o relatório de medição da válvula e explico friamente o risco iminente de explosão, oferecendo um plano rápido para retomar a produção em segurança.": "h3_gerente_frio"
        }
    },
    "h3_tecnico": {
        "titulo": "⏳ Corrida Contra o Relógio",
        "texto": "O técnico avalia e diz que a peça está prestes a romper, mas que ele consegue fazer uma gambiarra temporária de dez minutos se você assumir o risco de mantê-la ligada enquanto ele mexe.",
        "audio": None,
        "opcoes": {
            "Autorizo o procedimento arriscado na tentativa de salvar a meta do dia a qualquer custo.": "h3_ignorar",
            "Recuso firmemente o risco à vida do técnico, ordeno o isolamento da área e formalizo o chamado de manutenção pesada.": "h3_parada"
        }
    },
    "h3_briga": {"titulo": "❌ Insubordinação Crítica", "texto": "Apesar de estar certo sobre o risco técnico, o seu estouro emocional e a humilhação pública contra o seu superior quebram a hierarquia. O gerente te suspende por insubordinação. O comitê de ética valida o risco da máquina, mas pune severamente a sua falta de postura profissional. Sua chances de crescimento na empresa morrem aqui.", "audio": None, "opcoes": {}},
    "h3_gerente_frio": {"titulo": "🏆 Liderança de Elite", "texto": "Sua maturidade foi além de resolver o conflito: você ajudou a empresa. Tres meses depois, o gerente te promove a supervisor pela sua alta inteligência emocional e capacidade de liderança. Perfeito!", "audio": None, "opcoes": {}}
}

no_atual = historias[st.session_state.cenario_atual]

st.title("💼 Simulador de Inteligência Emocional")

if "titulo" in no_atual:
    st.markdown(f"### {no_atual['titulo']}")

st.markdown(f"<div class='custom-box'>{no_atual['texto']}</div>", unsafe_allow_html=True)

if "audio" in no_atual and no_atual["audio"]:
    st.markdown("🔊 **Ouça a narração da história:**")
    st.audio(no_atual["audio"])

st.markdown("<hr>", unsafe_allow_html=True)

if "opcoes" in no_atual and no_atual["opcoes"]:
    st.markdown("<h4 style='color: #fde047; margin-bottom: 15px;'>🧭 COMO VOCÊ REAGE?</h4>", unsafe_allow_html=True)
    for texto_opcao, proximo_passo in no_atual["opcoes"].items():
        if st.button(texto_opcao, key=texto_opcao):
            st.session_state.cenario_atual = proximo_passo
            st.rerun()
else:
    if not st.session_state.resposta_salva:
        st.markdown("<h4 style='color: #fde047; margin-bottom: 15px;'>📝 CONSIDERAÇÕES FINAIS</h4>", unsafe_allow_html=True)
        resposta_usuario = st.text_area("Diante de todo esse desfecho, o que você faria de agora em diante ou qual lição você tira disso?", placeholder="Escreva sua reflexão ou atitude final aqui...", height=120)
        if st.button("Gravar Resposta Final 🚀"):
            if resposta_usuario.strip() != "":
                st.session_state.respostas_usuarios.append(f"Cenário [{st.session_state.cenario_atual}]: {resposta_usuario}")
                st.session_state.resposta_salva = True
                st.rerun()
            else:
                st.warning("Escreva algo na caixa de texto antes de salvar!")
    else:
        st.markdown("<div class='thanks-box'><h3 style='color: #fde047 !important; margin-top: 0px;'>💖 Muito obrigado por participar!</h3><p style='font-size: 1.1rem; margin-bottom: 0px;'>Sua reflexão sobre Inteligência Emocional foi gravada com sucesso e enviada ao painel do avaliador. Seu aprendizado é o primeiro passo para o sucesso corporativo! ✨🌟</p></div>", unsafe_allow_html=True)

st.sidebar.markdown("<h3 style='text-align: center; color: #fde047 !important;'>⭐ CONTROLE ⭐</h3>", unsafe_allow_html=True)

if st.sidebar.button("🔄 Reiniciar História"):
    if st.session_state.cenario_atual.startswith("h1_"):
        st.session_state.cenario_atual = "h2_inicio"
    elif st.session_state.cenario_atual.startswith("h2_"):
        st.session_state.cenario_atual = "h3_inicio"
    else:
        st.session_state.cenario_atual = "h1_inicio"
    st.session_state.resposta_salva = False
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
        st.sidebar.write("Nenhuma resposta enviada ainda."). Faltou estratégia racional aqui.", "audio": None, "opcoes": {}},
    "h2_canal_etica": {"titulo": "✨ Justiça Feita ✨", "texto": "A auditoria da matriz investiga a contratação e comprova o favorecimento ilegal. O gerente geral é demitido por quebra de compliance e o sobrinho é desligado da empresa. A diretoria te convoca para assumir a gerência imediatamente.", "audio": None, "opcoes": {}},
    "h2_novo_emprego": {"titulo": "🚀 Novo Rumo 🚀", "texto": "Um mês depois, você aceita uma vaga em um concorrente direto ganhando 40% a mais. No seu último dia de aviso prévio, você vê o setor antigo entrar em colapso total porque ninguém sobrou para guiar o sobrinho perdido. Você mudou de patamar.", "audio": None, "opcoes": {}},
    "h2_lider_sombra": {"titulo": "⭐ Líder de Bastidores ⭐", "texto": "Você virou o verdadeiro comandante do setor. O trabalho é tranquilo, seu bolso está cheio e o sobrinho é quem leva as broncas da diretoria executiva quando algo dá errado na operação. Inteligência pura.", "audio": None, "opcoes": {}},
    "h2_concorrente_topo": {"titulo": "🏆 No Topo do Mercado 🏆", "texto": "Uma multinacional vê seu currículo updated, sua bagagem de 5 anos e seu cargo recente de coordenação. Eles te contratam direto como Gerente de Divisão. Quem não te deu valor no passado agora assiste ao seu sucesso de longe.", "audio": None, "opcoes": {}},
    
