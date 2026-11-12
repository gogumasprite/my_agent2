import pandas as pd
import streamlit as st

st.title("위젯 연습")
st.header("엑셀 파일 미리 보기")
st.caption("엑셀 파일을 한 개 또는 여러 개 올려 내용을 확인할 수 있어요.")

files = st.file_uploader(
    "엑셀 파일 선택", type=["xlsx"], accept_multiple_files=True
)
if files:
    selected = st.selectbox(
        "미리 볼 파일", range(len(files)), format_func=lambda index: files[index].name
    )
    if st.button("미리 보기"):
        try:
            st.dataframe(pd.read_excel(files[selected], engine="openpyxl"))
        except (ValueError, OSError):
            st.error("파일을 읽지 못했습니다. 올바른 .xlsx 파일인지 확인해 주세요.")
