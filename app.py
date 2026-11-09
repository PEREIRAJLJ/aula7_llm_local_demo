import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="ML III - Assistente Local",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 ML III — Robô Assitente")
st.caption("Streamlit → FastAPI → Ollama → Mistral")

st.write(
    "Este mini-chat utiliza um Large Language Model rodando localmente no computador. "
    "O histórico da conversa é mantido durante a sessão para que o modelo receba o contexto anterior."
)

temperature = st.slider(
    "Temperatura",
    min_value=0.0,
    max_value=1.5,
    value=0.7,
    step=0.1,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "Você é um assistente didático para alunos de Machine Learning. "
                "Responda em português, de forma clara, objetiva e tecnicamente correta."
            ),
        }
    ]

for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Digite sua mensagem...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "messages": st.session_state.messages,
                        "temperature": temperature,
                    },
                    timeout=180,
                )
                response.raise_for_status()
                result = response.json()

                if "erro" in result:
                    st.error(result["erro"])
                else:
                    answer = result["resposta"]
                    st.markdown(answer)

                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )

            except requests.exceptions.ConnectionError:
                st.error(
                    "Não consegui conectar à API FastAPI. "
                    "Execute primeiro: python -m uvicorn api:app --reload"
                )

            except Exception as e:
                st.error(f"Erro inesperado: {e}")

if st.button("Limpar conversa"):
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "Você é um assistente didático para alunos de Machine Learning. "
                "Responda em português, de forma clara, objetiva e tecnicamente correta."
            ),
        }
    ]
    st.rerun()
