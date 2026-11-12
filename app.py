import streamlit as st

st.set_page_config(page_title="우리 회사 챗봇")

pages = st.navigation(
    [
        st.Page("page_1.py", title="채팅 연습"),
        st.Page("page_2.py", title="AI 챗봇", default=True),
        st.Page("page_3.py", title="위젯 연습"),
    ],
    position="top",
)
pages.run()
