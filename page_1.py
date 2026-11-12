import streamlit as st

st.title("채팅 연습")

if "practice_messages" not in st.session_state:
    st.session_state.practice_messages = []

if prompt := st.chat_input("무엇을 도와드릴까요?"):
    st.session_state.practice_messages.append({"role": "user", "content": prompt})
    st.session_state.practice_messages.append(
        {"role": "assistant", "content": "반갑습니다."}
    )

for message in st.session_state.practice_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
