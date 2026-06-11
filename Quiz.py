import streamlit as st

# Configuração da aba do navegador
st.set_page_config(page_title="Nosso Jogo de Amor 💖", page_icon="💝", layout="centered")

# Injeção de CSS para deixar tudo rosa com detalhes verdes (Botões Atualizados!)
st.markdown("""
    <style>
    /* Fundo principal rosa bebê */
    .stApp {
        background-color: #ffe6f2; 
    }
    /* Títulos e textos em tons de rosa escuro/magenta */
    h1, h2, h3, h4, h5, h6 {
        color: #d81b60 !important;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    p, label {
        color: #c2185b !important;
        font-size: 18px !important;
        font-weight: bold;
    }
    /* Botões rosa claro com letras verdes */
    .stButton>button {
        background-color: #ffb6c1 !important; /* Fundo rosa claro */
        color: #2e7d32 !important; /* Texto verde */
        border-radius: 15px;
        border: 2px solid #2e7d32; /* Borda verde combinando com a letra */
        padding: 10px 24px;
        font-weight: bold;
        font-size: 18px;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff9aa2 !important; /* Rosa um pouco mais forte ao passar o mouse */
        color: #1b5e20 !important; /* Verde mais escuro ao passar o mouse */
        transform: scale(1.02);
    }
    /* Caixa das opções de resposta */
    .stRadio div[role="radiogroup"] {
        background-color: #ffccdf;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #4CAF50; /* Borda verde pontilhada */
    }
    </style>
""", unsafe_allow_html=True)

# Inicialização de Variáveis no Session State para controlar o fluxo do jogo
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'user_choice' not in st.session_state:
    st.session_state.user_choice = None

# Banco de Perguntas
questions = [
    {
        "q": "1 Questão) Onde foi o nosso primeiro encontro? 💘",
        "options": ["Orla do Paiva", "Patteo", "Mirabilandia", "Bar do rato"],
        "answer": "Patteo"
    },
    {
        "q": "2 Questão) Em que data começamos a namorar? 🗓️💖",
        "options": ["22/09", "19/02", "21/06", "02/12"],
        "answer": "21/06"
    },
    {
        "q": "3 Questão) Aonde você queria me dizer 'Eu te amo'? 🥺💞",
        "options": ["Parada de Ônibus", "Cinema", "Papa Capim", "Disney"],
        "answer": "Parada de Ônibus"
    },
    {
        "q": "4 Questão) Qual é a minha comida favorita? 🍝🤤",
        "options": ["Polvo", "Arroz", "Parmegiana", "Sushi"],
        "answer": "Parmegiana"
    },
    {
        "q": "5 Questão) Qual é a música da nossa foto no Instagram? 🎵💗",
        "options": ["Your Song", "Every Little Thing She Does Is Magic", "Escola do Neiff", "Selfless"],
        "answer": "Selfless"
    },
    {
        "q": "6 Questão) Quem é a pessoa que mais te ama no Universo? 🌍🥰",
        "options": ["EU", "É a letra A", "Escuta a letra B", "CLICA NA A"],
        "answer": "EU"
    },
    {
        "q": "7 Questão) Eu te amo mais do que você me ama? 🤭💝",
        "options": ["Sim", "Não"],
        "answer": "Sim"
    },
    {
        "q": "8 Questão) Vou te amar até o fim dos tempos e continuar te amando para sempre? ♾️💕",
        "options": ["SIM"], 
        "answer": "SIM"
    }
]

# --- TELA INICIAL (Página 0) ---
if st.session_state.page == 0:
    st.title("💖 Bem-vindo ao Nosso Quiz de Amor! 💖")
    st.write("Preparei esse joguinho para testar sua memória sobre nós. Será que você lembra de tudo? 🥰")
    
    try:
        st.image("foto_inicio.png", use_container_width=True, caption="Nós dois juntinhos! 👩‍❤️‍👨")
    except:
        st.info("Coloque uma foto chamada 'foto_inicio.jpg' na mesma pasta do código para ela aparecer aqui! 📸")
    
    st.write("---")
    if st.button("💚 INICIAR O JOGO 💚"):
        st.session_state.page = 1
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()

# --- TELAS DE PERGUNTAS (Páginas 1 a 8) ---
elif 1 <= st.session_state.page <= len(questions):
    q_index = st.session_state.page - 1
    current_q = questions[q_index]
    
    st.title(f"Pergunta {st.session_state.page} de {len(questions)} 💓")
    st.subheader(current_q["q"])
    
    # Renderiza as opções
    choice = st.radio("Escolha sua resposta:", current_q["options"], key=f"radio_{q_index}")
    
    st.write("---")
    
    # Botão de confirmar resposta
    if not st.session_state.answered:
        if st.button("Confirmar Resposta 💚 "):
            st.session_state.answered = True
            st.session_state.user_choice = choice
            
            # Checa se acertou e já pontua
            if choice == current_q["answer"]:
                st.session_state.score += 1
            st.rerun()
            
    # Feedback após responder
    if st.session_state.answered:
        if st.session_state.user_choice == current_q["answer"]:
            st.success(f"💚 VOCÊ ACERTOU, MEU AMOR! 💚 A resposta é mesmo '{current_q['answer']}'! 🎉💘")
        else:
            st.error(f"💔 VOCÊ ERROU! 💔 A resposta correta era: {current_q['answer']}. Poxa Paixão! 🥺")
            
        if st.button("Próxima Pergunta ➡️"):
            st.session_state.page += 1
            st.session_state.answered = False
            st.rerun()

# --- TELA FINAL (Página 9) ---
elif st.session_state.page > len(questions):
    st.title("💖 Fim do Jogo! 💖")
    
    if st.session_state.score == 8:
        msg = "Uau! Você acertou TUDO! Isso só prova que você presta atenção em cada detalhe do nosso amor. Eu te amo infinitamente! 🏆💞"
    elif st.session_state.score >= 5:
        msg = "Você foi muito bem, amor! Lembra de quase tudo sobre a gente. Meu coração é todo seu! 🥰💚"
    else:
        msg = "Parece que alguém precisa reviver nossos momentos para refrescar a memória, hein? 😂 Mas eu continuo te amando do tamanho do universo! 💖"
        
    st.subheader(f"Sua Pontuação: {st.session_state.score} de 8 acertos!")
    st.write(f"### {msg}")
    
    try:
        st.image("foto_final.png", use_container_width=True, caption="Pra sempre nós! ♾️💕")
    except:
        st.info("Coloque uma foto chamada 'foto_final.jpeg' na mesma pasta para aparecer na tela final! 📸")
        
    st.write("---")
    if st.button("Jogar Novamente 🔄💚"):
        st.session_state.page = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()
