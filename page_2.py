import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

st.title("우리 회사 챗봇")
st.write("채팅을 입력하세요.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if not os.getenv("OPENAI_API_KEY"):
    st.info("OPENAI_API_KEY를 설정하면 챗봇을 사용할 수 있습니다.")
    st.stop()

if prompt := st.chat_input("무엇이든 물어보세요"):
    user_message = {"role": "user", "content": prompt}
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            model = init_chat_model("gpt-5.4-mini", model_provider="openai")
            with st.spinner("답변을 작성하고 있어요."):
                response = model.invoke([*st.session_state.messages, user_message])
            answer = response.text
        except Exception as error:
            st.error(f"답변을 가져오지 못했습니다 ({type(error).__name__}).")
        else:
            st.markdown(answer)
            st.session_state.messages.extend(
                [user_message, {"role": "assistant", "content": answer}]
            )
